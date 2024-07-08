import pygame
from setting import *
from config import *


def handle_shooting(player: dict)-> None:
    """
    Maneja el disparo de proyectiles por parte del jugador.

    Args:
        player (dict): Diccionario con los atributos del jugador.
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LALT]:
        if len(player['projectiles']) == 0:
            new_projectile = {'x': player['x'], 'y': player['y'], 'speed': 10, 'image': proyectil_img}  # Utiliza la imagen del proyectil
            player['projectiles'].append(new_projectile)

def update_projectiles(player: dict, enemies: list)-> None:
    """
    Actualiza la posición de los proyectiles y maneja las colisiones con enemigos.

    Args:
        player (dict): Diccionario con los atributos del jugador.
        enemies (list): Lista de diccionarios con los atributos de los enemigos.
    """
    projectiles_copy = player['projectiles'].copy()
    enemies_copy = enemies.copy()
    
    for projectile in projectiles_copy:
        projectile['x'] += projectile['speed']
        projectile_rect = pygame.Rect(projectile['x'], projectile['y'], 15, 10)
        
        for enemy in enemies_copy:
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy['width'], enemy['height'])
            if projectile_rect.colliderect(enemy_rect):
                piedrazo_abeja_sound.play()
                player['projectiles'].remove(projectile)
                enemies.remove(enemy)
        
        if projectile['x'] > WIDTH:
            player['projectiles'].remove(projectile)

# Función para dibujar los proyectiles
def draw_projectiles(player: dict)-> None:
    """
    Dibuja los proyectiles en la pantalla.

    Args:
        player (dict): Diccionario con los atributos del jugador.
    """
    for projectile in player['projectiles']:
        screen.blit(projectile['image'], (projectile['x'], projectile['y']))
        