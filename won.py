import pygame
from pygame import *

from classes.menus.main_menu import main_menu

pygame.init()

WIN = pygame.display.set_mode(980, 980)

bg = pygame.image.load("./backgroundSpace.png")


def wonMenu():
    WIN.blit(bg)
    text = font.render("Congratulations you have completed your mission and picked up all "
                       "necessary materials to get you ship into orbit, "
                       "you headed back to the ship and repaired. You and your team started the ship and blasted into "
                       "orbit. "
                       "MISSION SUCCESS", 1, (0, 0, 0))
    WIN.blit(text, (450, 450))
    pygame.display.update()
