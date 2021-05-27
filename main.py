import pygame
from pygame import *
import Config
from Config import *
from classes.menus.main_menu import main_menu

Config.current_menu = main_menu

def main():
    running = True
    Config.map.convert_alpha()

    while running:
        clock.tick(FPS)
        for p in main_menu.player_sprite:
            if Config.x > 0:
                Config.x = p.rect.x - WIN.get_width()/2
                if Config.x + Config.WIDTH < Config.map.get_width():
                    Config.x = p.rect.x - WIN.get_width() / 2
                else:
                    if p.rect.x + WIDTH/2 < Config.map.get_width():
                        Config.x = p.rect.x - WIN.get_width() / 2
                    Config.x = p.rect.x - (WIDTH - (Config.map.get_width() - p.rect.x))
            else:
                if p.rect.x - WIN.get_width()/2 > 0:
                    Config.x = p.rect.x - WIN.get_width()/2
            if Config.y > 0:
                Config.y = p.rect.y - Config.HEIGHT/2
                if Config.y + Config.HEIGHT/2 < Config.map.get_height():
                    Config.y = p.rect.y - Config.map.get_height() / 2
                else:
                    Config.y = p.rect.y - (Config.map.get_height() - (Config.map.get_height() - p.rect.bottom))
            else:
                if p.rect.y - WIN.get_height()/2 > 0:
                    Config.y = p.rect.y - Config.map.get_height() / 2
                else:
                    Config.y = p.rect.y - (0 + p.rect.y)

        Config.map.convert_alpha()
        WIN.blit(Config.map, (-1 * Config.x, -1 * Config.y))
        Config.current_menu.run()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()



if __name__ == "__main__":
    main()