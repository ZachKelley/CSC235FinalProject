import pygame
from pygame import *


class ground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        blackcube = Surface((100, 100))
        blackcube.fill((0,0,0))
        self.image = blackcube
        self.rect = blackcube.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.center = (self.width/2, self.height/2)