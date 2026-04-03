from modulos.mostrar import mostrar_tabla


def menu():
    while True:
        print("\n===== SISTEMA MINESYS =====")
        print("1. Ver tablas")
        print("2. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nTablas disponibles:")
            print("yacimientos")
            print("maquinaria")
            print("empleados")
            print("seguridad")

            tabla = input("\nEscribe el nombre de la tabla: ")
            mostrar_tabla(tabla)

        elif opcion == "2":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


menu()