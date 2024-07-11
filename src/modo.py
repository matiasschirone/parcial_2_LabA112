import pygame
import csv
from setting import *
from config import *
import csv
import json

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

def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def guardar_puntajes(scores: list)->None:
    """
    Guarda los puntajes y las vidas utilizadas en un archivo CSV.

    Parámetros:
    scores (list): Una lista que contiene dos elementos: el puntaje (score) y las vidas utilizadas.

    Return:
    None
    """
    try:
        with open(get_path_actual('puntajes.csv'),'a', encoding="utf-8") as file:
            headers = ['score', 'vidas utilizadas']
            writer = csv.DictWriter(file, fieldnames=headers)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({'score': scores[0], 'vidas utilizadas': scores[1]})
                
        print("Puntaje guardado exitosamente.")
    except IOError:
        print("Error al guardar el puntaje.")
        
def leer_puntajes() -> list:
    """
    Lee los puntajes guardados desde un archivo CSV y los devuelve como una lista de diccionarios.

    Parámetros:
    None

    Returns:
    list: Una lista de diccionarios donde cada diccionario contiene las claves 'score' y 'vidas utilizadas'.
    """
    puntajes = []
    try:
        with open(get_path_actual('puntajes.csv'),'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                puntajes.append({'score': row['score'], 'vidas utilizadas': row['vidas utilizadas']})
    except IOError:
        print("Error al leer los puntajes.")
    
    return puntajes

def guardar_puntajes_ordenados(puntajes: list):
    """
    Guarda puntajes ordenados en un archivo CSV.

    Parámetros:
    puntajes (list): Una lista de diccionarios donde cada diccionario contiene las claves 'score' y 'vidas utilizadas'.

    Returns:
    None
    """
    ordenar_lista_datos(puntajes, 'score', ascendente=False)
    try:
        with open(get_path_actual('puntajes_ordenados.csv'),'w', encoding="utf-8") as file:
            headers = ['score', 'vidas utilizadas']
            writer = csv.DictWriter(file, fieldnames=headers)

            # Escribir encabezado como una línea separada
            encabezado = ",".join(headers) + "\n"
            file.write(encabezado)

            # Escribir datos ordenados
            for puntaje in puntajes:
                # Convertir los valores a una lista de strings
                values = list(puntaje.values())
                formatted_values = []
                for value in values:
                    if isinstance(value, (int, float)):
                        formatted_values.append(str(value))
                    else:
                        formatted_values.append(value)
                
                # Escribir la línea en el archivo
                linea = ",".join(formatted_values) + "\n"
                file.write(linea)
                
        print("Puntajes ordenados guardados exitosamente.")
    except IOError:
        print("Error al guardar los puntajes ordenados.")

def guardar_puntajes_json(puntajes: list)->None:
    """
    Guarda puntajes en formato JSON en un archivo.

    Parámetros:
    puntajes (list): Una lista de diccionarios donde cada diccionario contiene información de puntajes.

    Returns:
    None
    """
    ordenar_lista_datos(puntajes, 'score', ascendente=False)
    with open(get_path_actual('puntajes_ordenados.json'), 'w') as jsonfile:
        json.dump(puntajes, jsonfile, indent=4)

def convertir_csv_a_json()->None:
    """
    Lee los puntajes desde un archivo CSV y los guarda en un archivo JSON.
    """
    puntajes = leer_puntajes()
    guardar_puntajes_json(puntajes)  
    
def leer_puntajes_json()-> list:
    """
    Lee puntajes desde un archivo JSON y los devuelve como una lista de diccionarios.

    Return:
    list: Una lista de diccionarios que contiene los puntajes leídos desde el archivo JSON.
          Si hay un error al leer el archivo, devuelve una lista vacía.
    """
    try:
        with open(get_path_actual('puntajes_ordenados.json'), 'r') as jsonfile:
            return json.load(jsonfile)
    except IOError:
        print("Error al leer el archivo JSON.")
        return []         

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
    


 
    
