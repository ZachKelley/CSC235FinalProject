# Universal variables for all files
import pygame
from pygame import *

from Images.Tiles.ground import ground

pygame.init()
map = Surface((10000,1500))
map.fill((255, 255, 255))

ground_sprites = pygame.sprite.Group()

maplines = open('map')
maplines = maplines.read()
x = 0
y = 0
for m in maplines:
    if m == 'g':
        g = ground("top")
        g.rect.x = x
        g.rect.y = y
        ground_sprites.add(g)
    if m == 'u':
        g = ground("under")
        g.rect.x = x
        g.rect.y = y
        ground_sprites.add(g)
    x += 100
    if m == '\n':
        x = 0
        y += 100

ground_sprites.draw(map)
pygame.image.save(map, "map1.png")

WIDTH, HEIGHT = 1920, 1080
flags = FULLSCREEN | DOUBLEBUF | SCALED
WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags, 16)
x = 0
y = 0

pygame.display.set_caption("Eduardo's Journey")
FPS = 60
clock = pygame.time.Clock()

current_menu = None

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
