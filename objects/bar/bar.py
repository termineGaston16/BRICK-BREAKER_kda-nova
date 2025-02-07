import os
import pygame
from ..object import Object

class Bar(Object):
    def __init__(self, width, height, xPos, yPos, *groups):
        super().__init__(width, height, xPos, yPos, *groups)

        texture_path = os.path.join(os.path.dirname(__file__), "bar.texture.png")
        self.image = pygame.image.load(texture_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect(center=(self.xPos, self.yPos))

    def shiftLeft(self, vel, spacingLeft): 
        if not self.rect.x <= spacingLeft: self.rect.x -= vel

    def shiftRight(self, vel, spacingRight): 
        if not self.rect.x >= spacingRight: self.rect.x += vel

        


