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

    idle = pygame.image.load("./Images/enemies/poison-chomper/idle.png")
    idleleft = Animation(idle, 175, 119)
    idleleft.build()
    idleleft = idleleft.animation
    idleright = Animation(idle, 175, 119, flip=True)
    idleright.build()
    idleright = idleright.animation
    pygame.image.save(idleright[0], "idleright.png")

    jump = pygame.image.load("./Images/enemies/poison-chomper/jump-cycle.png")
    jumpleft = Animation(jump, 304, 246)
    jumpleft.build()
    jumpleft = jumpleft.animation
    jumpright = Animation(jump, 304, 246, flip=True)
    jumpright.build()
    jumpright = jumpright.animation
    pygame.image.save(jumpright[0], "jumpright.png")

    animationdic = {
        0: idleleft,
        1: idleright,
        2: jumpleft,
        3: jumpright,
    }

    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
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
        self.rect.x = Config.WIDTH/2
        self.rect.y = Config.HEIGHT/2
        self.rect.x = 2000
        self.rect.y = Config.HEIGHT / 2

    def update(self):

        if self.counter >= 5:
            self.index += 1
            self.counter = 0

        if self.state == self.states.IDLELEFT:
            self.image = self.animation[self.index]
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.JUMPLEFT
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.IDLERIGHT:
            self.image = self.animation[self.index]
            self.facing = "right"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.JUMPRIGHT
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.JUMPLEFT:
            self.image = self.animation[self.index]
            self.rect.x -= 3
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.IDLERIGHT
                self.animation = self.animationdic[self.state]
        elif self.state == self.states.JUMPRIGHT:
            self.image = self.animation[self.index]
            self.rect.x += 3
            self.facing = "left"
            if self.index == len(self.animation) - 1:
                self.index = 0
                self.state = self.states.IDLELEFT
                self.animation = self.animationdic[self.state]

        if self.rect.bottom >= Config.HEIGHT:
            self.rect.bottom = Config.HEIGHT

        pygame.draw.rect(Config.WIN, Config.RED, self.rect, 2)
        self.counter += 1