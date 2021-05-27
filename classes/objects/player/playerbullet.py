import pygame.sprite

import Config
from Images.Animations.Animation import Animation


class playerbullet(pygame.sprite.Sprite):

    counter = 0

    #animation
    bullet = pygame.image.load("./Images/SpacemarineAssetPack/Bullets/spritesheet/bullet.png")
    bulletleft = Animation(bullet, 33, 36, flip=True)
    bulletleft.scalefactor = 33
    bulletleft.build()
    bulletleft = bulletleft.animation[2:4]
    bulletright = Animation(bullet, 33, 36)
    bulletright.scalefactor = 33
    bulletright.build()
    bulletright = bulletright.animation[2:4]


    def __init__(self, x , y, dir):
        pygame.sprite.Sprite.__init__(self)
        self.dir = dir
        if dir == "left":
            self.animation = self.bulletleft
            self.image = self.animation[0]
        elif dir == "right":
            self.animation = self.bulletright
            self.image = self.animation[0]
        self.vel = 25
        self.index = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.image.get_width()/2, self.image.get_height()/2
        self.rect.x = x - self.rect.width
        self.rect.y = y - self.rect.height
        self.hitmask = pygame.mask.from_surface(self.image)

    def update(self):
        self.image = self.animation[self.index]
        if self.index == len(self.animation) - 1:
            self.index = 0

        if self.counter %2 == 0:
            self.index += 1

        if self.dir == "left":
            self.rect.x -= self.vel
        elif self.dir == "right":
            self.rect.x += self.vel

        self.counter += 1



