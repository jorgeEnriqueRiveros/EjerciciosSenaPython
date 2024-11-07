salir = True
opcion_menu = 0
while salir:
    opcion_menu = int(input(f'''
    Por favor ingrese una menu_option del menu
    1. Zapatos
    2. Patalones
    3. Camisas
    4. Bolsos
    5. Salir
    : '''))
    if opcion_menu == 1:
        print("Opcion 1 del menu: ")
    elif opcion_menu == 2:
        print("Opcion 2 del menu: ")
    elif opcion_menu == 3:
        print("Opcion 3 del menu: ")
    elif opcion_menu == 4:
        print("Opcion 4 del menu: ")
    elif opcion_menu == 5:
        print("Opcion 5 del menu: Salir ")
        salir = False
    else:
        print("Ingresaste una menu_option no valida")