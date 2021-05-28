import pygame
from pygame import *
from pygame.mixer import Sound

import Config
from Config import *
from classes.menus.main_menu import main_menu

music = Sound("./Sounds/backgroundsound.mp3")
music.set_volume(.2)

Config.current_menu = main_menu

def main():
    running = True

    while running:
        music.play()
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

            if p.rect.y - HEIGHT/2 > 0:
                if p.rect.y + Config.HEIGHT/2 < Config.map.get_height():
                    Config.y = p.rect.y - Config.HEIGHT/2
                elif p.rect.y + Config.HEIGHT / 2 > Config.map.get_height():
                    Config.y = Config.map.get_height() - HEIGHT
                else:
                    Config.y = 0

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