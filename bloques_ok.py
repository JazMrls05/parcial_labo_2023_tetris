from clase_bloque import Bloque
from clase_posicion import Posicion

"""
Las siguientes son "clases hijas" de la clase padre "Bloque", las cuales van a representar cada tipo
de bloque en el juego.
· Todas las clases se inicializan con self pasado como parámetro.
· Luego se llaman a los atributos de la clase padre, primero el atributo id, el cual le va a dar un número de identificación a cada bloque.
· Finalmente el atributo celdas, que fue inicializado como diccionario, va a contener en cada clave, las coordenadas de los azulejos de los bloques
para cada caso de rotación
"""
class Bloque_L(Bloque):
    def __init__(self):
        super().__init__(id = 1)
        self.celdas = {
            0: [Posicion(0, 2), Posicion(1,0), Posicion(1,1), Posicion(1,2)],
            1: [Posicion(0,1), Posicion(1,1), Posicion(2,1), Posicion(2,2)],
            2:[Posicion(1,0), Posicion(1,1), Posicion(1,2), Posicion(2,0)],
            3:[Posicion(0,0), Posicion(0,1), Posicion(1,1), Posicion(2,1)]
        }

class Bloque_O(Bloque):
    def __init__(self):
        super().__init__(id = 2)
        self.celdas = {
            0: [Posicion(0, 0), Posicion(0,1), Posicion(1,0), Posicion(1,1)]
        }

class Bloque_I(Bloque):
    def __init__(self):
        super().__init__(id = 3)
        self.celdas = {
            0: [Posicion(1, 0), Posicion(1,1), Posicion(1,2), Posicion(1,3)],
            1: [Posicion(0,2), Posicion(1,2), Posicion(2,2), Posicion(3,2)],
            2:[Posicion(2,0), Posicion(2,1), Posicion(2,2), Posicion(2,3)],
            3:[Posicion(0,1), Posicion(1,1), Posicion(2,1), Posicion(3,1)]
        }

class Bloque_S(Bloque):
    def __init__(self):
        super().__init__(id = 4)
        self.celdas = {
            0: [Posicion(0, 1), Posicion(0,2), Posicion(1,0), Posicion(1,1)],
            1: [Posicion(0,1), Posicion(1,1), Posicion(1,2), Posicion(2,2)],
            2:[Posicion(1,1), Posicion(1,2), Posicion(2,0), Posicion(2,1)],
            3:[Posicion(0,0), Posicion(1,0), Posicion(1,1), Posicion(2,1)]
        }

class Bloque_Z(Bloque): 
    def __init__(self):
        super().__init__(id = 5)
        self.celdas = {
            0: [Posicion(0,0), Posicion(0,1), Posicion(1,1), Posicion(1,2)],
            1: [Posicion(0,2), Posicion(1,1), Posicion(1,2), Posicion(2,1)],
            2:[Posicion(1,0), Posicion(1,1), Posicion(2,1), Posicion(2,2)],
            3:[Posicion(0,1), Posicion(1,0), Posicion(1,1), Posicion(2,0)]
        }

class Bloque_T(Bloque):
    def __init__(self):
        super().__init__(id = 6)
        self.celdas = {
            0: [Posicion(0,1), Posicion(1,0), Posicion(1,1), Posicion(1,2)],
            1: [Posicion(0,1), Posicion(1,1), Posicion(1,2), Posicion(2,1)],
            2:[Posicion(1,0), Posicion(1,1), Posicion(1,2), Posicion(2,1)],
            3:[Posicion(0,1), Posicion(1,0), Posicion(1,1), Posicion(2,1)]
        }

class Bloque_J(Bloque): 
    def __init__(self):
        super().__init__(id = 7)
        self.celdas = {
            0: [Posicion(0,0), Posicion(1,0), Posicion(1,1), Posicion(1,2)],
            1: [Posicion(0,1), Posicion(0,2), Posicion(1,1), Posicion(2,1)],
            2:[Posicion(1,0), Posicion(1,1), Posicion(1,2), Posicion(2,2)],
            3:[Posicion(0,1), Posicion(1,1), Posicion(2,0), Posicion(2,1)]
        }