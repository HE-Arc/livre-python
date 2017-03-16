"""Graphisme 2D avec Pillow"""

from PIL import Image, ImageDraw

image = Image.new('RGBA', (160, 160), (255,255,255,0))
draw = ImageDraw.Draw(image)

draw.line((0, image.size[1]/2,
           image.size[0], image.size[1]/2),
           fill=(0,255,0))
draw.line((image.size[0]/2, 0,
           image.size[0]/2, image.size[1]),
           fill=(0,255,0))

draw.ellipse((image.size[0]/4, image.size[1]/4,
              3*image.size[0]/4, 3*image.size[1]/4),
              outline=(0,0,255))

draw.text((20, 20), "Cercle trigonométrique", fill=(0,0,0))

del draw

image.show();
image.save("cercleTrigo.png", "png")
