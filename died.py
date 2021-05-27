import pygame
from pygame import *

from classes.menus.main_menu import main_menu

pygame.init()

WIN = pygame.display.set_mode(980, 980)

bg = pygame.image.load("./backgroundSpace.png")


def diedMenu():
    WIN.blit(bg)
    text = font.render("You have died and did not complete you mission to get back into orbit. Please try again...", 1, (0, 0, 0))
    WIN.blit(text, (450, 450))
    pygame.display.update()
