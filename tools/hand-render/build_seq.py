"""Build the sprite frame list from poses.json (open -> pregrasp while turning, then close)."""
import json, sys
names = [f"{f}j{i}" for f in ("ff", "mf", "rf", "th") for i in range(4)]
P = json.load(open('poses.json'))
R = P.get("rot", -60)
lerp = lambda a, b, t: {k: a[k] * (1 - t) + b[k] * t for k in names}
ease = lambda t: t * t * (3 - 2 * t)
frames = [{"rot": [0, 0, 0], "q": P["open"]}]
frames += [{"rot": [R * ease(t), 0, 0], "q": lerp(P["open"], P["pregrasp"], ease(t))} for t in (0.25, 0.5, 0.75, 1.0)]
frames += [{"rot": [R, 0, 0], "q": lerp(P["pregrasp"], P["close"], ease(t))} for t in (0.25, 0.5, 0.75, 1.0)]
json.dump(frames, open(sys.argv[1], 'w'))
