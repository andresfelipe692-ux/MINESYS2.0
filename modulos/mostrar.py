from database.conexion import conectar


def mostrar_tabla(tabla):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {tabla}")
    registros = cursor.fetchall()
    con.close()

    print(f"\nRegistros de la tabla {tabla}:")
    for r in registros:
        print(r)


if __name__ == "__main__":
    for tabla in ["yacimientos", "maquinaria", "empleados", "seguridad"]:
        mostrar_tabla(tabla)