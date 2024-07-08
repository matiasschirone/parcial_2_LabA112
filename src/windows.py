import pygame
from setting import *
from modo import *




def pantalla_inicio()-> None:
    #pantalla inicio
    background_comienzo = pygame.image.load(r'src\assets\scene-with-bees-flying-around-beehive-illustration-vector.jpg').convert()
    background_comienzo = pygame.transform.scale(background_comienzo, (WIDTH, HEIGHT))
    screen.blit(background_comienzo, ORIGIN)
    mostrar_texto(screen,"BEE'S", fuente, SCREEN_CENTER, BLACK)
    mostrar_texto(screen,"PULSA RCTRL PARA COMENZAR", fuente, MESSAGE_STAR_POS, WHITE)

    continuar = True
    pygame.display.flip()
    wait_user(pygame.K_RCTRL)
        
    
    
def pantalla_game_over():
    
    if game_over:
        pygame.mixer.music.stop()
        game_over_sound.play()
        background_game_over = pygame.image.load(r'src\assets\game_over3.png').convert()
        background_game_over = pygame.transform.scale(background_game_over, (WIDTH, HEIGHT))
        screen.blit(background_game_over, ORIGIN)
        mostrar_texto(screen, f"SCORE: {score}", fuente, LAST_SCORE_POS, WHITE)
        mostrar_texto(screen, f"MAXIMO SCORE: {max_score}", fuente, MAX_SCORE_POS, WHITE)
        mostrar_texto(screen, "PULSA RCTRL PARA COMENZAR", fuente, MESSAGE_STAR_POS, WHITE)
        pygame.display.flip()
        wait_user(pygame.K_RCTRL)  # Espera a que el usuario presione RCTRL para cerrar
