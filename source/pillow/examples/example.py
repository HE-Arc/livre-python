from PIL import Image

"""Exemple simple de manipulation d'images."""

image = Image.open("../../_static/pillow.png")
image = image.convert('L')
image.show()
image.save('gray-pillow.jpeg', 'jpeg')
