#Universal variables for all files
import pygame
from pygame import *

WIDTH, HEIGHT = 1920, 1080
flags = FULLSCREEN | DOUBLEBUF | SCALED
WIN = pygame.display.set_mode((WIDTH,HEIGHT), flags, 16)
pygame.display.set_caption("Eduardo's Journey")

current_menu = None


#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)