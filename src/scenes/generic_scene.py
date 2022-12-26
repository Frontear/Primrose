import pygame
from scene import Scene

class GenericScene(Scene):
    def __init__(self, window: pygame.surface.Surface):
        self.background = self.load_image("background.png")
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 36)

        # ratios for scaling other assets
        w_r = window.get_width() / self.background.get_width()
        h_r = window.get_height() / self.background.get_height()

        self.background = pygame.transform.scale(self.background, window.get_size())

        self.dialogue_box = self.load_image("dialogue_box.png")
        self.dialogue_box = pygame.transform.scale(self.dialogue_box, (self.dialogue_box.get_width() * w_r, self.dialogue_box.get_height() * h_r))

        self.billy = self.load_image("billy.png")

        self.text = self.font.render("Why hello there wonderful reader, it's a pleasure to meet you!", True, (255, 255, 255))

    def draw(self, surface: pygame.surface.Surface):
        scene = self.background.copy()
        scene.blit(self.billy, ((self.background.get_width() - self.billy.get_width()) / 2, (self.background.get_height() - self.billy.get_height() / 2) / 4))
        scene.blit(self.dialogue_box, c:=((self.background.get_width() - self.dialogue_box.get_width()) / 2, (self.background.get_height() - self.dialogue_box.get_height() - 20)))
        scene.blit(self.text, (c[0] + (self.dialogue_box.get_width() - self.text.get_width()) / 2, c[1] + (self.dialogue_box.get_height() - self.text.get_height()) / 2))

        surface.blit(scene, (0, 0))