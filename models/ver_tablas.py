from database.conexion import conectar


class VerificadorTablas:

    def __init__(self):
        # Lista de las tablas que tenemos en el sistema
        self.lista_tablas = ["yacimientos", "maquinaria", "empleados", "seguridad"]

    def obtener_datos(self, nombre_tabla):
        """Funcion para traer los datos de una tabla especifica"""
        try:
            con = conectar()
            cursor = con.cursor()

            # Consultamos todo de la tabla que le pasemos
            cursor.execute(f"SELECT * FROM {nombre_tabla}")
            datos = cursor.fetchall()

            return datos

        except Exception as e:
            print(f"Error al consultar la tabla {nombre_tabla}: {e}")
            return []
        finally:
            if con:
                con.close()

    def imprimir_reporte(self):
        """Funcion para mostrar todo en la consola y verificar"""
        for tabla in self.lista_tablas:
            datos = self.obtener_datos(tabla)
            print(f"\n--- Datos de la tabla: {tabla} ---")

            if not datos:
                print("No hay registros guardados todavia.")
                continue

            # Recorremos e imprimimos cada fila
            for fila in datos:
                print(fila)


if __name__ == "__main__":
    # Creamos el objeto y mandamos a imprimir todo
    visor = VerificadorTablas()
    visor.imprimir_reporte()