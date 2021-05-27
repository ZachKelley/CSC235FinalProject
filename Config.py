# Universal variables for all files
import pygame
from pygame import *

from Images.Tiles.ground import ground

pygame.init()
map = Surface((10000, 1500))
map.fill((255, 255, 255))

ground_sprites = pygame.sprite.Group()

maplines = open('map.txt')
maplines = maplines.readline()
maplines = maplines.split(',')


x = 0
y = 0
for m in maplines:
    if m == '1':
        g = ground("top")
        g.rect.x = x
        g.rect.y = y
        ground_sprites.add(g)
    if m == '2':
        g = ground("under")
        g.rect.x = x
        g.rect.y = y
        ground_sprites.add(g)
    x += 100
    if x == 10000:
        x = 0
        y += 50

background = pygame.image.load("./Images/sky.png")
background = pygame.Surface.subsurface(background, (0, 5399, 10000, 1100))
map.blit(background, (0, 0))
cavebackground = pygame.image.load("./Images/cave.png")
cavebackground = pygame.transform.scale(cavebackground, (map.get_width() - 6000,map.get_height() - 300))
map.blit(cavebackground, (6000, map.get_height()/2 + 320))
map.blit(cavebackground, (4800, map.get_height()/2 + 120))
map.blit(cavebackground, (4100, map.get_height()/2 - 20))
map.blit(cavebackground, (0, map.get_height()/5 + 20))
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
player_sprite = pygame.sprite.Group()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
