"""Filtrage, transformation, puis coloration."""

from PIL import Image, ImageFilter

img = Image.open("../../_static/pillow.png")

img = img.filter(ImageFilter.BLUR) \
         .transpose(Image.FLIP_TOP_BOTTOM) \
         .transpose(Image.FLIP_LEFT_RIGHT)

width, height = img.size

WHITE_THRESHOLD = 250
PURPLE = (155, 89, 182)
BLUE = (52, 152, 219)

for x in range(width):
    for y in range(height):
        pixel = img.getpixel((x, y))
        # On vérifie que le pixel est blanc
        if all(channel > WHITE_THRESHOLD for channel in pixel):
            if x + y <= width:
                img.putpixel((x, y), PURPLE)
            else:
                img.putpixel((x, y), BLUE)

img.show()
