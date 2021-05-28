import pygame.sprite
import Config
from Config import *
from Images.Animations.Animation import Animation


class poisonchomper(pygame.sprite.Sprite):

    class states():
        IDLELEFT = 0
        IDLERIGHT = 1
        JUMPLEFT = 2
        JUMPRIGHT = 3
        BITELEFT = 4
        BITERIGHT = 5
        SPITLEFT = 6
        SPITRIGHT = 7

    Config.WIN

    # constants
    counter = 0
    shootcounter = 0

    idle = pygame.image.load("./Images/enemies/poison-chomper/idle.png").convert_alpha()
    idleleft = Animation(idle, 175, 119)
    idleleft.scalefactor = 32
    idleleft.build()
    idleleft = idleleft.animation
    idleright = Animation(idle, 175, 119, flip=True)
    idleright.scalefactor = 32
    idleright.build()
    idleright = idleright.animation


    jump = pygame.image.load("./Images/enemies/poison-chomper/jump-cycle.png").convert_alpha()
    jumpleft = Animation(jump, 304, 246, num=1)
    jumpleft.build()
    jumpleft = jumpleft.animation
    jumpright = Animation(jump, 304, 246, flip=True, num=1)
    jumpright.build()
    jumpright = jumpright.animation


    animationdic = {
        0: idleleft,
        1: idleright,
        2: jumpleft,
        3: jumpright,
    }

    jumploop = 0
    hitcounter = 0

    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
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
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.width / 2, self.rect.height / 2)
        self.rect.x = Config.WIDTH/2
        self.rect.y = Config.HEIGHT/5
        self.hitmask = pygame.mask.from_surface(self.image)
        self.health = 50

    def update(self):
        self.hitmask = pygame.mask.from_surface(self.image)

        if self.counter >= 1:
            self.index += 1
            self.counter = 0

        if self.state == self.states.IDLELEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.JUMPLEFT
                self.animation = self.animationdic[self.state]
                self.rect.y -= 32
        elif self.state == self.states.IDLERIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.JUMPRIGHT
                self.animation = self.animationdic[self.state]
                self.rect.y -= 32
        elif self.state == self.states.JUMPLEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            if self.jumploop < 10:
                self.rect.x -= 10
                self.rect.y -= 5
                if self.index == len(self.animation) - 1:
                    self.index = 0
                    self.jumploop += 1
            else:
                self.index = 0
                self.state = self.states.IDLERIGHT
                self.animation = self.animationdic[self.state]
                self.rect.y += 32
                self.jumploop = 0

        elif self.state == self.states.JUMPRIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            if self.jumploop < 10:
                self.rect.x += 10
                self.rect.y -= 5
                if self.index == len(self.animation) - 1:
                    self.index = 0
                    self.jumploop += 1
            else:
                if self.index == len(self.animation) - 1:
                    self.index = 0
                    self.state = self.states.IDLELEFT
                    self.animation = self.animationdic[self.state]
                    self.jumploop = 0

        self.grounded = False
        for g in ground_sprites:
            if self.rect.bottom <= g.rect.top + 10:
                if g.rect.left < self.rect.x < g.rect.right or (g.rect.left < self.rect.right < g.rect.right):
                    if self.rect.bottom >= g.rect.top:
                        if self.state != self.states.JUMPLEFT or self.state != self.states.JUMPRIGHT:
                            self.rect.bottom = g.rect.top
                            self.grounded = True
        if not self.grounded:
            self.rect.y += 5

        for p in player_sprite:
            px = p.rect.x
            py = p.rect.y
            sx = self.rect.x
            sy = self.rect.y

            offset = (px - sx, py - sy)
            result = self.hitmask.overlap(p.hitmask, offset)
            if result:
                if self.hitcounter > 10:
                    if p.health > 0:
                        p.damage(1)
                    self.hitcounter = 0
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
                        self.health -= 5

        pygame.draw.line(Config.map, Config.RED, (self.rect.x, self.rect.y - 10), (self.rect.right, self.rect.y - 10),
                         4)
        pygame.draw.line(Config.map, Config.GREEN, (self.rect.x, self.rect.y - 10),
                         (self.rect.x + ((self.health / 50) * self.rect.width), self.rect.y - 10), 4)

        if self.health <= 0:
            self.dead = True


        self.counter += 1
        self.hitcounter += 1