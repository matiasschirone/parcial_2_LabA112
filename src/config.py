import pygame

def girar_imagenes(lista_original,flip_x,flip_y):
    lista_girada = []
    for img in lista_original:
        lista_girada.append(pygame.transform.flip(img, flip_x, flip_y))
        
    return lista_girada

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))
            
           
#Definimos los fotogramas de cada animacion.            

player_quieto_derecha = [pygame.image.load(r"src\assets\der1.png")]
player_quieto_izquierda = [pygame.image.load(r"src\assets\der1.png")]

player_corre_dere = [pygame.image.load(r"src\assets\der1.png"),
                    pygame.image.load(r"src\assets\der2.png")]

player_corre_izq = [pygame.image.load(r"src\assets\izq1.png"),
                    pygame.image.load(r"src\assets\izq2.png")]

player_salta_derecha = [pygame.image.load(r"src\assets\der2.png")]
player_salta_izquierda = [pygame.image.load(r"src\assets\izq2.png")]

pierde_vida = [pygame.image.load(r"src\assets\pierde_vida.png")]

perder_vida_img = pygame.image.load(r'src\assets\pierde_vida.png').convert_alpha()
perder_vida_img = pygame.transform.scale(perder_vida_img, (50, 50)) 
                                   
enemi_izq = [pygame.image.load(r"src\assets\3.png"),
                    pygame.image.load(r"src\assets\4.png"),
                    pygame.image.load(r"src\assets\5.png"),
                    pygame.image.load(r"src\assets\6.png")]

enemi_dere = girar_imagenes(enemi_izq, True, False)


flor = [pygame.image.load(r"src\assets\flor.png")]

proyectil_img = pygame.image.load(r"src\assets\piedra.png")
proyectil_img = pygame.transform.scale(proyectil_img, (15, 10))

def initialize_vidas(num_vidas: int)-> list:
    """
    Inicializa las imágenes de las vidas del jugador.

    Args:
        num_vidas (int): Número de vidas a inicializar.

    Returns:
        list: Lista de imágenes de las vidas inicializadas.
    """
    vida_img = pygame.image.load(r'src/assets/v0.png').convert_alpha()
    vida_img = pygame.transform.scale(vida_img, (30, 30))
    return [vida_img for _ in range(num_vidas)]
