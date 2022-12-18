import os
import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    pygame.display.set_mode((854, 480))
    pygame.display.set_caption("Primrose")
    pygame.display.set_icon(pygame.image.load(os.path.join("assets", "icon.png")))

    screen = pygame.display.get_surface()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 32)

    dialogue_box = pygame.image.load(os.path.join("assets", "dialogue_box.png"))
    background = pygame.image.load(os.path.join("assets", "background.png"))
    character = pygame.image.load(os.path.join("assets", "character.png"))
    generic_text = font.render("Why hello there wonderful reader, it's so nice to meet you!", True, (255, 255, 255))

    dialogue_box = pygame.transform.scale(dialogue_box, (dialogue_box.get_width() / (background.get_width() / screen.get_width()), dialogue_box.get_height() / (background.get_height() / screen.get_height())))
    background = pygame.transform.scale(background, pygame.display.get_window_size())

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        screen.blit(background, (0, 0))
        screen.blit(character, ((screen.get_width() - character.get_width()) / 2, character.get_height() / 8))
        screen.blit(dialogue_box, (x := (background.get_width() - dialogue_box.get_width()) / 2, y := background.get_height() - dialogue_box.get_height() - 10))
        #screen.blit(generic_text, (x, y))
        screen.blit(generic_text, (x + (dialogue_box.get_width() - generic_text.get_width()) / 2, y + (dialogue_box.get_height() - generic_text.get_height()) / 2))

        pygame.display.update()