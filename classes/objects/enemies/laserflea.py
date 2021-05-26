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
    laser = pygame.transform.scale(laser, (laser.get_width(), 30)).convert_alpha()
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
        self.rect.x = Config.WIDTH/2
        self.rect.y = Config.HEIGHT/2

    def update(self):
        self.animation = self.animationdic[self.state]

        if self.counter >= 2:
            self.index += 1
            self.counter = 0

        if self.state == self.states.IDLELEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.IDLELTOR
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.IDLERIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.IDLERTOL
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.IDLELTOR:
            self.image = self.animation[self.index]
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.IDLERIGHT
                self.facing = "right"
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.IDLERTOL:
            self.image = self.animation[self.index]
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.IDLELEFT
                self.facing = "left"
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.WALKLEFT:
            self.image = self.animation[self.index]
            self.rect.x -= 3
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.WALKLTOR
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.WALKRIGHT:
            self.image = self.animation[self.index]
            self.rect.x += 3
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.WALKRTOL
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.WALKLTOR:
            self.image = self.animation[self.index]
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.WALKRIGHT
                self.facing = "right"
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.WALKRTOL:
            self.image = self.animation[self.index]
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.WALKLEFT
                self.facing = "left"
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.LASERLEFT:
            self.image = self.animation[self.index]
            if self.index >= len(self.animation) - 8:
                self.shootlaser("left")
            if self.index == len(self.animation) - 1:
                self.index = 0
        elif self.state == self.states.LASERRIGHT:
            self.image = self.animation[self.index]
            if self.index >= len(self.animation) - 8:
                self.shootlaser("right")
            if self.index == len(self.animation) - 1:
                self.index = 0

        if self.rect.bottom >= Config.HEIGHT:
            self.rect.bottom = Config.HEIGHT


        pygame.draw.rect(Config.WIN, Config.RED, self.rect, 2)
        self.counter += 1

    def shootlaser(self, dir):

        if dir == "left":
            newimg = Surface(
                ((self.laser.get_width() + self.image.get_width()), self.image.get_height())).convert_alpha()
            newimg.fill((0, 0, 0, 0))
            newimg.blit(self.laser, (10, 15))
            newimg.blit(self.image, (newimg.get_width() - self.image.get_width(), 0))
            self.rect.right = self.rect.x + 200
            self.image = newimg
        else:
            newimg = Surface(
                ((self.laser.get_width() + self.image.get_width()), self.image.get_height())).convert_alpha()
            newimg.fill((0, 0, 0, 0))
            newimg.blit(self.laser, (self.image.get_width() - 10, 15))
            newimg.blit(self.image, (0, 0))
            self.image = newimg
