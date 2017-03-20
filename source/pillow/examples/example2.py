"""Filtrage, transformation, puis coloration."""

from PIL import Image, ImageFilter

img = Image.open("../../_static/pillow.png")

img = img.filter(ImageFilter.BLUR)
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img = img.transpose(Image.FLIP_LEFT_RIGHT)

width = img.size[0]
height = img.size[1]

white = 250
purple = (155, 89, 182)
blue = (52, 152, 219)

for x in range(width):
    for y in range(height):
        pixel = img.getpixel((x, y))
        # On vérifie que le pixel est blanc
        if all(channel > white for channel in pixel):
            if x + y <= width:
                img.putpixel((x, y), purple)
            else:
                img.putpixel((x, y), blue)

img.show()
