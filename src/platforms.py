import pygame
from setting import *

# Cargar imagen de la plataforma
platform_sprite = pygame.image.load(r'src/assets/grassHalf.png').convert_alpha()

def draw_platforms(platforms: list, debug_mode: bool)->None:
    """
    Dibuja las plataformas en la pantalla.

    Args:
        platforms (list): Lista de objetos pygame.Rect que representan las plataformas.
        debug_mode (bool): Indica si se debe mostrar el modo de depuración (dibujar rectángulos).
    """
    for platform in platforms:
        if debug_mode:
            pygame.draw.rect(screen, RED, platform, 4)
            sprite_width = platform_sprite.get_width()
            for x in range(platform.left, platform.right, sprite_width):
                screen.blit(platform_sprite, (x, platform.top))
        else:
            sprite_width = platform_sprite.get_width()
            for x in range(platform.left, platform.right, sprite_width):
                screen.blit(platform_sprite, (x, platform.top))


platforms = [
        pygame.Rect(50, 500, 210, 40),
        pygame.Rect(300, 450, 210, 40),
        pygame.Rect(550, 400, 210, 40),
        pygame.Rect(200, 350, 210, 40),
        pygame.Rect(600, 300, 210, 40),
        pygame.Rect(50, 250, 210, 40),
        pygame.Rect(400, 200, 210, 40),
        pygame.Rect(250, 150, 210, 40),
        pygame.Rect(450, 100, 210, 40)
    ]
