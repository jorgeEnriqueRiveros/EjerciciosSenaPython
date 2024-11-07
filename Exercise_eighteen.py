exit_menu = False  # Variable para controlar la salida del menú

while not exit_menu:
    # Menú principal
    print("\n--- Menú Principal ---")
    print("1. Carnes")
    print("2. Hamburguesas")
    print("3. Bebidas")
    print("4. Postres")
    print("5. Salir")

    menu_option = int(input("Elige una opción (1-5): "))

    if menu_option == 1:
        while True:
            # Submenú Carnes
            print("\n--- Submenú Carnes ---")
            print("1. Pollo")
            print("2. Res")
            print("3. Pescado")
            print("4. Volver al menú principal")
            print("5. Salir")

            meat_option = int(input("Elige una opción (1-5): "))
            if meat_option == 1:
                print("Has elegido Pollo")
            elif meat_option == 2:
                print("Has elegido Res")
            elif meat_option == 3:
                print("Has elegido Pescado")
            elif meat_option == 4:
                break  # Volver al menú principal
            elif meat_option == 5:
                print("Saliendo...")
                exit_menu = True  # Cambiar exit_menu a True para salir
                break  # Salir del submenú
            else:
                print("Opción inválida.")

    elif menu_option == 2:
        while True:
            # Submenú Hamburguesas
            print("\n--- Submenú Hamburguesas ---")
            print("1. Hamburguesa Clásica")
            print("2. Hamburguesa BBQ")
            print("3. Hamburguesa Vegetariana")
            print("4. Volver al menú principal")
            print("5. Salir")

            burger_option = int(input("Elige una opción (1-5): "))
            if burger_option == 1:
                print("Has elegido Hamburguesa Clásica")
            elif burger_option == 2:
                print("Has elegido Hamburguesa BBQ")
            elif burger_option == 3:
                print("Has elegido Hamburguesa Vegetariana")
            elif burger_option == 4:
                break  # Volver al menú principal
            elif burger_option == 5:
                print("Saliendo...")
                exit_menu = True  # Cambiar exit_menu a True para salir
                break  # Salir del submenú
            else:
                print("Opción inválida.")

    elif menu_option == 3:
        while True:
            # Submenú Bebidas
            print("\n--- Submenú Bebidas ---")
            print("1. Agua")
            print("2. Refresco")
            print("3. Jugo")
            print("4. Volver al menú principal")
            print("5. Salir")

            drinks_option = int(input("Elige una opción (1-5): "))
            if drinks_option == 1:
                print("Has elegido Agua")
            elif drinks_option == 2:
                print("Has elegido Refresco")
            elif drinks_option == 3:
                print("Has elegido Jugo")
            elif drinks_option == 4:
                break  # Volver al menú principal
            elif drinks_option == 5:
                print("Saliendo...")
                exit_menu = True  # Cambiar exit_menu a True para salir
                break  # Salir del submenú
            else:
                print("Opción inválida.")

    elif menu_option == 4:
        while True:
            # Submenú Postres
            print("\n--- Submenú Postres ---")
            print("1. Pastel")
            print("2. Helado")
            print("3. Flan")
            print("4. Volver al menú principal")
            print("5. Salir")

            dessert_option = int(input("Elige una opción (1-5): "))
            if dessert_option == 1:
                print("Has elegido Pastel")
            elif dessert_option == 2:
                print("Has elegido Helado")
            elif dessert_option == 3:
                print("Has elegido Flan")
            elif dessert_option == 4:
                break  # Volver al menú principal
            elif dessert_option == 5:
                print("Saliendo...")
                exit_menu = True  # Cambiar exit_menu a True para salir
                break  # Salir del submenú
            else:
                print("Opción inválida.")

    elif menu_option == 5:
        print("Saliendo del programa...")
        exit_menu = True  # Cambiar exit_menu a True para salir

    else:
        print("Opción inválida.")