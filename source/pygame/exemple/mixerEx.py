"""Exemple d'utilisation des modules pygame.event et pygame.mixer."""
import pygame
from pygame.locals import K_RETURN, K_SPACE, KEYDOWN, KEYUP, QUIT, RESIZABLE

pygame.init()
fenetre = pygame.display.set_mode((200, 200), RESIZABLE)
son = pygame.mixer.Sound("./exemple/Tinquen.wav")

continuer = True
joue = False
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not joue:
                    son.play()
                    joue = True
                else:
                    pygame.mixer.unpause()
            elif event.key == K_RETURN:
                son.stop()
                joue = False
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                pygame.mixer.pause()

pygame.quit()
