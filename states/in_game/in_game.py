import os
import pygame
from screen.screen import *
from objects.objects import bar_in_game
from objects.block_array.block_array import blocks, block_array

texture_path = os.path.join(os.path.dirname(__file__), "in_game_background.png")
background = pygame.image.load(texture_path).convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


block_array(8,10, vw(7), vw(1), vw(1.5), vw(13), vh(7))

def in_game():
    running = True
    while running:

        # RENDERIZADO
        clock.tick(fps)
        screen.blit(background, (0,0))
        screen.blit(bar_in_game.image, bar_in_game.rect)
        blocks.draw(screen)  


        # EVENTOS
        for event in pygame.event.get():

            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return "quit"

               
        # MANTENER TECLA
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: bar_in_game.shiftLeft(5, vw(10))
        if keys[pygame.K_RIGHT]: bar_in_game.shiftRight(5, vw(75))


        pygame.display.flip()

    return "quit"
