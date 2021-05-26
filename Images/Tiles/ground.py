import pygame
from pygame import *
class ground(pygame.sprite.Sprite):

    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        if type == "top":
            self.image = pygame.image.load("./groundTILE.png")
        else:
            self.dirt = Surface((100,100))
            self.dirt.fill((139,69,19))
            self.image = self.dirt
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.center = (self.width/2, self.height/2)
