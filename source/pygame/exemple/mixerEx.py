
"""Exemple d'utilisation des modules pygame.event et pygame.mixer."""
import pygame
from pygame.locals import *
pygame.init()
fenetre = pygame.display.set_mode((200, 200), RESIZABLE)
son = pygame.mixer.Sound("./exemple/Tinquen.wav")

continuer = 1
joue = 0
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN and event.key == K_SPACE and joue == 0:
            son.play()
            joue = 1
        if event.type == KEYDOWN and event.key == K_SPACE and joue == 1:
            pygame.mixer.unpause()
        if event.type == KEYUP and event.key == K_SPACE:
            pygame.mixer.pause()
        if event.type == KEYDOWN and event.key == K_RETURN:
            son.stop()
            joue = 0
pygame.quit()
