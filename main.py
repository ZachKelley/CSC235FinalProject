import pygame
from pygame import *
import Config
from Config import *
from classes.menus.main_menu import main_menu

current_menu = main_menu

def main():
    running = True

    while running:
        clock.tick(FPS)
        current_menu.run()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()



if __name__ == "__main__":
    main()