import pygame.sprite

import Config
from Config import *


class gear(pygame.sprite.Sprite):
    Config.WIN

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./Images/cogwheel.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (32,32))
        self.rect = self.image.get_rect()
        self.rect.center = self.image.get_width()/2, self.image.get_height()/2
        self.picked = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            for p in player_sprite:
                if self.rect.x - 50 <= p.rect.x <= self.rect.x + self.rect.width + 50:
                    if self.rect.y - 50 <= p.rect.center[1] <= self.rect.y + self.rect.height + 50:
                        self.picked = True