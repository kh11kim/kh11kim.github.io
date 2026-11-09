import sys
from PIL import Image
pre, out = sys.argv[1], sys.argv[2]
fr = [Image.open(f'{pre}{i:02d}.png') for i in range(9)]
s = Image.new('RGBA', (220 * 9, 220))
for i, f in enumerate(fr): s.paste(f, (220 * i, 0))
s.save(out, optimize=True)
