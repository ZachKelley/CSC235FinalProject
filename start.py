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
    text1 = font.render("A fatal crash occurs with the mother ship leaving you stranded on an unknown planet called "
                       "Aatrox.", True, (255,255,255))
    text2 = font.render("Pieces of the ship are scattered amongst the planet, having you adventure the land and gather "
                       "pieces of ", True, (255,255,255))
    text3 = font.render("the ship to get back into orbit. While looking for pieces to the ship, you are encountered with a bug ", True, (255,255,255))

    text4 = font.render("subspecies called the Zerg, they look as if they are multiplying and taking control of the spots to where ", True, (255,255,255))

    text5 = font.render("pieces of the ship remain. Killing the Zerglings are needed to even get close to the ship reckages. ", True, (255,255,255))

    text6 = font.render("The queen of the Zerg happens to be nesting around the radioactive power core to your ship.", True, (255,255,255))

    WIN.blit(text1, (10, 100))
    WIN.blit(text2, (10, 140))
    WIN.blit(text3, (10, 180))
    WIN.blit(text4, (10, 220))
    WIN.blit(text5, (10, 260))
    WIN.blit(text6, (10, 300))

    startfont = pygame.font.Font("./OpenSans-Bold.ttf", 72)
    start = startfont.render("press any button to start", True, (255,255,255))

    WIN.blit(start, (WIDTH/2 - start.get_width()/2, HEIGHT/2 - start.get_height()/2))

    keys = pygame.key.get_pressed()
    if keys.__contains__(1):
        Config.current_menu = game

    pygame.display.update()
