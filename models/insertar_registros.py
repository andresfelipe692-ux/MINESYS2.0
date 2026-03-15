import sqlite3
import os

# Ruta absoluta para la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "minesys.db")

def conectar():
    return sqlite3.connect(DB_PATH)

def crear_tablas():
    con = conectar()
    cur = con.cursor()

    # Yacimientos
    cur.execute("""
    CREATE TABLE IF NOT EXISTS yacimientos (
        codigo TEXT PRIMARY KEY,
        nombre TEXT,
        ubicacion TEXT,
        mineral TEXT,
        metodo TEXT,
        fecha TEXT,
        reservas REAL,
        vida TEXT,
        estado TEXT
    )
    """)

    # Maquinaria
    cur.execute("""
    CREATE TABLE IF NOT EXISTS maquinaria (
        serie TEXT PRIMARY KEY,
        tipo TEXT,
        marca TEXT,
        modelo TEXT,
        capacidad TEXT,
        anio INTEGER,
        horas REAL,
        combustible TEXT,
        ubicacion TEXT,
        estado TEXT
    )
    """)

    # Empleados
    cur.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id TEXT PRIMARY KEY,
        nombre TEXT,
        cargo TEXT,
        edad INTEGER,
        telefono TEXT,
        correo TEXT,
        direccion TEXT,
        fecha_ingreso TEXT,
        salario REAL
    )
    """)

    # Seguridad
    cur.execute("""
    CREATE TABLE IF NOT EXISTS seguridad (
        id TEXT PRIMARY KEY,
        zona TEXT,
        riesgo TEXT,
        descripcion TEXT,
        fecha TEXT,
        responsable TEXT,
        accion TEXT,
        estado TEXT
    )
    """)

    con.commit()
    con.close()

def insertar_registros():
    con = conectar()
    cur = con.cursor()

    # Yacimientos
    yacimientos = [
        ("Y001","La Esperanza","Envigado","Oro","Cielo Abierto","2026-01-01",1200,"10 años","Activo"),
        ("Y002","El Dorado","Medellin","Plata","Subterráneo","2025-05-15",800,"8 años","Activo"),
        ("Y003","San Juan","Rionegro","Cobre","Cielo Abierto","2024-03-20",1500,"12 años","Activo"),
        ("Y004","Santa Marta","Itagui","Hierro","Subterráneo","2023-07-10",600,"5 años","Inactivo"),
        ("Y005","La Fortuna","Sabaneta","Oro","Cielo Abierto","2022-09-05",900,"7 años","Activo"),
        ("Y006","El Progreso","Bello","Plomo","Subterráneo","2021-11-30",400,"4 años","Activo")
    ]
    cur.executemany("INSERT OR IGNORE INTO yacimientos VALUES (?,?,?,?,?,?,?,?,?)", yacimientos)

    # Maquinaria
    maquinaria = [
        ("M001","Excavadora","Caterpillar","320","20 Ton","2019",1500,"Diesel","La Esperanza","Activo"),
        ("M002","Camion","Volvo","FH16","25 Ton","2020",1200,"Diesel","El Dorado","Activo"),
        ("M003","Perforadora","Atlas Copco","DM45","15 Ton","2018",1800,"Diesel","San Juan","Activo"),
        ("M004","Bulldozer","Komatsu","D85","30 Ton","2017",2000,"Diesel","Santa Marta","Inactivo"),
        ("M005","Grúa","Liebherr","LTM 1100","10 Ton","2021",900,"Diesel","La Fortuna","Activo"),
        ("M006","Retroexcavadora","JCB","3CX","5 Ton","2022",600,"Diesel","El Progreso","Activo")
    ]
    cur.executemany("INSERT OR IGNORE INTO maquinaria VALUES (?,?,?,?,?,?,?,?,?,?)", maquinaria)

    # Empleados
    empleados = [
        ("E001","Juan Perez","Ingeniero","35","3101234567","juan@mail.com","Cra 10 #20-30","2020-01-01",4500),
        ("E002","Ana Gomez","Operario","28","3107654321","ana@mail.com","Cra 15 #25-40","2019-03-15",3200),
        ("E003","Luis Ramirez","Supervisor","40","3109876543","luis@mail.com","Cra 5 #30-50","2018-07-10",5000),
        ("E004","Maria Torres","Contadora","33","3101112222","maria@mail.com","Cra 7 #22-35","2021-05-05",4200),
        ("E005","Carlos Soto","Mecánico","30","3103334444","carlos@mail.com","Cra 12 #18-28","2022-09-12",3500),
        ("E006","Laura Ruiz","Geólogo","29","3105556666","laura@mail.com","Cra 20 #30-45","2023-02-20",4000)
    ]
    cur.executemany("INSERT OR IGNORE INTO empleados VALUES (?,?,?,?,?,?,?,?,?)", empleados)

    # Seguridad
    seguridad = [
        ("S001","Zona A","Alto","Derrumbe potencial","2026-03-01","Juan Perez","Señalización","Activo"),
        ("S002","Zona B","Medio","Gases tóxicos","2026-02-15","Ana Gomez","Monitoreo","Activo"),
        ("S003","Zona C","Bajo","Inundación","2026-01-20","Luis Ramirez","Evacuación","Activo"),
        ("S004","Zona D","Alto","Explosión","2025-12-10","Maria Torres","Capacitación","Activo"),
        ("S005","Zona E","Medio","Incendio","2025-11-05","Carlos Soto","Inspección","Activo"),
        ("S006","Zona F","Bajo","Caída objetos","2025-10-01","Laura Ruiz","Señalización","Activo")
    ]
    cur.executemany("INSERT OR IGNORE INTO seguridad VALUES (?,?,?,?,?,?,?,?)", seguridad)

    con.commit()
    con.close()

if __name__ == "__main__":
    crear_tablas()
    insertar_registros()
    print("Base de datos creada y registros insertados correctamente.")