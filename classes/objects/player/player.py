import pygame
import Config
from Config import *
from Images.Animations.Animation import Animation


class Player(pygame.sprite.Sprite):
    class states():
        IDLELEFT = 0
        IDLERIGHT = 1
        RUNLEFT = 2
        RUNRIGHT = 3
        JUMPLEFT = 4
        JUMPRIGHT = 5
        SHOOTLEFT = 6
        SHOOTRIGHT = 7

    Config.WIN

    # constants
    counter = 0
    shootcounter = 0
    jumpcounter = 30

    # images
    idle = pygame.image.load("./Images/SpacemarineAssetPack/Sprites/SpaceMarine/SpriteSheets/94x80/idleSpriteSheet.png").convert_alpha()
    idleleft = Animation(idle, 94, 80, flip=True)
    idleleft.scalefactor = 64
    idleleft.build()
    idleleft = idleleft.animation
    idleright = Animation(idle, 94, 80)
    idleright.scalefactor = 64
    idleright.build()
    idleright = idleright.animation

    run = pygame.image.load(
        "./Images/SpacemarineAssetPack/Sprites/SpaceMarine/SpriteSheets/94x80/runniingSpriteSheet.png").convert_alpha()
    runleft = Animation(run, 94, 80, flip=True)
    runleft.scalefactor = 64
    runleft.build()
    runleft = runleft.animation
    runright = Animation(run, 94, 80)
    runright.scalefactor = 64
    runright.build()
    runright = runright.animation


    animationdic = {
        0: idleleft,
        1: idleright,
        2: runleft,
        3: runright,
    }


    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
        self.grounded = True
        self.jumping = False
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
        elif self.state == self.states.IDLERIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
        elif self.state == self.states.RUNLEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            self.rect.x -= 10
            if self.index == len(self.animation) - 1:
                self.index = 0
        elif self.state == self.states.RUNRIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            self.rect.x += 10
            if self.index == len(self.animation) - 1:
                self.index = 0

        keys = pygame.key.get_pressed()
        if keys[K_a]:
            if self.state != self.states.RUNLEFT:
                self.state = self.states.RUNLEFT
                self.index = 0
        if keys[K_d]:
            if self.state != self.states.RUNRIGHT:
                self.state = self.states.RUNRIGHT
                self.index = 0
        if keys[K_w]:
            if self.grounded:
                self.jumping = True
                self.jumpcounter = 0
        if not keys.__contains__(1):
            if self.facing == "right":
                if self.state != self.states.IDLERIGHT:
                    self.state = self.states.IDLERIGHT
                    self.index = 0
            else:
                if self.state != self.states.IDLELEFT:
                    self.state = self.states.IDLELEFT
                    self.index = 0

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.right >= Config.map.get_width():
            self.rect.right = Config.map.get_width()


        self.grounded = False
        for g in ground_sprites:
            if g.rect.left < self.rect.left < g.rect.right or g.rect.left < self.rect.right < g.rect.right:
                if self.rect.bottom >= g.rect.top:
                    self.rect.bottom = g.rect.top
                    self.grounded = True

        if self.jumping:
            if self.jumpcounter < 10:
                self.rect.y -= (15 - (3*self.jumpcounter))
            else:
                self.jumping = False
            self.jumpcounter += 1
        else:
            self.rect.y += 15

        self.counter += 1
        pygame.draw.rect(Config.map, Config.RED, self.rect, 2)