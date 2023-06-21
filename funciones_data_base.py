import sqlite3

def crear_tabla(path):
    with sqlite3.connect(path) as conexion:
        try:
            sentencia = ''' create table jugadores
                            (
                            id integer primary key autoincrement,
                            nombre text,
                            puntaje int
                            )
                            '''
            conexion.execute(sentencia)
            print("Se creo la tabla jugadores")
        except sqlite3.OperationalError:
            print("La tabla jugadores ya existe")

def agregar_datos_a_db(path, nombre, puntaje):
    with sqlite3.connect(path) as conexion:
        try:
            conexion.execute("insert into jugadores(nombre,puntaje) values(?,?)", (nombre, puntaje))
            conexion.commit()
        except: 
                print("Error")

def obtener_datos_db(path):
    with sqlite3.connect(path) as conexion:
        datos = conexion.execute("SELECT * FROM jugadores order by puntaje desc")
        lista_datos = []
        for fila in datos: 
            nombre = fila[1]          
            puntaje = str(fila[2])         
            lista_datos.append((nombre,puntaje))
        return lista_datos