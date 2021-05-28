import pygame.sprite

import Config
from Config import *
from Images.Animations.Animation import Animation


class golemlaser(pygame.sprite.Sprite):

    counter = 0
    damagecounter = 0

    #animation
    laser = pygame.image.load("./Images/enemies/Mecha-stone Golem 0.1/weapon PNG/Laser_sheet.png")
    laserleft = Animation(laser, 300, 100, flip=True)
    laserleft.build()
    laserleft = laserleft.animation
    laserright = Animation(laser, 300, 100)
    laserright.scalefactor = 33
    laserright.build()
    laserright = laserright.animation


    def __init__(self, x , y, dir):
        pygame.sprite.Sprite.__init__(self)
        self.done = False
        self.dir = dir
        if dir == "left":
            self.image = self.laserleft[9]
        elif dir == "right":
            self.image = self.laserright[9]

        self.rect = self.image.get_rect()
        self.rect.center = (self.image.get_width()/2, self.image.get_height()/2)
        if dir == "left":
            self.rect.x = x - self.rect.width + 30
        else:
            self.rect.x = x
        self.rect.y = y
        self.hitmask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.counter > 10:
            self.done = True

        for p in player_sprite:
            px = p.rect.x
            py = p.rect.y
            sx = self.rect.x
            sy = self.rect.y

            offset = (px - sx, py - sy)
            result = self.hitmask.overlap(p.hitmask, offset)
            if result:
                if p.health > 0:
                    if self.damagecounter > 7:
                        self.damagecounter = 0
                        p.damage(3)
        self.counter += 1
        self.damagecounter += 1


