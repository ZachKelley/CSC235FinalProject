import pygame.sprite

import Config
from Config import *
from classes.objects.enemies.laserflea import laserflea
from classes.objects.enemies.poisonchomper import poisonchomper
from classes.objects.player.player import Player

Boss = laserflea("right")
chompa1 = poisonchomper("right")
chompa2 = poisonchomper("left")
chompa2.rect.x = chompa2.rect.x + 1200
chompa3 = poisonchomper("left")
chompa3.rect.x = chompa2.rect.x + 100
chompa4 = poisonchomper("left")
chompa4.rect.x = chompa2.rect.x + 200
chompa5 = poisonchomper("right")
chompa5.rect.x = chompa1.rect.x - 100
chompa6 = poisonchomper("right")
chompa6.rect.x = chompa1.rect.x - 200

player = Player("right")
player.rect.x = 0
player.rect.y = Config.map.get_height()/6
test_sprites = pygame.sprite.Group()
test_sprites.add(Boss)
test_sprites.add(chompa1)
test_sprites.add(chompa2)
test_sprites.add(chompa3)
test_sprites.add(chompa4)
test_sprites.add(chompa5)
test_sprites.add(chompa6)
player_sprite.add(player)
Config.map.convert()


def run():
    Config.map = pygame.transform.flip(map, False, False)
    for t in test_sprites:
        pygame.display.update(t.rect)
        if t.health <= 0:
            test_sprites.remove(t)
    for p in player_sprite:
        p.bullets.draw(Config.map)
        p.bullets.update()
        if p.health <= 0:
            player_sprite.remove(p)
        for b in p.bullets:
            pygame.display.update(b.rect)
        pygame.display.update(p.rect)
    test_sprites.draw(Config.map)
    test_sprites.update()
    player_sprite.draw(Config.map)
    player_sprite.update()
