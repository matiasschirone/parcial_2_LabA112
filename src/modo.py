import pygame
import csv
from setting import *
from config import *


DEBUG = False

def cambiar_modo():
    global DEBUG
    DEBUG = not DEBUG
    
def get_mode():
    return DEBUG



def salir_juego()-> None:
    pygame.quit()
    exit()

def mostrar_texto(superficie: pygame.surface, texto: str, fuente: pygame.font, posicion: tuple[int, int], color: tuple[int, int, int], color_fondo: tuple[int, int, int]= None)-> None:
    """
    Muestra texto en la pantalla.

    Args:
        superficie (pygame.surface): Superficie donde se dibujará el texto.
        texto (str): Texto que se mostrará.
        fuente (pygame.font): Fuente utilizada para el texto.
        posicion (tuple[int, int]): Posición (x, y) donde se centrará el texto.
        color (tuple[int, int, int]): Color del texto en formato RGB.
        color_fondo (tuple[int, int, int], optional): Color de fondo del texto en formato RGB. Default None.
    """
    sup_texto = fuente.render(texto, True, color, color_fondo)
    rect_texto = sup_texto.get_rect()
    rect_texto.center = posicion
    superficie.blit(sup_texto, rect_texto)
    
    
def wait_user(tecla: int)-> None:
    """
    Espera a que el usuario presione una tecla específica para continuar.

    Args:
        tecla (int): Código de la tecla que debe presionarse para continuar.
    """
    continuar = True
    while continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir_juego()
            elif event.type == pygame.KEYDOWN:
                if event.key == tecla:
                    continuar = False
                    
def swap_lista(lista: list, i: int, j: int)->None:
    """
    Intercambia dos elementos en una lista.

    Args:
        lista (list): Lista donde se realizará el intercambio.
        i (int): Índice del primer elemento.
        j (int): Índice del segundo elemento.
    """
    aux =  lista[i]
    lista[i] =lista[j]
    lista[j] =aux
                    
def ordenar_lista_datos(lista: list, campo: str, ascendente: bool = True) -> None:
    """
    Ordena una lista de datos según un campo específico.

    Args:
        lista (list): Lista de diccionarios que representan datos.
        campo (str): Nombre del campo por el cual ordenar.
        ascendente (bool, optional): True para ordenar de manera ascendente, False para descendente. Default True.
    """
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if (ascendente and int(lista[i][campo]) > int(lista[j][campo])) or (not ascendente and int(lista[i][campo]) < int(lista[j][campo])):
                swap_lista(lista,i,j)

def guardar_puntajes(scores, filename='scores.csv')-> None:
    """
    Guarda los puntajes en un archivo CSV.

    Args:
        scores (list): Lista con los puntajes a guardar.
        filename (str, optional): Nombre del archivo CSV. Default 'scores.csv'.
    """
    try:
        with open(filename, 'r', encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            current_scores = list(reader)
    except FileNotFoundError:
        current_scores = []

    current_scores.append(scores)
    
    ordenar_lista_datos(current_scores, campo=0, ascendente=False)
    
    current_scores = current_scores[:3]
    
    # Convierte el nombre a mayúsculas como lo hiciste antes
    for i in range(len(current_scores)):
        current_scores[i][0] = current_scores[i][0].upper()

    # Guarda los puntajes actualizados en el archivo CSV
    with open(filename, mode='w', encoding= "utf-8") as archivo:
        encabezado = ",".join(current_scores[0]) + "\n"
        archivo.write(encabezado)
        for persona in current_scores:
            linea = ",".join(persona) + "\n"
            archivo.write(linea)
            

def reset_player(player: dict)-> None:
    """
    Reinicia la posición del jugador.

    Args:
        player (dict): Diccionario con los atributos del jugador.
    """
    player['x'] = WIDTH // 2
    player['y'] = HEIGHT - 50
    player['speed_x'] = 0
    player['speed_y'] = 0
    player['on_ground'] = True
    global vidas_imgs
    vidas_imgs = initialize_vidas(player['max_lives'])