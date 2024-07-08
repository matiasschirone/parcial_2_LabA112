import pygame
              
WIDTH = 800
HEIGHT = 600
MID_WIDTH_SCREEN = WIDTH // 2
MID_HEIGHT_SCREEN = HEIGHT // 2
SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_CENTER = (MID_WIDTH_SCREEN, MID_HEIGHT_SCREEN)
ORIGIN = (0, 0)
SCORE_POS = (MID_WIDTH_SCREEN, 20)
TIME_POS = (120, 20)
VIDAS_POS = (WIDTH - 80, 10) 
LAST_SCORE_POS = (150, 20)
MAX_SCORE_POS = (WIDTH - 150, 20)
MUTE_POS = (60, HEIGHT - 60)
MESSAGE_STAR_POS = (MID_WIDTH_SCREEN, HEIGHT - 50)

FPS = 60
SPEED = 5

#colors    
CUSTOM = (226, 203, 95)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (226, 225, 225)

SIZE_PLAYER = (300, 300, 200, 100)


max_score = 0
game_over = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))


#cargo fuentes
pygame.font.init()
fuente = pygame.font.SysFont(None, 40)


pygame.mixer.init()
#cargo sonidos
coin_sound = pygame.mixer.Sound(r"src\assets\coin.mp3")
choque_com_abeja_sound = pygame.mixer.Sound(r"src\assets\sharp-punch.mp3")
piedrazo_abeja_sound = pygame.mixer.Sound(r"src\assets\jab-jab.mp3")
game_over_sound = pygame.mixer.Sound(r"src\assets\game_over_2.mp3")