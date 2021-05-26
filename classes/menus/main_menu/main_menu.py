import pygame.sprite

import Config
from Config import *
from classes.objects.enemies.laserflea import laserflea
from classes.objects.enemies.poisonchomper import poisonchomper

test = laserflea("right")
test2 = poisonchomper("right")
test_sprites = pygame.sprite.Group()
test_sprites.add(test)
test_sprites.add(test2)


def run():
    Config.updatemap()
    test_sprites.draw(Config.map)
    test_sprites.update()
    for t in test_sprites:
        pygame.display.update(t.rect)
