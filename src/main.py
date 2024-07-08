import pygame
from setting import *
from modo import *
from sys import exit
from player import *
from enemis import *
from coin import *
from platforms import *
from windows import *




    
# Inicializar Pygame
pygame.init()

# Reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()


# Configurar la pantalla


pygame.display.set_caption("BEES'S GAME")

# Cargar imagen de fondo
background = pygame.image.load(r'src/assets/Grasslands.png').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))





#musica de fondo
pygame.mixer.music.load(r"src\assets\musica_fondo.mp3")
pygame.mixer.music.set_volume(0.1)



#cargo imagenes
sound_on = pygame.image.load(r'src\assets\on.png')
sound_on = pygame.transform.scale(sound_on, (30, 30))

sound_off = pygame.image.load(r'src\assets\R.png')
sound_off = pygame.transform.scale(sound_off, (40, 40))







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
        









TIMERCOIN =pygame.USEREVENT + 1
GAMETIMEOUT = pygame.USEREVENT +2



start_time = pygame.time.get_ticks()

while True:
    
    pantalla_inicio()
    
    player = initialize_player()
    
    enemies = initialize_enemies(platforms)
   
    coins = initialize_coins(10, platforms)  
        
    pygame.mixer.music.play(-1)
    playing_music = True
    
    pygame.time.set_timer(TIMERCOIN, 5000)
    
    pygame.time.set_timer(GAMETIMEOUT, 10000)

    score = 0
    is_running = True
    game_over = False
    
    start_time = pygame.time.get_ticks()
    
    while is_running:
        clock.tick(FPS)
        
        current_time = pygame.time.get_ticks()
        time_seconds = (current_time - start_time) // 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir_juego()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    cambiar_modo()
                if event.key == pygame.K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music
                if event.key == pygame.K_p:
                    pygame.mixer.music.pause()
                    mostrar_texto(screen, "PAUSA", fuente, SCREEN_CENTER, MAGENTA)
                    pygame.display.flip()
                    wait_user(pygame.K_p)
                    if playing_music:
                        pygame.mixer.music.unpause()
                        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player['speed_x'] = -5
                player['current_animation'] = 'corre_izquierda'
            elif keys[pygame.K_RIGHT]:
                player['speed_x'] = 5
                player['current_animation'] = 'corre_derecha'
            else:
                player['speed_x'] = 0
                if player['on_ground']:
                    if player['current_animation'] == 'corre_derecha':
                        player['current_animation'] = 'quieto_derecha'
                    elif player['current_animation'] == 'corre_izquierda':
                        player['current_animation'] = 'quieto_izquierda'
            
            if keys[pygame.K_SPACE] and player['on_ground']:
                player['speed_y'] = player['jump_power']
                player['on_ground'] = False
                if player['speed_x'] > 0:
                    player['current_animation'] = 'salta_derecha'
                elif player['speed_x'] < 0:
                    player['current_animation'] = 'salta_izquierda'
            
            if keys[pygame.K_LALT]:
                handle_shooting(player)   
                
            if event.type == TIMERCOIN:
                print("se lanzo el evento")
                handle_coin_timer(coins, platforms)
            if event.type == GAMETIMEOUT:
                game_over = True 
                is_running = False
                start_time = pygame.time.get_ticks()
                    
            
                    
        screen.blit(background, ORIGIN)
        
        score = update_coins(player, coins, score)
        
        
        mostrar_texto(screen, f"SCORE: {score}", fuente, SCORE_POS, BLACK)
        
        mostrar_texto(screen, f"Tiempo: {time_seconds}", fuente, TIME_POS, BLACK)
        
        if playing_music:
            screen.blit(sound_on, (10, 10))
        else:
            screen.blit(sound_off, (10, 10))

        
        # handle_input(player)
        update_player(player, platforms)
        update_enemies(enemies, platforms, player)
        update_projectiles(player, enemies)
        

        draw_platforms(platforms, get_mode())
        draw_enemies(enemies, get_mode())
        draw_player(player, get_mode())
        draw_projectiles(player)
        draw_coins(coins)
        num_vidas = player["lives"]
        draw_vidas(screen, vidas_imgs, num_vidas)
       
        
        
        
        pygame.display.flip()
        
    #pantalla game over
    if score > max_score:
            max_score = score
    scores = [str(max_score), str(player['max_lives'] - player['lives'])]
    guardar_puntajes(scores)
    pantalla_game_over()

salir_juego()

