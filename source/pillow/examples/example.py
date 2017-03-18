"""Exemple simple de manipulation d'images."""

from PIL import Image

image = Image.open("../../_static/pillow.png")
image = image.convert('L')

image.show()
image.save('gray-pillow.jpeg', 'jpeg')
