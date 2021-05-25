import pygame
from pygame import *
import Config
from Config import *


def main():
    running = True

    while running:
        WIN.fill(BLUE)
        pygame.display.update()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()