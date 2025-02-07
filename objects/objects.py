import pygame
from .bar.bar import Bar
from screen.screen import vw, vh


bar_in_game = Bar(width=vw(15), height=vh(3), xPos=vw(50), yPos=vh(85))
blocks = pygame.sprite.Group()