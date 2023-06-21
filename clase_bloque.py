from clase_cuadricula import Cuadricula
from clase_posicion import Posicion
import pygame

class Bloque:
    def __init__(self, id) -> None:
        self.id = id
        self.celdas = {}
        self.tamaño_celda = 30
        self.desplazamiento_filas = 0
        self.desplazamiento_columnas = 0
        self.estado_rotacion = 0
        self.colores = Cuadricula.obtener_colores_celdas(self)

    def mover_bloque(self, filas, columnas):
        self.desplazamiento_filas += filas
        self.desplazamiento_columnas += columnas

    def obtener_posicion_celdas(self):
        azulejos = self.celdas[self.estado_rotacion]
        azulejos_movidos = []
        for posicion in azulejos:
            posicion = Posicion(posicion.fila + self.desplazamiento_filas, posicion.columna + self.desplazamiento_columnas)
            azulejos_movidos.append(posicion)
        return azulejos_movidos
    
    def rotacion_bloque(self):
        """
        Recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos

        Esta función va a hacer que el estado de rotación vaya incrementando de a un valor. Cuando este valor
        alcanza la longitud de los estados maximos de rotación en el bloque, se reinicia a 0.
        """
        self.estado_rotacion += 1
        if self.estado_rotacion == len(self.celdas):
            self.estado_rotacion = 0
    
    def deshacer_rotacion(self):
        """
        Recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos

        Esta función se encarga de restarle de a un valor, el estado de rotación de un bloque.
        · Si el estado de rotación ya era 0, vuelve al estado anterior a 0, lo que sería el último estado.
        """
        self.estado_rotacion -= 1
        if self.estado_rotacion == 0:
            self.estado_rotacion = len(self.celdas) - 1

    def draw(self, pantalla, siguiente_bloque_x, siguiente_bloque_y):
        azulejos = self.obtener_posicion_celdas()
        for azulejo in azulejos:
            azulejo_rect = pygame.Rect(siguiente_bloque_x + azulejo.columna * self.tamaño_celda, 
                siguiente_bloque_y + azulejo.fila * self.tamaño_celda,
                self.tamaño_celda - 1, self.tamaño_celda -1)
            pygame.draw.rect(pantalla, self.colores[self.id], azulejo_rect)
