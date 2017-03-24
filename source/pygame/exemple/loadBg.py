
"""Exemple d'affichage d'une image de fond."""
import pygame
from pygame.locals import *
pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

fond = pygame.image.load("./exemple/background.jpg").convert()
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    fenetre.blit(fond, (0, 0))

    pygame.display.flip()
pygame.quit()
