import pygame.sprite
import Config
from Config import *
from Images.Animations.Animation import Animation


class laserflea(pygame.sprite.Sprite):
    class states():
        IDLELEFT = 0
        IDLERIGHT = 1
        IDLELTOR = 2
        IDLERTOL = 3
        LASERLEFT = 4
        LASERRIGHT = 5
        WALKLEFT = 6
        WALKRIGHT = 7
        WALKLTOR = 8
        WALKRTOL = 9
        DEATH = 10

    Config.WIN

    # constants
    counter = 0
    shootcounter = 0
    walklooper = 0

    # images
    idle = pygame.image.load("./Images/enemies/laser-flea/idle_change_direction.png").convert_alpha()
    idleleft = Animation(idle, 222, 222, flip=True, num=1)
    idleleft.currenty = (idleleft.dy * 2)
    idleleft.scalefactor = 200
    idleleft.build()
    idleleft = idleleft.animation
    idleright = Animation(idle, 222, 222, num=1)
    idleright.currenty = (idleright.dy * 2)
    idleright.scalefactor = 200
    idleright.build()
    idleright = idleright.animation

    idlertol = Animation(idle, 222, 222, flip=True, num=1)
    idlertol.scalefactor = 200
    idlertol.build()
    idlertol = idlertol.animation

    idleltor = Animation(idle, 222, 222, num=1)
    idleltor.scalefactor = 200
    idleltor.build()
    idleltor = idleltor.animation

    walk = pygame.image.load("./Images/enemies/laser-flea/walk_change_direction.png").convert_alpha()
    walkrtol = Animation(walk, 220, 230, num=1)
    walkrtol.scalefactor = 200
    walkrtol.build()
    walkrtol = walkrtol.animation

    walkltor = Animation(walk, 220, 230, flip=True, num=1)
    walkltor.scalefactor = 200
    walkltor.build()
    walkltor = walkltor.animation

    walkleft = walkrtol[10:]
    walkright = walkltor[10:]

    laseratk = pygame.image.load("./Images/enemies/laser-flea/lasser_swept.png").convert_alpha()
    laserleft = Animation(laseratk, 221, 224)
    laserleft.scalefactor = 200
    laserleft.build()
    laserleft = laserleft.animation[0:35]
    laserright = Animation(laseratk, 221, 224, flip=True)
    laserright.scalefactor = 200
    laserright.build()
    laserright = laserright.animation[0:35]

    laser = pygame.image.load("./Images/enemies/laser-flea/laser.png").convert_alpha()
    laser = Animation(laser, 1464, 133, scale=False)
    laser.build()
    laser = laser.animation[5:6]
    laser = laser[0]
    laser = pygame.transform.scale(laser, (laser.get_width(), 50)).convert_alpha()
    i = pygame.Surface((100, 64)).convert_alpha()
    i.fill((0, 0, 0, 0))
    i.blit(laser, (0 - 500, 0))
    laser = i
    laser = pygame.transform.scale(laser, (1500, laser.get_height()))

    animationdic = {
        0: idleleft,
        1: idleright,
        2: idleltor,
        3: idlertol,
        4: laserleft,
        5: laserright,
        6: walkleft,
        7: walkright,
        8: walkltor,
        9: walkrtol,
    }

    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
        if direction == "right":
            self.state = self.states.WALKRIGHT
            self.animation = self.animationdic[self.state]
            self.image = self.animation[0]
            self.facing = "right"
        else:
            self.state = self.states.WALKLEFT
            self.animation = self.animationdic[self.state]
            self.image = self.animation[0]
            self.facing = "left"
        self.index = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = (self.image.get_width()/2, self.image.get_height()/2)
        self.rect.x = map.get_width() - 2000
        self.rect.y = map.get_height() - (map.get_height()/4)
        self.vel = 3
        self.hitmask = pygame.mask.from_surface(self.image)
        self.shot = False

    def update(self):
        self.animation = self.animationdic[self.state]
        self.think()

        if self.state == self.states.LASERLEFT or self.state == self.states.LASERRIGHT:
            if self.counter >= 1:
                self.index += 1
                self.counter = 0
        elif self.state == self.states.IDLELEFT or self.state == self.states.IDLERIGHT or self.state == self.states.IDLELTOR or self.state == self.states.IDLERTOL:
            if self.counter >= 1:
                self.index += 1
                self.counter = 0
        else:
            if self.counter >= 2:
                self.index += 1
                self.counter = 0

        if self.state == self.states.IDLELEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.WALKLEFT
                self.animation = self.animationdic[self.state]
                self.image = self.animation[self.index]
        elif self.state == self.states.IDLERIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.WALKRIGHT
                self.animation = self.animationdic[self.state]
                self.image = self.animation[self.index]
        elif self.state == self.states.IDLELTOR:
            self.image = self.animation[self.index]
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.IDLERIGHT
                self.facing = "right"
                self.animation = self.animationdic[self.state]
                self.image = self.animation[self.index]
        elif self.state == self.states.IDLERTOL:
            self.image = self.animation[self.index]
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.IDLELEFT
                self.facing = "left"
                self.animation = self.animationdic[self.state]
                self.image = self.animation[self.index]
        elif self.state == self.states.WALKLEFT:
            self.image = self.animation[self.index]
            self.rect.x -= self.vel
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
                if self.walklooper > 10:
                    self.walklooper = 0
                    self.state = self.states.WALKLTOR
                    self.animation = self.animationdic[self.state]
                    self.image = self.animation[self.index]
                else:
                    self.walklooper += 1
        elif self.state == self.states.WALKRIGHT:
            self.image = self.animation[self.index]
            self.rect.x += self.vel
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
                if self.walklooper > 10:
                    self.walklooper = 0
                    self.state = self.states.WALKRTOL
                    self.animation = self.animationdic[self.state]
                    self.image = self.animation[self.index]
                else:
                    self.walklooper += 1
        elif self.state == self.states.WALKLTOR:
            self.image = self.animation[self.index]
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.WALKRIGHT
                self.facing = "right"
                self.animation = self.animationdic[self.state]
                self.image = self.animation[self.index]
        elif self.state == self.states.WALKRTOL:
            self.image = self.animation[self.index]
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.WALKLEFT
                self.facing = "left"
                self.animation = self.animationdic[self.state]
                self.image = self.animation[self.index]
        elif self.state == self.states.LASERLEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            if not self.shot:
                if self.index >= len(self.animation) - 8:
                    self.shot = True
                    self.rect.x -= 1500
            if self.index >= len(self.animation) - 8:
                self.shootlaser()
            if self.index == len(self.animation) - 1:
                self.rect.x += 1500
                self.index = 0
                self.state = self.states.IDLELEFT
                self.animation = self.animationdic[self.state]
                self.image = self.animation[self.index]
                self.rect = Rect(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height())
                self.shot = False

        elif self.state == self.states.LASERRIGHT:
            self.facing = "right"
            self.image = self.animation[self.index]
            if self.index >= len(self.animation) - 8:
                self.shootlaser()
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.IDLERIGHT
                self.animation = self.animationdic[self.state]
                self.image = self.animation[self.index]
                self.rect = Rect(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height())

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.right >= Config.map.get_width():
            self.rect.right = Config.map.get_width()

        self.grounded = False
        for g in ground_sprites:
            if self.rect.bottom <= g.rect.top + 15:
                if g.rect.left < self.rect.x < g.rect.right or (g.rect.left < self.rect.right < g.rect.right):
                    if self.rect.bottom >= g.rect.top:
                        self.rect.bottom = g.rect.top
                        self.grounded = True


        self.counter += 1

    def think(self):
        for p in player_sprite:
            if self.state == self.states.WALKLEFT or self.state == self.states.IDLELEFT:
                if self.state != self.states.LASERLEFT:
                    if self.rect.y <= p.rect.top and (self.rect.bottom >= p.rect.bottom):
                        if self.rect.left - WIDTH/2 + 200 <= p.rect.right <= self.rect.left:
                            self.state = self.states.LASERLEFT
                            self.animation = self.animationdic[self.state]
                            self.index = 0
            elif self.state == self.states.WALKRIGHT or self.state == self.states.IDLERIGHT:
                if self.state != self.states.LASERRIGHT:
                    if self.rect.y <= p.rect.top and (self.rect.bottom >= p.rect.bottom):
                        if self.rect.right <= p.rect.left <= self.rect.right + WIDTH/2 - 100:
                            self.state = self.states.LASERRIGHT
                            self.animation = self.animationdic[self.state]
                            self.index = 0

    def shootlaser(self):

        if self.state == self.states.LASERLEFT:
            newimg = Surface(
                ((self.laser.get_width() + self.image.get_width()), self.image.get_height())).convert_alpha()
            newimg.fill((0, 0, 0, 0))
            newimg.blit(self.laser, (30, newimg.get_height()/2 - 25))
            newimg.blit(self.image, (newimg.get_width() - self.image.get_width(), 0))
            self.image = newimg
            self.rect = Rect(self.rect.x , self.rect.y, self.image.get_width(), self.image.get_height())
            self.hitmask = pygame.mask.from_surface(self.image)

        elif self.state == self.states.LASERRIGHT:
            newimg = Surface(
                ((self.laser.get_width() + self.image.get_width()), self.image.get_height())).convert_alpha()
            newimg.fill((0, 0, 0, 0))
            newimg.blit(self.laser, (self.image.get_width() - 30, newimg.get_height()/2 - 25))
            newimg.blit(self.image, (0, 0))
            self.image = newimg
            self.rect = Rect(self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height())
            self.hitmask = pygame.mask.from_surface(self.image)

        for p in player_sprite:
            px = p.rect.x
            py = p.rect.y
            sx = self.rect.x
            sy = self.rect.y

            offset = (px - sx, py - sy)
            result = self.hitmask.overlap(p.hitmask, offset)
            if result:
                print("hit")