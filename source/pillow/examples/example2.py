"""Filtrage, transformation, puis coloration."""

from PIL import Image, ImageFilter

img = Image.open("../../_static/pillow.png")

img = img.filter(ImageFilter.BLUR)
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img = img.transpose(Image.FLIP_LEFT_RIGHT)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if img.getpixel((x,y))[0] > 250 and img.getpixel((x,y))[1] > 250 and img.getpixel((x,y))[2] > 250:
            if x + y <= img.size[0]:
                img.putpixel((x,y), (155, 89, 182))
            else:
                img.putpixel((x,y), (52, 152, 219))

img.show()
