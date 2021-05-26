import pygame.sprite

import Config
from Config import *
from classes.objects.enemies.laserflea import laserflea

test = laserflea("right")
test_sprites = pygame.sprite.Group()
test_sprites.add(test)

def run():
    Config.WIN.fill(Config.WHITE)

    test_sprites.draw(Config.WIN)
    test_sprites.update()
    pygame.display.update()
