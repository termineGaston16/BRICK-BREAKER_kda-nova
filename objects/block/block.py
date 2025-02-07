import pygame
import random
from ..object import Object


class Block(Object):
    def __init__(self, width, height, xPos, yPos, color, *groups):
        super().__init__(width, height, xPos, yPos, *groups)
        self.color = color
        self.reward = random.uniform(0.50, 5.50)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect(center=(self.xPos, self.yPos))
