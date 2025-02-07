import pygame
from screen.screen import screen, clock, fps

pygame.font.init()  # 🔥 Asegurar que las fuentes están inicializadas

def main_menu():
    running = True
    while running:
        clock.tick(fps)
        screen.fill((15, 69, 147))  # Fondo del menú

        # Capturar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Iniciar juego
                    return "game"
                if event.key == pygame.K_ESCAPE:  # Salir del juego
                    return "quit"

        # Dibujar texto
        font = pygame.font.Font(None, 50)  # 🔥 Ahora funcionará sin errores
        text = font.render("Presiona ENTER para Jugar", True, (255, 255, 255))
        screen.blit(text, (200, 250))

        pygame.display.flip()

    return "quit"
