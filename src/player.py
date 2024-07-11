import pygame
from setting import *
from config import *
from enemis import *
from modo import *

def initialize_player()-> dict:
    """
    Inicializa los atributos del jugador.

    Returns:
        dict: Diccionario con los atributos del jugador.
    """
    
    animations = {
        'quieto_derecha': player_quieto_derecha,
        'quieto_izquierda': player_quieto_izquierda,
        'corre_derecha': player_corre_dere,
        'corre_izquierda': player_corre_izq,
        'salta_derecha': player_salta_derecha,
        'salta_izquierda': player_salta_izquierda,
        'pierde_vida': pierde_vida
    }

    # Reescala las imágenes de las animaciones a 50x50
    for key in animations:
        frames = animations[key]
        for i in range(len(frames)):
            frames[i] = pygame.transform.scale(frames[i], (40, 50))

    return {
        'x': WIDTH // 2,
        'y': HEIGHT - 50,
        'width': 40,
        'height': 50,
        'speed_x': 0,
        'speed_y': 0,
        'on_ground': False,
        'gravity': 0.5,
        'jump_power': -10,
        'alt_pressed': False,
        'projectiles': [],
        'lives': 3,
        'max_lives': 3,
        'animations': animations,
        'current_animation': 'quieto_derecha',
        'animation_index': 0,
        'animation_speed': 0.2,
        'direction' : 1
    }


    

# Función para actualizar la lógica del jugador
def update_player(player: dict, platforms: list)-> None:
    """
    Actualiza la posición del jugador y maneja las colisiones con las plataformas.

    Args:
        player (dict): Diccionario con los atributos del jugador.
        platforms (list): Lista de objetos pygame.Rect que representan las plataformas.
    """
    player['speed_y'] += player['gravity']
    player['x'] += player['speed_x']
    player['y'] += player['speed_y']

    if player['x'] < 0:
        player['x'] = 0
    elif player['x'] + player['width'] > WIDTH:
        player['x'] = WIDTH - player['width']

    if player['y'] < 0:
        player['y'] = 0
    elif player['y'] + player['height'] > HEIGHT:
        player['y'] = HEIGHT - player['height']

    if player['y'] + player['height'] >= HEIGHT:
        player['y'] = HEIGHT - player['height']
        player['speed_y'] = 0
        player['on_ground'] = True

    player_rect = pygame.Rect(player['x'], player['y'], player['width'], player['height'])
    for platform in platforms:
        if player_rect.colliderect(platform):
            if player['speed_y'] > 0:
                player['y'] = platform.top - player['height']
                player['speed_y'] = 0
                player['on_ground'] = True
            elif player['speed_y'] < 0:
                player['y'] = platform.bottom
                player['speed_y'] = 1


def draw_player(player: dict, debug_mode)-> None:
    current_animation = player['current_animation']
    animation_index = player['animation_index']
    x = player['x']
    y = player['y']

   
    animation_frames = player['animations'][current_animation]
    num_frames = len(animation_frames)


    if animation_index < num_frames:

        screen.blit(animation_frames[animation_index], (x, y))

        player['animation_index'] += 1

    if player['animation_index'] >= num_frames:
        player['animation_index'] = 0

    if debug_mode:
        pygame.draw.rect(screen, RED, (x, y, player['width'], player['height']), 2)
       


def draw_vidas(screen: pygame.Surface, vidas_imgs: list, vidas: int):
    """
    Dibuja las vidas del jugador en la pantalla.

    Args:
        screen (pygame.Surface): Superficie de la pantalla donde se dibujan las vidas.
        vidas_imgs (list): Lista de imágenes de las vidas del jugador.
        vidas (int): Número de vidas a dibujar.
    """
    vidas_pos = VIDAS_POS
    
    if vidas > len(vidas_imgs):
        vidas = len(vidas_imgs)

    for i in range(vidas):
        vida_img = vidas_imgs[i]
        x = vidas_pos[0] - i * (vida_img.get_width() + 5)  
        y = vidas_pos[1]
        screen.blit(vida_img, (x, y)) 
        
