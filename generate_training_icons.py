from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parent
app_dir = root / 'appPackage'
app_dir.mkdir(exist_ok=True)

# Create outline icon: 32x32, transparent background, white training symbol
outline = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
draw = ImageDraw.Draw(outline)
# Rounded square border
for i in range(2):
    draw.rounded_rectangle((1 + i, 1 + i, 30 - i, 30 - i), radius=5, outline=(255, 255, 255, 255), width=1)
# Training/learning symbol: book and spark
# book body
book_left = 7
book_top = 8
book_right = 25
book_bottom = 24
draw.rounded_rectangle((book_left, book_top, book_right, book_bottom), radius=2, outline=(255, 255, 255, 255), width=1)
draw.line((book_left + 3, book_top + 5, book_right - 3, book_top + 5), fill=(255, 255, 255, 255), width=1)
draw.line((book_left + 3, book_top + 10, book_right - 3, book_top + 10), fill=(255, 255, 255, 255), width=1)
draw.line((book_left + 3, book_top + 15, book_right - 3, book_top + 15), fill=(255, 255, 255, 255), width=1)
draw.polygon([(24, 7), (29, 6), (27, 11), (24, 10)], fill=(255, 255, 255, 255))
outline.save(app_dir / 'outline.png')

# Create color icon: 192x192, orange gradient, training motif
color = Image.new('RGBA', (192, 192), (0, 0, 0, 0))
# background orange gradient
for y in range(192):
    for x in range(192):
        # soft orange to darker orange
        r = int(255 - (x / 192) * 20)
        g = int(140 + (y / 192) * 30)
        b = int(40 + (x / 192) * 15)
        a = 255
        color.putpixel((x, y), (r, g, b, a))

draw = ImageDraw.Draw(color)
# rounded container
for i in range(5):
    draw.rounded_rectangle((18 + i, 18 + i, 174 - i, 174 - i), radius=28, outline=(255, 255, 255, 255), width=2)
# training book icon
book_left = 56
book_top = 58
book_right = 136
book_bottom = 136
draw.rounded_rectangle((book_left, book_top, book_right, book_bottom), radius=10, fill=(255, 255, 255, 255), outline=(255, 140, 0, 255), width=3)
draw.line((book_left + 18, book_top + 24, book_right - 18, book_top + 24), fill=(255, 140, 0, 255), width=5)
draw.line((book_left + 18, book_top + 42, book_right - 18, book_top + 42), fill=(255, 140, 0, 255), width=5)
draw.line((book_left + 18, book_top + 60, book_right - 18, book_top + 60), fill=(255, 140, 0, 255), width=5)
# spark accent
for pts in [((142, 58), (156, 42), (150, 58), (166, 66)), ((150, 74), (162, 72), (154, 82), (166, 86))]:
    draw.polygon(pts, fill=(255, 220, 180, 255))
color.save(app_dir / 'color.png')

print('Updated icons:')
print(app_dir / 'outline.png')
print(app_dir / 'color.png')
