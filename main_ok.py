import pygame
from os import system
system ("cls")
from clase_juego import Juego
import funciones_data_base  
import ranking

def tetris():
    pygame.init()

    juego = Juego() #Llamamos a la "Clase principal" 
    nombre_jugador = "" # Inicialización del nombre del jugador: espacio en blanco para que el jugador pueda ingresar su nombre
    nombre_jugador = str(nombre_jugador)
    puntaje_final = 0

    #COLORES
    COLOR_FONDO = (204, 204, 255)
    COLOR_CELESTE_PASTEL = (153, 235, 255)
    COLOR_FUENTE =  (170, 128, 255)
    COLOR_ROSA_PASTEL = (255, 153, 255)

    #FUENTES, TAMAÑO DE LETRA
    fuente_texto = pygame.font.SysFont("Times New Roman", 35)
    fuente_nombre = pygame.font.SysFont("Times New Roman", 30)
    fuente_reseteo = pygame.font.SysFont("Times New Roman", 25)

    #RENDERIZADO DE FUENTE (texto, antialias: True, COLOR)
    superficie_puntaje = fuente_texto.render("Puntaje:", True, COLOR_FUENTE)
    superficie_siguiente_bloque = fuente_texto.render("Siguiente:", True, COLOR_FUENTE)

    #RECTÁNGULOS (x , y, ancho, alto)
    siguiente_bloque_rectangulo = pygame.Rect(320, 215, 170, 180)
    puntaje_rectangulo = pygame.Rect(323, 75, 165, 60)

    #IMÁGENES
    imagen_juego_terminado = pygame.image.load("C:/Users/jazmi/Desktop/Progra y labo UTN 2023/Programación 1er Cuatri/Post 1er parcial/PROYECTO PYGAME/pygame tetris/Imagenes/game over.png")
    imagen_juego_terminado = pygame.transform.scale(imagen_juego_terminado,(600,600))

    #VENTANA DEL PROGRAMA
    ANCHO_PANTALLA = 500
    ALTO_PANTALLA = 620
    pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA)) # Seteo medidas de la pantalla
    pygame.display.set_caption("Tetris con pygame") # Título del programa

    # CREACIÓN DE UN EVENTO PROPIO
    timer_milisegundos = pygame.USEREVENT
    pygame.time.set_timer(timer_milisegundos, 190) # Velocidad puesta en milisegundos

    #LOOP DEL JUEGO
    flag_correr = True
    funciones_data_base.crear_tabla("C:/Users/jazmi/Desktop/Progra y labo UTN 2023/Programación 1er Cuatri/data_base_tetris.db")

    while flag_correr:
        
        lista_eventos = pygame.event.get() 
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_correr = False

            if evento.type == pygame.KEYDOWN: # Cuando se presione una tecla por vez...
                if evento.key == pygame.K_BACKSPACE and juego.juego_terminado == True:
                    nombre_jugador = nombre_jugador[0:-2] # Se eliminan dos espacios (un caracter cualquiera y el "." que le sigue preestablecido)
                elif len(nombre_jugador) < 6: 
                    nombre_jugador += evento.unicode + "."

                if evento.key == pygame.K_RETURN and juego.juego_terminado == True:        
                    return nombre_jugador, puntaje_final

                if evento.key == pygame.K_SPACE and juego.juego_terminado == True:
                    juego.juego_terminado = False
                    juego.resetear_juego() 
                    juego.musica_fondo.play(-1)

                if evento.key == pygame.K_LEFT and juego.juego_terminado == False:
                    juego.mover_izquierda()

                if evento.key == pygame.K_RIGHT and juego.juego_terminado == False:
                    juego.mover_derecha()

                if evento.key == pygame.K_DOWN and juego.juego_terminado == False:
                    juego.mover_abajo()
                    juego.actualizar_puntaje(0)

                if evento.key == pygame.K_UP and juego.juego_terminado == False:
                    juego.rotar_bloque()

            elif evento.type == timer_milisegundos and juego.juego_terminado == False:
                juego.mover_abajo()

        # "Dibujos" en la pantalla
        superficie_valor_puntaje = fuente_texto.render(str(juego.puntaje), True, COLOR_FUENTE)
        puntaje_final = juego.puntaje

        pantalla.fill(COLOR_FONDO) # Llenamos el fondo del juego
        pantalla.blit(superficie_puntaje, (340, 20, 50, 50)) # Fundir en la pantalla: texto para el puntaje, (x,y,ancho, alto)
        pantalla.blit(superficie_siguiente_bloque, (332, 160, 50, 50)) # Fundir en la pantalla: texto para le siguiente bloque, (x,y,ancho,alto)

        pygame.draw.rect(pantalla,COLOR_CELESTE_PASTEL, puntaje_rectangulo, 0, 10) # Dibujo del cubo que contiene el puntaje
        pantalla.blit(superficie_valor_puntaje, superficie_valor_puntaje.get_rect(centerx = puntaje_rectangulo.centerx,
                centery = puntaje_rectangulo.centery)) # Fundir en la pantalla: cubo que contiene el puntaje
        pygame.draw.rect(pantalla, COLOR_CELESTE_PASTEL, siguiente_bloque_rectangulo, 0, 10) # Dibujo del cubo que contiene el siguiente bloque 
        juego.draw(pantalla)

        # JUEGO TERMINADO
        if juego.juego_terminado == True: 
            pantalla.blit(imagen_juego_terminado, (-70,-40)) # Fundir en la pantalla: Imagen OH NO, posición
            
            fuente_titulo_superficie = fuente_nombre.render("Ingrese 3 iniciales: ",True,(140, 26, 255))
            superficie_fuente_reseteo = fuente_reseteo.render("o bien, aprete ESPACIO para reiniciar el juego", True, "White")
            ingreso_rect = pygame.Rect(120,450,210,50) # Rectángulo del ingreso de nombre 
            pygame.draw.rect(pantalla,COLOR_ROSA_PASTEL, ingreso_rect) # Dibujo del rectángulo de ingreso de nombre: superficie, color, valor del rectángulo
            pygame.draw.rect(pantalla,"White", ingreso_rect,2) # # Dibujo del marquito del ingreso de nombre: superficie, color, valor del rectángulo, ancho de más

            fuente_nombre_superficie = fuente_nombre.render(nombre_jugador.upper(),True,(140, 26, 255)) # Superficie para la fuente del nombre del jugador
            pantalla.blit(fuente_nombre_superficie, (ingreso_rect.x + 65, ingreso_rect.y + 10)) # Fundir en la pantalla: nombre del jugador, posición # ingreso_rect.x + 5
            pantalla.blit(fuente_titulo_superficie, (120, 415, 210,50))
            pantalla.blit(superficie_fuente_reseteo, (20,505,210,50))
            juego.musica_fondo.stop() # La música de fondo se detiene

        pygame.display.flip() # Actualizar todos los cambios en la pantalla

    pygame.quit()

datos = tetris()

try:
    funciones_data_base.agregar_datos_a_db("C:/Users/jazmi/Desktop/Progra y labo UTN 2023/Programación 1er Cuatri/data_base_tetris.db",datos[0], datos[1])
    ranking.mostrar_ranking()
except:
    pygame.quit()





