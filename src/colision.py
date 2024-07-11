import pygame
from setting import *
from config import *
from modo import *
from player import *


 
def handle_collisions(player: dict, enemies: list, reset_player, vidas_imgs: list)-> None:
    """
    Maneja las colisiones entre el jugador y los enemigos.

    Args:
        player (dict): Diccionario con los atributos del jugador.
        enemies (list): Lista de diccionarios con los atributos de los enemigos.
    """
    global is_running, game_over, start_time
    
    player_rect = pygame.Rect(player['x'], player['y'], player['width'], player['height'])
    
    for enemy in enemies.copy():
        enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy['width'], enemy['height'])
        
        
        if player_rect.colliderect(enemy_rect):
            choque_com_abeja_sound.play()
            player['lives'] -= 1
            print(player['lives'])
          
            if player['lives'] > 0:
                vidas_imgs_copy = vidas_imgs.copy()
                for vida_img in vidas_imgs_copy:
                    vidas_imgs.remove(vida_img)
                    break
                
            if player['lives'] == 0:
                is_running = False
                game_over = True
                start_time = pygame.time.get_ticks()
                return  
        
            reset_player(player)
            enemies.remove(enemy)

