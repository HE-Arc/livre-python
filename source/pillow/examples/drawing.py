"""Graphisme 2D avec Pillow."""

from PIL import Image, ImageDraw

width = 160
height = 160
white = (255, 255, 255, 0)

image = Image.new('RGBA', (width, height), white)

# Obtention du contexte graphique
draw = ImageDraw.Draw(image)

green = (0, 255, 0, 0)
draw.line((0, height//2,
          width, height//2),
          fill=green)
draw.line((width//2, 0,
          width//2, height),
          fill=green)

blue = (0, 0, 255, 0)
draw.ellipse((width//4, height//4,
             3*width//4, 3*height//4),
             outline=blue)

black = (0, 0, 0, 0)
draw.text((20, 20), "Cercle trigonométrique", fill=black)

image.show()
image.save("cercleTrigo.png", "png")
