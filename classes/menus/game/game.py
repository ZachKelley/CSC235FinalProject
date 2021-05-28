import pygame.sprite

import Config
import died
from Config import *
from classes.objects.enemies.laserflea import laserflea
from classes.objects.enemies.poisonchomper import poisonchomper
from classes.objects.enemies.stonegolem import stonegolem
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

golem1 = stonegolem("left")
golem1.rect.x = 1000
golem1.rect.y = 500

for i in range(3):
    g = stonegolem("left")
    g.rect.x = 1700 + (i*550)
    g.rect.y = 500
    test_sprites.add(g)

g = stonegolem("left")
g.rect.x = 2300
g.rect.y = 900
test_sprites.add(g)

for i in range(4):
    g = stonegolem("left")
    g.rect.x = 5800 + (i * 450)
    g.rect.y = 950
    test_sprites.add(g)

player = Player("right")
player.rect.x = 0
player.rect.y = Config.map.get_height()/6
test_sprites.add(Boss)
test_sprites.add(chompa1)
test_sprites.add(chompa2)
test_sprites.add(chompa3)
test_sprites.add(chompa4)
test_sprites.add(chompa5)
test_sprites.add(chompa6)
test_sprites.add(golem1)

player_sprite.add(player)
Config.map.convert()



def run():
    Config.map = pygame.transform.flip(map, False, False)

    for p in player_sprite:
        p.bullets.draw(Config.map)
        p.bullets.update()
        if p.health <= 0:
            player_sprite.remove(p)
            Config.current_menu = died

    for t in test_sprites:
        if t.dead:
            test_sprites.remove(t)

    player_sprite.draw(Config.map)
    test_sprites.draw(Config.map)

    pygame.display.update()
    test_sprites.update()
    player_sprite.update()
