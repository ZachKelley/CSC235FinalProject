import sys

import pygame
from pygame.mixer import Sound
import Config
from Config import *

pygame.init()
pygame.font.init()

death = Sound("./Sounds/deathsound.mp3")

bg = pygame.image.load("./backgroundSpace.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

def run():
    death.play()

    WIN.blit(bg, (0,0))
    font = pygame.font.Font("./OpenSans-Bold.ttf", 36)
    text = font.render("You have died and did not complete you mission to get back into orbit. Please try again...", True, (255,255,255))
    WIN.blit(text, (200, 450))

    startfont = pygame.font.Font("./OpenSans-Bold.ttf", 72)
    start = startfont.render("press any button to QUIT", True, (255, 255, 255))

    WIN.blit(start, (WIDTH / 2 - start.get_width() / 2, HEIGHT / 2 - start.get_height() / 2))

    keys = pygame.key.get_pressed()
    if keys.__contains__(1):
        pygame.quit()
        sys.exit()

    pygame.display.update()
