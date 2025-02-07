import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, width, height, xPos, yPos, *groups):
        super().__init__(*groups)
        self.width = width
        self.height = height
        self.xPos = xPos
        self.yPos = yPos




