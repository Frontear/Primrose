import os
import pygame
from pygame.locals import *
from scenes.generic_scene import GenericScene

def main():
    pygame.init()

    screen = setup_display()
    scene = GenericScene(screen)

    update_screen = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)

        scene.draw(screen)

        if update_screen:
            pygame.display.update()
            update_screen = False

def setup_display():
    pygame.display.set_mode((854, 480))
    pygame.display.set_caption("Primrose")
    pygame.display.set_icon(pygame.image.load(os.path.join("assets", "icon.png")))

    return pygame.display.get_surface()

if __name__ == "__main__":
    main()