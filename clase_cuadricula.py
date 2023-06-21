import pygame

class Cuadricula:
    def __init__(self) -> None:
        self.filas = 20 
        self.columnas = 10
        self.tamaño_celda = 30
        self.cuadricula = [[0 for j in range(self.columnas)] for i in range(self.filas)]
        self.colores = self.obtener_colores_celdas()

    def imprimir_cuadricula(self):
        """
        recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos

        Esta función no se llamará en el juego, pero sirve para previsualizar en la terminal 
        las filas y columnas en formato de matriz (matriz nula, pq los valores inicializados son en 0)
        """
        for fila in range(self.filas):
            for columna in range(self.columnas):
                print(self.cuadricula[fila][columna], end = " ") # end ="" --> indica que el carácter final debe identificarse con un espacio en blanco y no con una nueva línea 
            print()

    def obtener_colores_celdas(self):
        """
        Recibe como parámetro:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos
        Esta función contiene una lista con colores cuyos valores son en formato RGB (Red, Green, Blue).
        · Retorna una lista con dichos colores.
        """
        COLOR_ANTICELDA = (161, 161, 247)
        NARANJA = (214, 153, 92) 
        AMARILLO = (214, 214, 92)
        FUCSIA = (214, 92, 214) 
        VERDE = (92, 214, 92) 
        ROJO = (255, 102, 102)
        VIOLETA = (153, 51, 255)
        AZUL = (0, 138, 230)

        return [COLOR_ANTICELDA, NARANJA, AMARILLO, FUCSIA, VERDE, ROJO, VIOLETA, AZUL]
    
    def verificar_bloques_dentro(self, fila, columna):
        """
        Recibe como parámetros:
        - self: parámetro propio de cualquier función creada por el usuario para inicializar sus atributos
        - fila: dato de tipo entero que representa el valor de una fila en la cuadrícula
        - columna: dato de tipo entero que representa el valor de una columna en la cuadrícula

        Esta función se encarga de comprobar que cada bloque permanezca completo dentro de la cuadrícula.
        Si es así, retornará True; caso contrario, retornará False.
        """
        if fila >= 0 and fila < self.filas and columna >= 0 and columna < self.columnas:
            return True
        return False
    
    def verificar_celda_vacia(self, fila, columna):
        if self.cuadricula[fila][columna] == 0:
            return True
        return False
    
    def verificar_filas_llenas(self, fila):
        for columna in range(self.columnas):
            if self.cuadricula[fila][columna] == 0:
                return False
        return True
    
    def limpiar_fila(self, fila):
        for columna in range(self.columnas):
            self.cuadricula[fila][columna] = 0

    def mover_fila_abajo(self, fila, filas):
        for columna in range(self.columnas):
            self.cuadricula[fila+filas][columna] = self.cuadricula[fila][columna]
            self.cuadricula[fila][columna] = 0

    def limpiar_filas_llenas(self):
        completado = 0
        for fila in range(self.filas -1, 0, -1):
            if self.verificar_filas_llenas(fila):
                self.limpiar_fila(fila)
                completado += 1
            elif completado > 0:
                self.mover_fila_abajo(fila, completado)
        return completado
    
    def resetear_cuadricula(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                self.cuadricula[fila][columna] = 0

    def draw(self, pantalla):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                valor_celda = self.cuadricula[fila][columna]
                celda_rectangulo = pygame.Rect(columna*self.tamaño_celda +11, fila*self.tamaño_celda +11,
                self.tamaño_celda -1, self.tamaño_celda -1) # (x, y, ancho, alto)
                pygame.draw.rect(pantalla, self.colores[valor_celda], celda_rectangulo) # (superficie, color, coordenadas del rect)
