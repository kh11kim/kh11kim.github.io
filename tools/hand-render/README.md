# Hand animation renderer

Renders the cartoon Allegro Hand sprite (`images/allegro-grasp.webp`) shown next to the name.

The hand model is the Wonik Allegro Hand from [MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie/tree/main/wonik_allegro) (BSD-2-Clause).

## Files
- `poses.json`: joint angles for the open hand, pregrasp, and close poses, plus the wrist rotation (`rot`, degrees).
- `style.json`: toon palette, outline widths, render size.
- `build_seq.py`: builds the 9-frame list (0 wave, 1-4 turn + preshape, 5-8 close) from `poses.json`.
- `render_seq.py`: renders frames with MuJoCo and applies flat toon shading with outlines, using a shared crop.
- `make_sprite.py`: packs the frames into one horizontal sprite.

## Usage
```sh
git clone --depth 1 --filter=blob:none --sparse https://github.com/google-deepmind/mujoco_menagerie.git /tmp/menagerie
git -C /tmp/menagerie sparse-checkout set wonik_allegro
uv venv .venv && uv pip install mujoco pillow numpy scipy

cd tools/hand-render && mkdir -p out
../../.venv/bin/python build_seq.py frames.json
../../.venv/bin/python render_seq.py /tmp/menagerie/wonik_allegro/right_hand.xml out/f frames.json style.json
../../.venv/bin/python make_sprite.py out/f sprite.png
cwebp -q 90 -alpha_q 100 sprite.png -o ../../images/allegro-grasp.webp
```

If the close pose changes, re-measure the grasp aperture in the last frame and update `GRASP` in `index.html`.
