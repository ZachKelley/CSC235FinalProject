import pygame.sprite

import Config
from Config import *
from classes.objects.enemies.laserflea import laserflea

test = laserflea("right")
test_sprites = pygame.sprite.Group()
test_sprites.add(test)


def run():
    Config.updatemap()
    test_sprites.draw(Config.map)
    test_sprites.update()
    for t in test_sprites:
        pygame.display.update(t.rect)
