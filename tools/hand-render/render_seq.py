"""Render a sequence of toon frames with a shared fixed crop.
usage: render_seq.py <xml> <out_prefix> <frames.json> <style.json>
frames.json: [{"rot": [rx, ry, rz] (deg, world axes, applied to palm), "q": {...}}, ...]
"""
import sys, json, mujoco, numpy as np
from PIL import Image
from scipy import ndimage
from scipy.spatial.transform import Rotation as R

xml, prefix = sys.argv[1], sys.argv[2]
frames, st = json.load(open(sys.argv[3])), json.load(open(sys.argv[4]))
S, OUT = st.get("S", 1000), st.get("out", 200)
hx = lambda c: np.array([int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)])
BODY, TIP, LINE = [hx(c) for c in st["body"]], [hx(c) for c in st["tip"]], hx(st["line"])

m = mujoco.MjModel.from_xml_path(xml)
m.vis.global_.offwidth = m.vis.global_.offheight = S
m.vis.global_.fovy = 8
m.vis.headlight.ambient[:] = .35; m.vis.headlight.diffuse[:] = .75; m.vis.headlight.specular[:] = 0
d = mujoco.MjData(m)
palm = m.body("palm").id
q0 = m.body_quat[palm].copy()
opt = mujoco.MjvOption(); opt.geomgroup[:] = 0; opt.geomgroup[2] = 1
cam = mujoco.MjvCamera()
cam.lookat[:] = st.get("lookat", [0.05, 0, 0]); cam.distance = st.get("dist", 3.6)
cam.azimuth, cam.elevation = 0, -89.9
r = mujoco.Renderer(m, S, S)
white_geoms = [g for g in range(m.ngeom) if m.geom_matid[g] >= 0 and m.material(m.geom_matid[g]).name == "white"]

def toon(rgb, seg):
    mask = seg >= 0
    white = np.isin(seg, white_geoms)
    lum = rgb.mean(-1)
    img = np.zeros((S, S, 4))
    for sel, cols in ((mask & ~white, BODY), (white, TIP)):
        if sel.any():
            v = lum[sel]; lo, hi = np.percentile(v, [30, 80])
            img[sel, :3] = np.array(cols)[np.where(v < lo, 0, np.where(v < hi, 1, 2))]
    img[mask, 3] = 1
    inner = np.zeros_like(mask)
    inner[:-1] |= seg[:-1] != seg[1:]; inner[:, :-1] |= seg[:, :-1] != seg[:, 1:]
    inner = ndimage.binary_dilation(inner & mask, iterations=st["inner_w"]) & mask
    sil = ndimage.binary_dilation(mask, iterations=st["outline_w"]) & ~mask
    img[inner, :3] = LINE; img[sil, :3] = LINE; img[sil, 3] = 1
    return img

out = []
for f in frames:
    rot = R.from_euler("xyz", f.get("rot", [0, 0, 0]), degrees=True)
    base = R.from_quat(q0[[1, 2, 3, 0]])
    qq = (rot * base).as_quat()
    m.body_quat[palm] = qq[[3, 0, 1, 2]]
    d.qpos[:] = 0
    for k, v in f.get("q", {}).items():
        d.qpos[m.joint(k).qposadr[0]] = v
    mujoco.mj_forward(m, d)
    r.update_scene(d, cam, opt); rgb = r.render().astype(float) / 255
    r.enable_segmentation_rendering(); r.update_scene(d, cam, opt); seg = r.render()[..., 0]
    r.disable_segmentation_rendering()
    out.append(toon(rgb, seg))

# shared crop: union bbox of all frames, padded to a square
alpha = np.max([o[..., 3] for o in out], 0)
ys, xs = np.where(alpha > 0); pad = 8
y0, y1, x0, x1 = ys.min() - pad, ys.max() + pad, xs.min() - pad, xs.max() + pad
n = max(y1 - y0, x1 - x0); cy, cx = (y0 + y1) // 2, (x0 + x1) // 2
big = np.zeros((S + 2 * n, S + 2 * n, 4))
crops = []
for o in out:
    big[:] = 0; big[n:n + S, n:n + S] = o
    crops.append(big[n + cy - n // 2:n + cy - n // 2 + n, n + cx - n // 2:n + cx - n // 2 + n].copy())
for i, img in enumerate(crops):
    Image.fromarray((img * 255).astype(np.uint8), "RGBA").resize((OUT, OUT), Image.LANCZOS).save(f"{prefix}{i:02d}.png")
strip = np.concatenate(crops, 1)
Image.fromarray((strip * 255).astype(np.uint8), "RGBA").resize((OUT * len(crops), OUT), Image.LANCZOS).save(f"{prefix}strip.png")
json.dump({"crop_px": int(n), "S": S}, open(f"{prefix}meta.json", "w"))
