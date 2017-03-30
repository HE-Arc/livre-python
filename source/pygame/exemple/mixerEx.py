

"""Exemple d'utilisation: lecteur audio."""

import pygame
from pygame.locals import K_RETURN, K_SPACE, KEYDOWN, KEYUP, QUIT, RESIZABLE

pygame.init()
fenetre = pygame.display.set_mode((400, 300))
son = pygame.mixer.Sound("./exemple/Tinquen.wav")

# definition de couleurs
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# definition de texte
myFont = pygame.font.SysFont("monospace", 20)

continuer = 1
joue = 0
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

        # on dessine 2 rectangles, qui nous serviront de boutons
        pygame.draw.rect(fenetre, green, (50, 100, 100, 50))
        pygame.draw.rect(fenetre, red, (250, 100, 100, 50))

        # recuperation de la posision de la souris
        mouse = pygame.mouse.get_pos()

        # si la souris est dans les limites d'un rectangle, il s'illumine.
        if 50 + 100 > mouse[0] > 50 and 100 + 50 > mouse[1] > 100:
            # si on appuie, le son se lance
            if event.type == pygame.MOUSEBUTTONDOWN:
                son.play()
            pygame.draw.rect(fenetre, bright_green, (50, 100, 100, 50))
        else:
            pygame.draw.rect(fenetre, green, (50, 100, 100, 50))

        if 250 + 100 > mouse[0] > 250 and 100 + 50 > mouse[1] > 100:
            if event.type == pygame.MOUSEBUTTONDOWN:
                son.stop()
            pygame.draw.rect(fenetre, bright_red, (250, 100, 100, 50))
        else:
            pygame.draw.rect(fenetre, red, (250, 100, 100, 50))

        # affichage du texte dans le bouton improvisé.
        play = myFont.render("Play!", 1, (0, 0, 0))
        fenetre.blit(play, (75, 100))

        stop = myFont.render("Stop!", 1, (0, 0, 0))
        fenetre.blit(stop, (275, 100))

        pygame.display.update()

pygame.quit()
