import sqlite3

def conectar():
    # Esto crea un archivo minesys.db en la carpeta del proyecto
    conexion = sqlite3.connect("minesys.db")
    return conexion