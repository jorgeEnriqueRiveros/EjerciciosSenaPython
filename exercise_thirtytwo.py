# Inicializa una lista vacía para almacenar los productos del inventario
inventory_list = []

# Bucle infinito para simular un menú interactivo que continúa hasta que el usuario elige salir
while True:  # Simulación de un do-while
    # Muestra el menú de opciones al usuario
    print("\n--- Menú de Opciones ---")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Buscar un producto")
    print("4. Calcular valor del inventario")
    print("5. Salir")

    # Solicita al usuario que seleccione una opción del menú
    menu_product = int(input(f'Selecciona una opcion: '))

    # Opción 1: Agregar un producto al inventario
    if menu_product == 1:
        print(f'\n---Agrega un producto:---')
        # Solicita el nombre, precio y cantidad del producto al usuario
        product_name = input(f'Nombre del producto: ')
        product_price = int(input(f'Precio del producto: '))
        product_quantity = float(input(f'Cantidad del producto: '))
        # Crea una tupla con los datos del producto y la agrega a la lista del inventario
        tuple_product = (product_name, product_price, product_quantity)
        inventory_list.append(tuple_product)
        # Confirma que el producto fue agregado correctamente
        print(f"El producto {product_name} agregado correctamente.")

    # Opción 2: Listar todos los productos en el inventario
    elif menu_product == 2:
        print(f'\n---Lista de productos:---')
        # Verifica si el inventario está vacío
        if not inventory_list:
            print(f'Producto no encontrado')
        else:
            # Recorre e imprime cada producto con su índice, nombre, precio y cantidad
            for i, product_value in enumerate(inventory_list):
                print(f'{i + 1}. Producto: {product_value[0]}, Precio: {product_value[1]}, Cantidad de productos: {product_value[2]}')

    # Opción 3: Buscar un producto por su nombre
    elif menu_product == 3:
        print(f'\n---Buscar un producto:---')
        # Solicita el nombre del producto que se desea buscar
        product_name = input(f'Ingresa un producto a buscar: ').strip().lower()
        product_found = False  # Bandera para verificar si el producto fue encontrado
        # Recorre la lista buscando el producto
        for product_value in inventory_list:
            if product_value[0].lower() == product_name:
                # Si se encuentra, muestra los detalles del producto
                print(f'Producto encontrado: \n'
                      f'nombre del producto: \n'
                      f'{product_value[0]}, precio del producto: {product_value[1]}, cantidad del producto: {product_value[2]}')
                product_found = True
                break
        # Si no se encuentra el producto, muestra un mensaje correspondiente
        if not product_found:
            print(f'Producto no encontrado')

    # Opción 4: Calcular el valor total del inventario
    elif menu_product == 4:
        print(f'\n---Calcular valor total del inventario')
        # Verifica si el inventario está vacío
        if not inventory_list:
            print(f'El inventario esta vacio, el valor total es 0')
        else:
            # Calcula el valor total del inventario multiplicando precio y cantidad de cada producto
            inventory_total = sum(total_product[1] * total_product[2] for total_product in inventory_list)  # Usando comprensión de listas
            print(f"El valor total del inventario es: {inventory_total:.2f} pesos")

    # Opción 5: Salir del programa
    elif menu_product == 5:
        # Imprime un mensaje de despedida y termina el bucle
        print(f'Saliendo del programa. ¡Hasta luego!')
        break

    # Manejo de una opción inválida ingresada por el usuario
    else:
        print(f'Opcion no valida. Intente de nuevo')