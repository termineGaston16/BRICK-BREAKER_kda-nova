import pygame

# Elegir una resolución de la lista (puedes cambiar el índice para probar otra)
resolutions = [
    (1920, 1080),  # Full HD
    (1366, 768),   # Laptop común
    (1280, 720),   # HD estándar
    (1024, 768),   # 4:3 más cuadrado
    (800, 600),    # Baja resolución
]
WIDTH, HEIGHT = resolutions[1]  # Cambia el índice para probar otra resolución

# info = pygame.display.Info()
# WIDTH, HEIGHT = info.current_w, info.current_h




screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("BRICK BREAKER")

def vw(percent): return round(WIDTH * (percent/100))
def vh(percent): return round(HEIGHT * (percent/100))


clock = pygame.time.Clock()
fps = 60

