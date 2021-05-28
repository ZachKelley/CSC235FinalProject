import sys

import Config
from Config import *
from main import main

pygame.init()
pygame.font.init()


bg = pygame.image.load("./backgroundSpace.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))


def run():
    WIN.blit(bg, (0, 0))
    font = pygame.font.Font("./OpenSans-Bold.ttf", 36)
    text1 = font.render("Congratulations you have completed your mission and picked up all", True, (255, 255, 255))
    text2 = font.render("necessary materials to get you ship into orbit, you headed back to the ship and repaired.", True, (255, 255, 255))
    text3 = font.render("You and your team started the ship and blasted into orbit. MISSION SUCCESS", True, (255, 255, 255))

    WIN.blit(text1, (10, 200))
    WIN.blit(text2, (10, 240))
    WIN.blit(text3, (10, 280))

    startfont = pygame.font.Font("./OpenSans-Bold.ttf", 72)
    start = startfont.render("press any button to EXIT", True, (255, 255, 255))

    WIN.blit(start, (WIDTH / 2 - start.get_width() / 2, HEIGHT / 2 - start.get_height() / 2))

    keys = pygame.key.get_pressed()
    if keys.__contains__(1):
        pygame.quit()
        sys.exit()

    pygame.display.update()
