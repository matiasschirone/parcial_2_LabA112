import pygame
import random
from setting import *
from modo import *
from config import *
from sys import exit
from colision import handle_collisions



# Redimensionar sprites de enemigos
animaciones_enemigos = {'left': enemi_izq, 'right': enemi_dere}
reescalar_imagenes(animaciones_enemigos, 40, 30)

def initialize_enemies(platforms: list)-> list:
    """
    Inicializa los atributos de los enemigos.

    Returns:
        list: Lista de diccionarios con los atributos de los enemigos.
    """
    enemies = []
    for _ in range(6):
        while True:
            x = random.randint(0, WIDTH - 30)
            y = random.randint(50, HEIGHT - 200)
            enemy_rect = pygame.Rect(x, y, 30, 20)
            overlap = False
            for platform in platforms:
                if enemy_rect.colliderect(platform):
                    overlap = True
                    break
            if not overlap:
                enemies.append({
                    'x': x, 
                    'y': y, 
                    'width': 30,
                    'height': 20,
                    'speed': random.uniform(1.0, 3.0) * random.choice([-1, 1]),
                    'direction': 'left',
                    'sprite_index': 0
                })
                break
    return enemies



vidas_imgs = initialize_vidas(3)  
           
            
def update_enemies(enemies: list, platforms: list, player: dict)-> None:
    """
    Actualiza la posición y el comportamiento de los enemigos.

    Args:
        enemies (list): Lista de diccionarios con los atributos de los enemigos.
        platforms (list): Lista de objetos pygame.Rect que representan las plataformas.
        player (dict): Diccionario con los atributos del jugador.
    """
    for enemy in enemies.copy():
        enemy['x'] += enemy['speed']
        enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy['width'], enemy['height'])
        enemy['sprite_index'] = (enemy['sprite_index'] + 1) % len(animaciones_enemigos['left'])
        
        if enemy['x'] < 0 or enemy['x'] + enemy['width'] > WIDTH:
            enemy['speed'] *= -1
            enemy['direction'] = 'right' if enemy['speed'] > 0 else 'left'
        
        for platform in platforms:
            if enemy_rect.colliderect(platform):
                if enemy['speed'] > 0:
                    enemy['x'] = platform.left - enemy['width']
                    enemy['speed'] *= -1
                    enemy['direction'] = 'left'
                elif enemy['speed'] < 0:
                    enemy['x'] = platform.right
                    enemy['speed'] *= -1
                    enemy['direction'] = 'right'
        
        handle_collisions(player, enemies, reset_player)
        
        for other_enemy in enemies:
            if other_enemy != enemy:
                other_enemy_rect = pygame.Rect(other_enemy['x'], other_enemy['y'], other_enemy['width'], other_enemy['height'])
                if enemy_rect.colliderect(other_enemy_rect):
                    enemy['speed'] *= -1
                    other_enemy['speed'] *= -1
                    enemy['direction'] = 'left' if enemy['speed'] < 0 else 'right'
                    other_enemy['direction'] = 'left' if other_enemy['speed'] < 0 else 'right'
                    break



def draw_enemies(enemies: list, debug_mode: bool)-> None:
    """
    Dibuja a los enemigos en la pantalla.

    Args:
        enemies (list): Lista de diccionarios con los atributos de los enemigos.
        debug_mode (bool): Indica si se debe mostrar el modo de depuración (dibujar rectángulos).
    """
    for enemy in enemies:
        if debug_mode:
            pygame.draw.rect(screen, RED, (enemy['x'], enemy['y'], enemy['width'], enemy['height']), 3)
        else:
            sprite_list = animaciones_enemigos[enemy['direction']]
            sprite = sprite_list[enemy['sprite_index']]
            screen.blit(sprite, (enemy['x'], enemy['y']))