import pygame
direction = ["left", "right"]
char = pygame.image.load("./Images/player/standing.png")

walkRight = [pygame.image.load("./Images/player/R1.png"), pygame.image.load("./Images/player/R2.png"),
             pygame.image.load("./Images/player/R3.png"), pygame.image.load("./Images/player/R4.png"),
             pygame.image.load("./Images/player/R5.png"), pygame.image.load("./Images/player/R6.png"),
             pygame.image.load("./Images/player/R7.png"), pygame.image.load("./Images/player/R8.png"),
             pygame.image.load("./Images/player/R9.png")]
walkLeft = [pygame.image.load("./Images/player/L1.png"), pygame.image.load("./Images/player/L2.png"),
            pygame.image.load("./Images/player/L3.png"), pygame.image.load("./Images/player/L4.png"),
            pygame.image.load("./Images/player/L5.png"), pygame.image.load("./Images/player/L6.png"),
            pygame.image.load("./Images/player/L7.png"), pygame.image.load("./Images/player/L8.png"),
            pygame.image.load("./Images/player/L9.png")]


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 7
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.face = 0
        self.hitbox = (self.x + 17, self.y + 6, 30, 60)
        self.health = 40


    def damaged(self):
        if self.health > 0:
            self.health -= 1
            print('damaged')
        else:
            print('you died')
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.face = direction[0]
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                self.face = direction[1]
        else:
            if self.face is direction[1]:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 3, 40, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 3, 40 - (40 - self.health), 10))

        self.hitbox = (self.x + 17, self.y + 6, 30, 60)