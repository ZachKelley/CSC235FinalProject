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
        Config.map.convert_alpha()
        WIN.blit(Config.map, (-1 * Config.x, -1 * Config.y))
        current_menu.run()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[K_d]:
            Config.x += 10
        if keys[K_a]:
            Config.x -= 10
        if keys[K_s]:
            Config.y += 10
        if keys[K_w]:
            Config.y -= 10

    pygame.quit()



if __name__ == "__main__":
    main()