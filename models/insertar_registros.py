from database.conexion import conectar

def poblar_datos_iniciales():
    """Inserta registros de prueba especificando las columnas para evitar errores de conteo."""
    try:
        con = conectar()
        cur = con.cursor()

        print("Insertando registros de prueba...")

        # 1. Yacimientos (Especificamos las 9 columnas de negocio)
        yacimientos = [
            ("Y001","La Esperanza","Envigado","Oro","Cielo Abierto","2026-01-01",1200.0,"10 años","Activo"),
            ("Y002","El Dorado","Medellin","Plata","Subterráneo","2025-05-15",800.0,"8 años","Activo"),
            ("Y003","San Juan","Rionegro","Cobre","Cielo Abierto","2024-03-20",1500.0,"12 años","Activo")
        ]
        cur.executemany("""
            INSERT OR IGNORE INTO yacimientos 
            (codigo, nombre, ubicacion, mineral, metodo, fecha, reservas, vida, estado) 
            VALUES (?,?,?,?,?,?,?,?,?)
        """, yacimientos)

        # 2. Maquinaria (Especificamos las 10 columnas de negocio)
        maquinaria = [
            ("M001","Excavadora","Caterpillar","320","20 Ton",2019,1500.0,"Diesel","La Esperanza","Activo"),
            ("M002","Camion","Volvo","FH16","25 Ton",2020,1200.0,"Diesel","El Dorado","Activo"),
            ("M003","Perforadora","Atlas Copco","DM45","15 Ton",2018,1800.0,"Diesel","San Juan","Activo")
        ]
        cur.executemany("""
            INSERT OR IGNORE INTO maquinaria 
            (serie, tipo, marca, modelo, capacidad, anio, horas, combustible, ubicacion, estado) 
            VALUES (?,?,?,?,?,?,?,?,?,?)
        """, maquinaria)

        # 3. Empleados (Especificamos las 9 columnas de negocio)
        empleados = [
            ("E001","Juan Perez","Ingeniero",35,"3101234567","juan@mail.com","Cra 10 #20-30","2020-01-01",4500.0),
            ("E002","Ana Gomez","Operario",28,"3107654321","ana@mail.com","Cra 15 #25-40","2019-03-15",3200.0),
            ("E003","Luis Ramirez","Supervisor",40,"3109876543","luis@mail.com","Cra 5 #30-50","2018-07-10",5000.0)
        ]
        cur.executemany("""
            INSERT OR IGNORE INTO empleados 
            (id, nombre, cargo, edad, telefono, correo, direccion, fecha_ingreso, salario) 
            VALUES (?,?,?,?,?,?,?,?,?)
        """, empleados)

        # 4. Seguridad (Especificamos las 8 columnas de negocio)
        seguridad = [
            ("S001","Zona A","Alto","Derrumbe potencial","2026-03-01","Juan Perez","Señalización","Activo"),
            ("S002","Zona B","Medio","Gases tóxicos","2026-02-15","Ana Gomez","Monitoreo","Activo"),
            ("S003","Zona C","Bajo","Inundación","2026-01-20","Luis Ramirez","Evacuación","Activo")
        ]
        cur.executemany("""
            INSERT OR IGNORE INTO seguridad 
            (id, zona, riesgo, descripcion, fecha, responsable, accion, estado) 
            VALUES (?,?,?,?,?,?,?,?)
        """, seguridad)

        con.commit()
        print("¡Perfecto! Registros de prueba insertados exitosamente.")

    except Exception as e:
        print(f"Error al insertar registros: {e}")
    finally:
        if con:
            con.close()

if __name__ == "__main__":
    poblar_datos_iniciales()