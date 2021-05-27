import pygame
from pygame import *

from classes.menus.main_menu import main_menu

pygame.init()

WIN = pygame.display.set_mode(980, 980)

bg = pygame.image.load("./backgroundSpace.png")


def startMenu():
    WIN.blit(bg)
    text = font.render("A fatal crash occurs with the mother ship leaving you stranded on an unknown planet called "
                       "Aatrox." +
                       "Pieces of the ship are scattered amongst the planet, having you adventure the land and gather "
                       "pieces of the ship to get back into orbit. " +
                       "While looking for pieces to the ship, you are encountered with a bug subspecies called the "
                       "Zerg, they look as if they are multiplying and " +
                       "taking control of the spots to where pieces of the ship remain. Killing the Zerglings are "
                       "needed to even get close to the ship reckages. " +
                       "The queen of the Zerg happens to be nesting around the radioactive power core to your ship.", 1, (0, 0, 0))
    WIN.blit(text, (450, 450))
    pygame.display.update()
