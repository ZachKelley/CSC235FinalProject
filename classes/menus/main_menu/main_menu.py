import pygame.sprite

import Config
from Config import *
from classes.objects.enemies.laserflea import laserflea
from classes.objects.enemies.poisonchomper import poisonchomper
from classes.objects.player.player import Player

test = laserflea("right")
test2 = poisonchomper("right")
player = Player("right")
player.rect.x = 0
player.rect.y = Config.map.get_height()/2 - 100
test_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
test_sprites.add(test)
test_sprites.add(test2)
player_sprite.add(player)


def run():
    Config.updatemap()
    test_sprites.draw(Config.map)
    test_sprites.update()
    player_sprite.draw(Config.map)
    player_sprite.update()
    for t in test_sprites:
        pygame.display.update(t.rect)
    for p in player_sprite:
        pygame.display.update(p.rect)
