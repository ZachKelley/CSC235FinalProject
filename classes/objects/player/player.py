import pygame
import Config
import died
from Config import *
from Images.Animations.Animation import Animation
from classes.objects.player.playerbullet import playerbullet


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
    idle = pygame.image.load(
        "./Images/SpacemarineAssetPack/Sprites/SpaceMarine/SpriteSheets/94x80/idleSpriteSheet.png").convert_alpha()
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

    shoot = pygame.image.load(
        "./Images/SpacemarineAssetPack/Sprites/SpaceMarine/SpriteSheets/94x80/ShootingSpriteSheet.png").convert_alpha()
    shootleft = Animation(shoot, 94, 80, flip=True)
    shootleft.scalefactor = 64
    shootleft.build()
    shootleft = shootleft.animation
    shootright = Animation(shoot, 94, 80)
    shootright.scalefactor = 64
    shootright.build()
    shootright = shootright.animation

    animationdic = {
        0: idleleft,
        1: idleright,
        2: runleft,
        3: runright,
        6: shootleft,
        7: shootright
    }

    bullets = pygame.sprite.Group()

    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
        self.grounded = True
        self.jumping = False
        self.shooting = False
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
        self.hitmask = pygame.mask.from_surface(self.image)
        self.vel = 10
        self.health = 10

    def update(self):
        if self.health > 0:
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
                if self.state != self.states.SHOOTLEFT:
                    self.image = self.animation[self.index]
                self.facing = "left"
                self.rect.x -= self.vel
                if self.index == len(self.animation) - 1:
                    self.index = 0
            elif self.state == self.states.RUNRIGHT:
                if self.state != self.states.SHOOTRIGHT:
                    self.image = self.animation[self.index]
                self.facing = "right"
                self.rect.x += self.vel
                if self.index == len(self.animation) - 1:
                    self.index = 0

            elif self.state == self.states.SHOOTLEFT:
                self.image = self.animation[self.index]
                self.facing = "left"
                if self.index == len(self.animation) - 1:
                    b = playerbullet(self.rect.left, self.rect.center[1], "left")
                    self.bullets.add(b)
                    self.index = 0
                    self.state = self.states.IDLELEFT

            elif self.state == self.states.SHOOTRIGHT:
                self.image = self.animation[self.index]
                self.facing = "right"
                if self.index == len(self.animation) - 1:
                    b = playerbullet(self.rect.right, self.rect.center[1], "right")
                    self.bullets.add(b)
                    self.index = 0
                    self.state = self.states.IDLERIGHT

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
                    self.index = 0

            if not keys.__contains__(1):
                if self.facing == "right":
                    if self.state != self.states.IDLERIGHT:
                        self.state = self.states.IDLERIGHT
                        self.index = 0
                else:
                    if self.state != self.states.IDLELEFT:
                        self.state = self.states.IDLELEFT
                        self.index = 0
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.state != self.states.SHOOTLEFT and self.state != self.states.SHOOTRIGHT:
                            if self.facing == "left":
                                self.state = self.states.SHOOTLEFT
                                self.index = 0
                            else:
                                self.state = self.states.SHOOTRIGHT
                                self.index = 0

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

                if self.state == self.states.RUNRIGHT:
                    if g.rect.top - self.rect.height / 4 <= self.rect.center[1] <= g.rect.bottom + self.rect.height / 4:
                        if self.rect.right >= g.rect.left and (self.rect.right <= g.rect.left + 15):
                            self.rect.right = g.rect.left
                            self.vel = 0
                    elif g.rect.top < self.rect.bottom:
                        self.vel = 10

                if self.state == self.states.RUNLEFT:
                    if g.rect.top - self.rect.height / 4 <= self.rect.center[1] <= g.rect.bottom + self.rect.height / 4:
                        if g.rect.right >= self.rect.left and (self.rect.left >= g.rect.left - 15):
                            self.rect.left = g.rect.right
                            self.vel = 0
                    elif g.rect.top < self.rect.bottom:
                        self.vel = 10

            if self.jumping:
                if self.jumpcounter < 10:
                    self.rect.y -= (15 - (3 * self.jumpcounter))
                else:
                    self.jumping = False
                self.jumpcounter += 1
            else:
                self.rect.y += 15

            self.counter += 1
            pygame.draw.line(Config.map, Config.RED, (self.rect.x, self.rect.y - 10), (self.rect.right, self.rect.y - 10),
                             4)
            pygame.draw.line(Config.map, Config.GREEN, (self.rect.x, self.rect.y - 10),
                             (self.rect.x + ((self.health / 10) * self.rect.width), self.rect.y - 10), 4)

            for b in self.bullets:
                for g in ground_sprites:
                    if g.rect.left <= b.rect.center[0] <= g.rect.right:
                        if g.rect.top <= b.rect.center[1] <= g.rect.bottom:
                            self.bullets.remove(b)
                if b.counter > 50:
                    self.bullets.remove(b)


    def damage(self, num):
        self.health -= num
