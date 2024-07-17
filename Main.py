from AdminAutomoviles import AdminAutomoviles


def agregar_automovil_menu(admin):
    while True:
        print("\n   **Agregar Automóvil**")
        admin.agregar_automovil()
        print("Automóvil agregado exitosamente.")
        print("1. Agregar otro automóvil")
        print("2. Regresar al menú principal")
        opc = input("\nSelecciona una opción: ")

        if opc == '1':
            continue
        elif opc == '2':
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


def mostrar_automoviles_menu(admin):
    while True:
        print("\n   **Mostrar Automóviles**")
        print("1. Ver inventario")
        print("2. Buscar automóvil por placa")
        print("3. Regresar al menú principal")
        opc = input("\nSelecciona una opción: ")

        if opc == '1':
            admin.mostrar_automoviles()
        elif opc == '2':
            buscar = input("Ingrese la placa del automóvil que desea buscar: ")
            admin.buscar_automovil(buscar)
        elif opc == '3':
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


def editar_automovil_menu(admin):
    while True:
        print("\n   **Editar Automóvil**")
        admin.editar_automovil()
        print("Automóvil editado exitosamente.")
        print("1. Editar otro automóvil")
        print("2. Regresar al menú principal")
        opc = input("\nSelecciona una opción: ")

        if opc == '1':
            continue
        elif opc == '2':
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


def eliminar_automovil_menu(admin):
    while True:
        print("\n   **Eliminar Automóvil**")
        admin.eliminar_automovil()
        print("Automóvil eliminado exitosamente.")
        print("1. Eliminar otro automóvil")
        print("2. Regresar al menú principal")
        opc = input("\nSelecciona una opción: ")

        if opc == '1':
            continue
        elif opc == '2':
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


def main():
    admin = AdminAutomoviles()

    while True:
        print("\n   **Garage la Z**")
        print("1. Agregar automóvil")
        print("2. Mostrar Automóviles")
        print("3. Buscar automóvil por placa")
        print("4. Editar automóvil")
        print("5. Eliminar automóvil")
        print("6. Salir")
        opc = input("\nSelecciona una opción: ")

        if opc == '1':
            agregar_automovil_menu(admin)
        elif opc == '2':
            mostrar_automoviles_menu(admin)
        elif opc == '3':
            buscar = input("Ingrese la placa del automóvil que desea buscar: ")
            admin.buscar_automovil(buscar)
            print("1. Buscar otro automóvil")
            print("2. Regresar al menú principal")
            opc = input("\nSelecciona una opción: ")

            if opc == '1':
                continue
            elif opc == '2':
                continue
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")
        elif opc == '4':
            editar_automovil_menu(admin)
        elif opc == '5':
            eliminar_automovil_menu(admin)
        elif opc == '6':
            print("Vuelve pronto...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main()
