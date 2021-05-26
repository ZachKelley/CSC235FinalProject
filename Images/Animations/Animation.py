import pygame

import Config


class Animation():

    Config.WIN

    def __init__(self, image, dx, dy, flip=False, num=0, scale=True):
        self.animation = []
        self.flip = flip
        self.image = image
        self.currentx = 0
        self.currenty = 0
        self.dx = dx
        self.dy = dy
        self.num = num
        self.scale = scale
        self.scalefactor = 64

    def build(self):
        while self.currenty != self.image.get_height():
            if self.currenty == self.image.get_height() - self.dy:
                i = pygame.Surface.subsurface(self.image, (
                    self.currentx, self.currenty, self.dx, self.dy)).convert_alpha()
                if self.flip:
                    i = pygame.transform.flip(i, True, False)
                if self.scale:
                    i = pygame.transform.scale(i, (self.scalefactor, self.scalefactor))
                self.animation.append(i)
                if self.currentx == self.image.get_width() - (self.dx * (self.num + 1)):
                    self.currentx = 0
                    self.currenty += self.dy
                self.currentx += self.dx
            else:
                i = pygame.Surface.subsurface(self.image, (
                    self.currentx, self.currenty, self.dx, self.dy)).convert_alpha()
                if self.flip:
                    i = pygame.transform.flip(i, True, False)
                if self.scale:
                    i = pygame.transform.scale(i, (self.scalefactor, self.scalefactor))
                self.animation.append(i)
                self.currentx += self.dx
                if self.currentx == self.image.get_width():
                    self.currentx = 0
                    self.currenty += self.dy
