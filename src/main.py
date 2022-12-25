import os
import pygame
from pygame.locals import *

def main():
    pygame.init()

    screen = setup_display()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 48)

    dialogue_box = load_image("dialogue_box.png")
    background = load_image("background.png")
    billy = pygame.transform.scale2x(load_image("billy.png"))
    text = font.render("Why hello there wonderful reader, it's a pleasure to meet you!", True, (255, 255, 255))

    scene = background.copy()
    scene.blit(billy, ((background.get_width() - billy.get_width()) / 2, 0))
    scene.blit(dialogue_box, (x := (background.get_width() - dialogue_box.get_width()) / 2, y := background.get_height() - dialogue_box.get_height() - 20))
    """
    scene_unscaled = x1, y1: 98, 592 | x2, y2: 1181, 627
    scene_scaled = x1, y1: 65, 394 | x2, y2: 788, 418
    dialogue_box = x1, y1: 58, 72 | x2, y2: 1141, 107
    obsolete_code: x1, y1: 27, 350??
    98 / 65 = 1280 / 854
    65 = 98 / (1280 / 854)
    """
    scene.blit(text, (x + (dialogue_box.get_width() - text.get_width()) / 2, y + (dialogue_box.get_height() - text.get_height()) / 2)) # TODO: text scaled down is grainy
    scene = pygame.transform.scale(scene, screen.get_size())

    update_screen = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)

        screen.blit(scene, (0, 0))

        if update_screen:
            pygame.display.update()
            update_screen = False

def setup_display():
    pygame.display.set_mode((854, 480))
    pygame.display.set_caption("Primrose")
    pygame.display.set_icon(load_image("icon.png"))

    return pygame.display.get_surface()

def load_image(name):
    return pygame.image.load(os.path.join("assets", name))

if __name__ == "__main__":
    main()