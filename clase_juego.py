from clase_cuadricula import Cuadricula
from bloques_ok import *
from clase_bloque import *
import random
import pygame


class Juego:
    def __init__(self):
        """
        Esta es una función de inicialización de atributos para nuestra clase creada, por lo que para ello 
        necesitaremos como parámetro -self-, y posteriormente agregarlo a las demás funciones que necesitemos crear.
        """
        self.cuadricula = Cuadricula()
        self.bloques = [Bloque_I(), Bloque_J(), Bloque_L(), Bloque_O(), Bloque_S(), Bloque_T(), Bloque_Z()]
        self.bloque_actual = self.obtener_bloque_aleatorio()
        self.siguiente_bloque = self.obtener_bloque_aleatorio()
        self.juego_terminado = False
        self.puntaje = 0

        # SONIDOS
        self.sonido_rotacion = pygame.mixer.Sound("C:/Users/jazmi/Desktop/Progra y labo UTN 2023/Programación 1er Cuatri/Post 1er parcial/PROYECTO PYGAME/pygame tetris/Sonidos/rotacion.mp3")
        self.sonido_limpiar = pygame.mixer.Sound("C:/Users/jazmi/Desktop/Progra y labo UTN 2023/Programación 1er Cuatri/Post 1er parcial/PROYECTO PYGAME/pygame tetris/Sonidos/limpiar.mp3")
        self.musica_fondo = pygame.mixer.Sound("C:/Users/jazmi/Desktop/Progra y labo UTN 2023/Programación 1er Cuatri/Post 1er parcial/PROYECTO PYGAME/pygame tetris/Sonidos/background.mp3")
        self.musica_fondo.set_volume(0.2) 
        self.musica_fondo.play(-1) # Para que el sonido se reproduzca en loop por tiempo indeterminado


    def actualizar_puntaje(self, filas_limpiadas):
        """
        Recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos
        - filas_limpiadas: cantidad de filas de bloques que se completaron

        Según la cantidad de filas que se completaron -recibidas por parámetro-, el puntaje se irá acumulando 
        y sumando en las cantidades determinadas.
        """
        if filas_limpiadas == 1:
            self.puntaje += 100
        elif filas_limpiadas == 2:
            self.puntaje += 300
        elif filas_limpiadas == 3:
            self.puntaje += 500


    def obtener_bloque_aleatorio(self):
        """
        Recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos

        ·Si la longitud de la lista de bloques es 0, es decir, no contiene elementos, se rellena lista nuevamente.
        ·El objeto bloque representa cualquier elemento de la lista de bloques elegida aleatoriamente. Cada vez
        que un elemento sea elegido, se removerá de la lista.

        Finalmente, se retorna el objeto: Bloque
        """
        if len(self.bloques) == 0:
            self.bloques = [Bloque_I(), Bloque_J(), Bloque_L(), Bloque_O(), Bloque_S(), Bloque_T(), Bloque_Z()]
        bloque = random.choice(self.bloques)
        self.bloques.remove(bloque)
        return bloque

#--------------------------------------------------------#
    """
    def mover_-direccion-():
    Reciben como parámetro:  
    - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos

    ·En estas funciones se indica el sentido de movimiento de los bloques, 
    asegurándose de que cada uno se mueva dentro de la cuadrícula.
    """
    def mover_izquierda(self):
        self.bloque_actual.mover_bloque(0,-1)
        if self.bloque_dentro() == False or self.encajar_bloque() == False:
            self.bloque_actual.mover_bloque(0,1)

    def mover_derecha(self):
        self.bloque_actual.mover_bloque(0,1)
        if self.bloque_dentro() == False or self.encajar_bloque() == False:
            self.bloque_actual.mover_bloque(0,-1)

    def mover_abajo(self):
        self.bloque_actual.mover_bloque(1,0)
        if self.bloque_dentro() == False or self.encajar_bloque() == False:
            self.bloque_actual.mover_bloque(-1,0)
            self.bloquear_bloque()
#--------------------------------------------------------#

    def bloquear_bloque(self):
        """
        Recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos
        · El objeto azulejos representa las celdas de cada bloque que se va mostrando en pantalla.
        
        """
        azulejos = self.bloque_actual.obtener_posicion_celdas()
        for posicion in azulejos:
            self.cuadricula.cuadricula[posicion.fila][posicion.columna] = self.bloque_actual.id
        self.bloque_actual = self.siguiente_bloque
        self.siguiente_bloque = self.obtener_bloque_aleatorio()
        filas_limpiadas = self.cuadricula.limpiar_filas_llenas()
        if filas_limpiadas > 0:
            self.sonido_limpiar.play()
            self.actualizar_puntaje(filas_limpiadas)
        if self.encajar_bloque() == False:
            self.juego_terminado = True

    def resetear_juego(self):
        """
        Recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos

        ·Esta función reestablece los valores dentro del juego.
        """
        self.cuadricula.resetear_cuadricula()
        self.bloques = [Bloque_I(), Bloque_J(), Bloque_L(), Bloque_O(), Bloque_S(), Bloque_T(), Bloque_Z()]
        self.bloque_actual = self.obtener_bloque_aleatorio()
        self.siguiente_bloque = self.obtener_bloque_aleatorio()
        self.puntaje = 0

    def encajar_bloque(self):
        # Ver si el bloque está encima de una celda vacía de la cuadrícula o no.
        azulejos = self.bloque_actual.obtener_posicion_celdas()
        for azulejo in azulejos:
            if self.cuadricula.verificar_celda_vacia(azulejo.fila, azulejo.columna) == False:
                return False
        return True

    def rotar_bloque(self):
        """
        Recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos

        ·Esta función se encarga de simular el movimiento de rotación de los bloques ,reproduciendo además, un sonido en cada vez.
        ·Cuando el bloque ya encajó entre los demás, este no puede rotar.
        """
        self.bloque_actual.rotacion_bloque()
        if self.bloque_dentro() == False or self.encajar_bloque() == False:
            self.bloque_actual.deshacer_rotacion()
        else:
            self.sonido_rotacion.play()

    def bloque_dentro(self):
        # bloque dentro de la cuadricula
        azulejos = self.bloque_actual.obtener_posicion_celdas()
        for azulejo in azulejos:
            if self.cuadricula.verificar_bloques_dentro(azulejo.fila, azulejo.columna) == False:
                return False
        return True
        
    def draw(self, pantalla):
        """
        Recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos
        - pantalla: dimensiones de la ventana del programa

        Esta función dibuja la cuadrícula y los bloques del juego, tanto los que bajan en la cuadrícula,
        como los que están primeramente en el contenedor "Siguiente bloque"(*)
        (*) Para los bloques "O" e "I" en el contenedor "siguiente", las coordenadas de posición fueron cambiadas ligeramente
        para que "estén centradas". 
        """
        self.cuadricula.draw(pantalla)
        self.bloque_actual.draw(pantalla, 11, 11)

        if self.siguiente_bloque.id == 3: # Bloque "I"
            self.siguiente_bloque.draw(pantalla, 344, 258)

        elif self.siguiente_bloque.id == 2: # Bloque "O"
            self.siguiente_bloque.draw(pantalla,370,280 )
        else:
            self.siguiente_bloque.draw(pantalla, 360, 270)