import pygame
import funciones_data_base

def mostrar_ranking():
    pygame.init()

    pygame.display.set_caption("Ranking Tetris")
    pantalla = pygame.display.set_mode((500,620))

    imagen_fondo_ranking = pygame.image.load("C:/Users/jazmi/Desktop/Progra y labo UTN 2023/Programación 1er Cuatri/Post 1er parcial/PROYECTO PYGAME/pygame tetris/Imagenes/fondo_ranking.jfif")
    imagen_fondo_ranking= pygame.transform.scale(imagen_fondo_ranking,(500,620))

    fuente_texto_titulo = pygame.font.SysFont("Times New Roman", 53)
    texto_titulo = fuente_texto_titulo.render("·Ranking Top 5· ", True, "Blue")

    lista_tupla_datos_juego = funciones_data_base.obtener_datos_db("C:/Users/jazmi/Desktop/Progra y labo UTN 2023/Programación 1er Cuatri/data_base_tetris.db")

    pantalla.blit(imagen_fondo_ranking, [0,0])
    pantalla.blit(texto_titulo, (70, 80, 50,50))

    espacio_ranking_jugador = 0
    eje_y_jugador= 200

    for elemento in lista_tupla_datos_juego:
        nombre_jugador = elemento[0]
        puntaje_jugador = elemento[1]

        fuente_texto_puntaje = pygame.font.SysFont("Times New Roman",35)
        texto_puntaje = fuente_texto_puntaje.render(puntaje_jugador, True, "Black")

        fuente_texto_nombre = pygame.font.SysFont("Times New Roman", 35)
        texto_nombre = fuente_texto_nombre.render(nombre_jugador.upper(), True, "Black")
        
        pantalla.blit(texto_puntaje, [400, eje_y_jugador+ espacio_ranking_jugador])
        pantalla.blit(texto_nombre, [50, eje_y_jugador+ espacio_ranking_jugador])
        espacio_ranking_jugador += 85
    
    correr_juego = True

    while correr_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                correr_juego = False

        pygame.display.flip()
    pygame.quit()