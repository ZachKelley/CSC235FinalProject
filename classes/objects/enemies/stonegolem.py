import pygame.sprite
import Config
from Config import *
from Images.Animations.Animation import Animation
from classes.objects.enemies.golemlaser import golemlaser


class stonegolem(pygame.sprite.Sprite):
    class states():
        IDLELEFT = 0
        IDLERIGHT = 1
        MOVELEFT = 2
        MOVERIGHT = 3
        IMMUNELEFT = 4
        IMMUNERIGHT = 5
        SHOOTLEFT = 6
        SHOOTRIGHT = 7
        DEATHLEFT = 8
        DEATHRIGHT = 9

    Config.WIN

    # images
    spritesheet = pygame.image.load(
        "./Images/enemies/Mecha-stone Golem 0.1/PNG sheet/Character_sheet.png").convert_alpha()
    animationsright = Animation(spritesheet, 100, 100)
    animationsright.build()
    animationsright = animationsright.animation
    animationsleft = Animation(spritesheet, 100, 100, flip=True)
    animationsleft.build()
    animationsleft = animationsleft.animation

    idleright = animationsright[0:4]
    idleleft = animationsleft[0:4]

    immuneright = animationsright[33:38]
    immuneleft = animationsleft[33:38]

    laserright = animationsright[50:57]
    laserleft = animationsleft[50:57]

    deathright = animationsright[80:84]
    deathleft = animationsleft[80:84]

    animationdic = {
        0: idleleft,
        1: idleright,
        2: idleleft,
        3: idleright,
        4: immuneleft,
        5: immuneright,
        6: laserleft,
        7: laserright,
        8: deathleft,
        9: deathright
    }

    counter = 0
    hitcounter = 0
    lasercounter = 0

    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
        self.shooting = False
        self.grounded = True
        self.dead = False
        if direction == "right":
            self.state = self.states.IDLERIGHT
            self.animation = self.animationdic[self.state]
            self.image = self.animation[0]
            self.facing = "right"
        else:
            self.state = self.states.IDLELEFT
            self.animation = self.animationdic[self.state]
            self.image = self.animation[0]
            self.facing = "left"
        self.index = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = (self.width / 2, self.height / 2)
        self.hitmask = pygame.mask.from_surface(self.image)
        self.vel = 5
        self.health = 25

    def update(self):
        self.think()
        self.animation = self.animationdic[self.state]
        self.image = self.animation[self.index]

        if self.counter >= 5:
            self.index += 1
            self.counter = 0

        if self.state == self.states.IDLELEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
        elif self.state == self.states.IDLERIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
        elif self.state == self.states.MOVELEFT:
            if self.state != self.states.SHOOTLEFT:
                self.image = self.animation[self.index]
            self.facing = "left"
            self.rect.x -= self.vel
            if self.index == len(self.animation) - 1:
                self.index = 0
        elif self.state == self.states.MOVERIGHT:
            if self.state != self.states.SHOOTRIGHT:
                self.image = self.animation[self.index]
            self.facing = "right"
            self.rect.x += self.vel
            if self.index == len(self.animation) - 1:
                self.index = 0
        elif self.state == self.states.IMMUNELEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
        elif self.state == self.states.IMMUNERIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
        elif self.state == self.states.SHOOTLEFT:
            self.shooting = True
            self.image = self.animation[self.index]
            self.facing = "left"
            laser = golemlaser(self.rect.x, self.rect.y , "left")
            if self.index == len(self.animation) - 1:
                self.index = 0
                Config.lasers.add(laser)
                self.shooting = False
        elif self.state == self.states.SHOOTRIGHT:
            self.shooting = True
            self.image = self.animation[self.index]
            self.facing = "right"
            laser = golemlaser(self.rect.x + self.rect.width, self.rect.y, "right")
            if self.index == len(self.animation) - 1:
                self.index = 0
                Config.lasers.add(laser)
                self.shooting = False
        elif self.state == self.states.DEATHLEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.dead = True
        elif self.state == self.states.DEATHRIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.dead = True

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.right >= Config.map.get_width():
            self.rect.right = Config.map.get_width()

        self.grounded = False
        for g in Config.ground_sprites:
            if self.rect.bottom <= g.rect.top + 15:
                if g.rect.left < self.rect.x < g.rect.right or (g.rect.left < self.rect.right < g.rect.right):
                    if self.rect.bottom >= g.rect.top:
                        self.rect.bottom = g.rect.top
                        self.grounded = True

            if self.state == self.states.MOVERIGHT:
                if g.rect.top - self.rect.height / 4 <= self.rect.center[1] <= g.rect.bottom + self.rect.height / 4:
                    if self.rect.right >= g.rect.left and (self.rect.right <= g.rect.left + 15):
                        self.rect.right = g.rect.left
                        self.vel = 0
                        self.rect.y -= 15
                elif g.rect.top < self.rect.bottom:
                    self.vel = 5

            if self.state == self.states.MOVELEFT:
                if g.rect.top - self.rect.height / 4 <= self.rect.center[1] <= g.rect.bottom + self.rect.height / 4:
                    if g.rect.right >= self.rect.left and (self.rect.left >= g.rect.left - 15):
                        self.rect.left = g.rect.right
                        self.vel = 0
                        self.rect.y -= 15
                elif g.rect.top < self.rect.bottom:
                    self.vel = 5

        if not self.grounded:
            self.rect.y += 10

        for p in player_sprite:
            for b in p.bullets:
                bx = b.rect.x
                by = b.rect.y
                sx = self.rect.x
                sy = self.rect.y

                offset = (bx - sx, by - sy)
                result = self.hitmask.overlap(b.hitmask, offset)
                if result:
                    p.bullets.remove(b)
                    if self.health > 0:
                        if self.state != self.states.IMMUNERIGHT and self.state != self.states.IMMUNELEFT:
                            if self.state != self.states.SHOOTLEFT and self.state != self.states.SHOOTRIGHT:
                                self.health -= 5
        if self.health <= 0:
            if self.state != self.states.DEATHLEFT and self.state != self.states.DEATHRIGHT:
                if self.facing == "left":
                    self.state = self.states.DEATHLEFT
                    self.index = 0
                else:
                    self.state = self.states.DEATHRIGHT
                    self.index = 0

        self.hitcounter += 1
        self.counter += 1


        pygame.draw.line(Config.map, Config.RED, (self.rect.x, self.rect.y - 10), (self.rect.right, self.rect.y - 10),
                         4)
        pygame.draw.line(Config.map, Config.GREEN, (self.rect.x, self.rect.y - 10),
                         (self.rect.x + ((self.health / 25) * self.rect.width), self.rect.y - 10), 4)

    def think(self):
        if not self.shooting:
            if self.state != self.states.DEATHRIGHT and self.state != self.states.DEATHLEFT:
                for p in player_sprite:
                    if self.rect.x - 50 <= p.rect.right <= self.rect.x:
                        self.state = self.states.SHOOTLEFT
                        self.index = 0

                    elif self.rect.right <= p.rect.x <= self.rect.right + 50:
                        self.state = self.states.SHOOTRIGHT
                        self.index = 0

                    elif self.rect.x - 2000 <= p.rect.x <= self.rect.x - 150:
                        if p.facing == "left":
                            if self.rect.x - 300 <= p.rect.x <= self.rect.x - p.rect.width:
                                self.state = self.states.MOVELEFT
                                self.index = 0
                        elif p.facing == "right":
                            self.state = self.states.IMMUNELEFT
                            self.index = 0
                    elif self.rect.right + 50 <= p.rect.x <= self.rect.right + 2000:
                        if p.facing == "right":
                            if self.rect.right <= p.rect.x <= self.rect.right + 300 + p.rect.width:
                                self.state = self.states.MOVERIGHT
                                self.index = 0
                        elif p.facing == "left":
                            self.state = self.states.IMMUNERIGHT
                            self.index = 0
