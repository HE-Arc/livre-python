"""Inversion des bandes (r, b, g) d'une image."""

from PIL import Image

image = Image.open("../../_static/pillow.png")

r, g, b, a = image.split()

image = Image.merge("RGBA", (b, r, g, a))

image.show()
