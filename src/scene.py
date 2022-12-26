import os
import pygame
from abc import ABC, abstractmethod

"""
load_assets
transform_assets
"""
class Scene(ABC):
    def __init__(self, window: pygame.surface.Surface):
        pass

    def load_image(self, name):
        return pygame.image.load(os.path.join("assets", name))

    @abstractmethod
    def draw(self, surface: pygame.surface.Surface):
        pass