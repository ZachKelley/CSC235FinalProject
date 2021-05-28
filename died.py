import Config
from Config import *
from classes.menus.game import game

pygame.init()
pygame.font.init()


bg = pygame.image.load("./backgroundSpace.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))


def run():
    WIN.blit(bg, (0,0))
    font = pygame.font.Font("./OpenSans-Bold.ttf", 36)
    text = font.render("You have died and did not complete you mission to get back into orbit. Please try again...", True, (255,255,255))
    WIN.blit(text, (200, 450))
    pygame.display.update()
