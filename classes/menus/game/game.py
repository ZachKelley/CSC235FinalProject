import pygame.sprite

import Config
import died
import won
from Config import *
from classes.objects.enemies.laserflea import laserflea
from classes.objects.enemies.poisonchomper import poisonchomper
from classes.objects.enemies.stonegolem import stonegolem
from classes.objects.objectives.gear import gear
from classes.objects.objectives.reactor import Reactor
from classes.objects.player.player import Player

gears = 0
reactors = 0

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

gear1 = gear()
gear1.rect.x = 2300
gear1.rect.y = 500
gear2 = gear()
gear2.rect.x = 2300
gear2.rect.y = 950
gear3 = gear()
gear3.rect.x = 6000
gear3.rect.y = 1000
gear4 = gear()
gear4.rect.x = 7000
gear4.rect.y = 1000
gear5 = gear()
gear5.rect.x = 2000
gear5.rect.y = 250

reactor = Reactor()
reactor.rect.x = 7750
reactor.rect.y = 1160

objective_sprites.add(gear1)
objective_sprites.add(gear2)
objective_sprites.add(gear3)
objective_sprites.add(gear4)
objective_sprites.add(gear5)
objective_sprites.add(reactor)

font = pygame.font.Font("./OpenSans-Bold.ttf", 16)

def run():
    global gears, reactors
    Config.map = pygame.transform.flip(map, False, False)
    geartxt = font.render("gears: " + repr(gears) + " / 5", True, (255, 255, 255))
    reactortxt = font.render("reactor: " + repr(reactors) + " / 1", True, (255, 255, 255))
    WIN.blit(geartxt, (WIDTH - geartxt.get_width() - 10, 10))
    WIN.blit(reactortxt, (WIDTH - reactortxt.get_width() - 10, 26))

    for p in player_sprite:
        p.bullets.draw(Config.map)
        p.bullets.update()
        if p.health <= 0:
            player_sprite.remove(p)
            Config.current_menu = died

    for t in test_sprites:
        if t.dead:
            test_sprites.remove(t)

    for o in objective_sprites:
        if o.picked:
            objective_sprites.remove(o)
            if isinstance(o, gear):
                gears += 1
            else:
                reactors += 1
    if not objective_sprites:
        Config.current_menu = won

    for l in Config.lasers:
        if l.done:
            Config.lasers.remove(l)

    player_sprite.draw(Config.map)
    test_sprites.draw(Config.map)
    objective_sprites.draw(Config.map)
    lasers.draw(Config.map)

    pygame.display.update()
    test_sprites.update()
    player_sprite.update()
    objective_sprites.update()
    lasers.update()

