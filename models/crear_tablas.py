from database.conexion import conectar

def crear_tablas():
    con = conectar()
    cursor = con.cursor()

    # Tabla Yacimientos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS yacimientos(
        codigo TEXT PRIMARY KEY,
        nombre TEXT,
        ubicacion TEXT,
        mineral TEXT,
        metodo TEXT,
        fecha_inicio TEXT,
        reservas TEXT,
        vida_util TEXT,
        estado TEXT
    )
    """)

    # Tabla Maquinaria
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS maquinaria(
        serie TEXT PRIMARY KEY,
        tipo TEXT,
        marca TEXT,
        modelo TEXT,
        capacidad TEXT,
        anio TEXT,
        horas TEXT,
        combustible TEXT,
        ubicacion TEXT,
        estado TEXT
    )
    """)

    # Tabla Empleados
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados(
        numero TEXT PRIMARY KEY,
        nombres TEXT,
        apellidos TEXT,
        documento TEXT,
        cargo TEXT,
        especialidad TEXT,
        turno TEXT,
        fecha TEXT
    )
    """)

    # Tabla Seguridad
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS seguridad(
        codigo TEXT PRIMARY KEY,
        fecha TEXT,
        zona TEXT,
        tipo TEXT,
        inspector TEXT,
        hallazgos TEXT,
        riesgo TEXT,
        acciones TEXT
    )
    """)

    con.commit()
    con.close()
    print("Tablas creadas correctamente")

# Ejecutar
if __name__ == "__main__":
    crear_tablas()