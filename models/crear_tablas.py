from database.conexion import conectar

class DatabaseManager:
    """Clase encargada de la gestión y creación de la base de datos."""

    def __init__(self):
        self.con = None

    def crear_tablas(self):
        """Crea las tablas necesarias para el sistema MINESYS si no existen."""
        try:
            self.con = conectar()
            cursor = self.con.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")

            # Crear tablas básicas si no existen
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS yacimientos (
                codigo TEXT PRIMARY KEY, nombre TEXT NOT NULL, ubicacion TEXT,
                mineral TEXT, metodo TEXT, fecha TEXT, reservas REAL,
                vida TEXT, estado TEXT
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS maquinaria (
                serie TEXT PRIMARY KEY, tipo TEXT NOT NULL, marca TEXT,
                modelo TEXT, capacidad TEXT, anio INTEGER, horas REAL,
                combustible TEXT, ubicacion TEXT, estado TEXT
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id TEXT PRIMARY KEY, nombre TEXT NOT NULL, cargo TEXT,
                edad INTEGER, telefono TEXT, correo TEXT, direccion TEXT,
                fecha_ingreso TEXT, salario REAL
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS seguridad (
                id TEXT PRIMARY KEY, zona TEXT NOT NULL, riesgo TEXT,
                descripcion TEXT, fecha TEXT, responsable TEXT, accion TEXT, estado TEXT
            )
            """)

            self.con.commit()

            # --- PARTE PROFESIONAL: MIGRACIÓN DE COLUMNAS PARA IMÁGENES ---
            # Si las tablas existen de antes, les agregamos la columna de imagen
            tablas_y_columnas = {
                "yacimientos": "ruta_imagen",
                "maquinaria": "ruta_imagen",
                "empleados": "ruta_foto",
                "seguridad": "ruta_evidencia"
            }

            for tabla, columna in tablas_y_columnas.items():
                cursor.execute(f"PRAGMA table_info({tabla})")
                columnas_actuales = [col[1] for col in cursor.fetchall()]

                # Si la columna no existe en la tabla vieja, la creamos
                if columna not in columnas_actuales:
                    cursor.execute(f"ALTER TABLE {tabla} ADD COLUMN {columna} TEXT")
                    print(f"Columna '{columna}' añadida con éxito a la tabla '{tabla}'.")

            self.con.commit()
            print("Estructura de la base de datos verificada y actualizada correctamente.")

        except Exception as e:
            print(f"Error al crear o actualizar las tablas: {e}")
        finally:
            if self.con:
                self.con.close()

if __name__ == "__main__":
    manager = DatabaseManager()
    manager.crear_tablas()