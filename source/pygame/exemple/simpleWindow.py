
"""Exemple d'affichage d'une fenêtre simple."""
import pygame
from pygame.locals import *

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption('Basic Pygame program')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

# Display some text
font = pygame.font.Font(None, 36)
text = font.render("Hello There", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

# Event loop
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    screen.blit(background, (0, 0))
    pygame.display.flip()
