import pygame
from screen.screen import *
from states.main_menu.main_menu import main_menu
from states.in_game.in_game import in_game

# Estado inicial
state = "game"

while state != "quit":
    if state == "game":
        state = in_game()

pygame.quit()
