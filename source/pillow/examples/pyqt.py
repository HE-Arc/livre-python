"""Manipulation d'une image graphiquement à l'aide de PyQt."""

import sys

from PIL import Image, ImageFilter, ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                             QVBoxLayout, QWidget)


class Viewer(QWidget):
    """Affiche une image avec trois boutons pour la pivoter/flouter."""

    def __init__(self):
        """Initialisation des composants, connexion signaux/slots."""
        super().__init__()

        self.blurButton = QPushButton("Blur")
        self.rotateLeftButton = QPushButton("Rotate Left")
        self.rotateRightButton = QPushButton("Rotate Right")

        self.label = QLabel()
        self.image = Image.open("../../_static/pillow.png")

        self.initUI()
        self.displayImage()

        self.blurButton.clicked.connect(self.blurImage)
        self.rotateLeftButton.clicked.connect(self.turnLeft)
        self.rotateRightButton.clicked.connect(self.turnRight)

    def displayImage(self):
        """PIL Image -> QImage -> QPixmap.

        Convertit une image de la bibliothèque PIL en QImage. Convertit
        l'objet QImage en QPixmap puis affiche le résultat dans un label.
        """
        self.label.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.image)))

    def turnLeft(self):
        """Tourne l'image à gauche à l'aide de PIL puis affiche le résultat."""
        self.image = self.image.rotate(90)
        self.displayImage()

    def turnRight(self):
        """Tourne l'image à droite à l'aide de PIL puis affiche le résultat."""
        self.image = self.image.rotate(-90)
        self.displayImage()

    def blurImage(self):
        """Floute l'image à l'aide de PIL puis affiche le résultat."""
        self.image = self.image.filter(ImageFilter.BLUR)
        self.displayImage()

    def initUI(self):
        """Dispose les composants dans des layouts."""
        hboxLabel = QHBoxLayout()
        hboxLabel.addStretch(1)
        hboxLabel.addWidget(self.label)
        hboxLabel.addStretch(1)

        hboxButtons = QHBoxLayout()
        hboxButtons.addStretch(1)
        hboxButtons.addWidget(self.blurButton)
        hboxButtons.addStretch(1)
        hboxButtons.addWidget(self.rotateLeftButton)
        hboxButtons.addStretch(1)
        hboxButtons.addWidget(self.rotateRightButton)
        hboxButtons.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hboxLabel)
        vbox.addStretch(1)
        vbox.addLayout(hboxButtons)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    viewer = Viewer()
    viewer.resize(450, 400)
    viewer.setWindowTitle('Image Viewer')
    viewer.show()

    sys.exit(app.exec_())
