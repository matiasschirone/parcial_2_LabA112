import pygame
from setting import *
import random


coin_img = pygame.image.load(r'src/assets/coin.png').convert_alpha()
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Función para inicializar las monedas
def initialize_coins(num_coins: int, platforms: list)-> list:
    """
    Inicializa las posiciones de las monedas en el juego.

    Args:
        num_coins (int): Número de monedas a inicializar.
        platforms (list): Lista de objetos pygame.Rect que representan las plataformas.

    Returns:
        list: Lista de diccionarios con las posiciones de las monedas inicializadas.
    """
    coins = []
    for _ in range(num_coins):
        while True:
            x = random.randint(0, WIDTH - coin_img.get_width())
            y = random.randint(0, HEIGHT - coin_img.get_height())
            coin_rect = pygame.Rect(x, y, coin_img.get_width(), coin_img.get_height())
            overlap = False
            for platform in platforms:
                if coin_rect.colliderect(platform):
                    overlap = True
                    break
            if not overlap:
                coins.append({'x': x, 'y': y, 'collected': False})
                break
    return coins


# Función para dibujar las monedas en la pantalla
def draw_coins(coins: list)-> None:
    """
    Dibuja las monedas en la pantalla.

    Args:
        coins (list): Lista de diccionarios con las posiciones de las monedas.
    """
    for coin in coins:
        if not coin['collected']:
            screen.blit(coin_img, (coin['x'], coin['y']))
            



def handle_coin_timer(coins: list, platforms: list)-> None:
    """
    Maneja la generación periódica de nuevas monedas.

    Args:
        coins (list): Lista de diccionarios con las posiciones de las monedas.
        platforms (list): Lista de objetos pygame.Rect que representan las plataformas.
    """
    new_coin = initialize_coins(1, platforms)  
    coins.append(new_coin[0])  
    



def update_coins(player, coins, score)-> int:
    """
    Actualiza el estado de las monedas y el puntaje del jugador.

    Args:
        player (dict): Diccionario con los atributos del jugador.
        coins (list): Lista de diccionarios con las posiciones de las monedas.
        score (int): Puntaje actual del jugador.

    Returns:
        int: Puntaje actualizado después de recolectar monedas.
    """
    player_rect = pygame.Rect(player['x'], player['y'], player['width'], player['height'])
    
    coins_copy = coins.copy()
    
    for coin in coins_copy:
        coin_rect = pygame.Rect(coin['x'], coin['y'], coin_img.get_width(), coin_img.get_height())
        if player_rect.colliderect(coin_rect) and not coin['collected']:
            coin_sound.play()
            coin['collected'] = True
            score += 10
            
            coins.remove(coin)
    
    return score