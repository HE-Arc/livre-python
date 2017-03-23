"""Graphisme 2D avec Pillow."""

from PIL import Image, ImageDraw

width = 160
height = 160

WHITE = (255, 255, 255, 0)

image = Image.new('RGBA', (width, height), WHITE)

# Obtention du contexte graphique
draw = ImageDraw.Draw(image)

GREEN = (0, 255, 0, 0)
draw.line((0, height//2,
          width, height//2),
          fill=GREEN)
draw.line((width//2, 0,
          width//2, height),
          fill=GREEN)

BLUE = (0, 0, 255, 0)
draw.ellipse((width//4, height//4,
             3*width//4, 3*height//4),
             outline=BLUE)

BLACK = (0, 0, 0, 0)
draw.text((20, 20), "Cercle trigonométrique", fill=BLACK)

image.show()
image.save("cercleTrigo.png", "png")
