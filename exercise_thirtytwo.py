inventory_list = []

while True:  # Simulación de un do-while
    # Mostrar el menú
    print("\n--- Menú de Opciones ---")
    print("1. Agregar Producto")
    print("2. Listar Productos")
    print("3. Buscar un producto")
    print("4. Calcular valor del inventario")
    print("5. Salir")

    menu_product = int(input(f'Selecciona una opcion: '))

    if menu_product == 1:
        print(f'\n---Agrega un producto:---')
        product_name = input(f'Nombre del producto: ')
        product_price = int(input(f'Precio del producto: '))
        product_quantity = float(input(f'Cantidad del producto: '))
        tuple_product = (product_name, product_price, product_quantity)
        inventory_list.append(tuple_product)
        print(f"El producto {product_name} agregado correctamente.")

    elif menu_product == 2:
        print(f'\n---Lista de productos:---')
        if not inventory_list:
            print(f'Producto no encontrado')
        else:
            for i,product_value in enumerate(inventory_list):
                print(f'{i + 1}. Producto: {product_value[0]}, Precio: {product_value[1]}, Cantidad de productos: {product_value[2]}')

    elif menu_product == 3:
        print(f'\n---Buscar un producto:---')
        product_name = input(f'Ingresa un producto a buscar: ').strip().lower()
        product_found = False
        for product_value in inventory_list:
            if product_value[0] == product_name:
                print(f'Producto encontrado: \n'
                      f'nombre del producto: {product_value[0]}, precio del producto: {product_value[1]}, cantidad del producto: {product_value[2]}')
                product_found = True
                break
        if not product_found:
            print(f'Producto no encontrado')

    elif menu_product == 4:
        print(f'\n---Calcular valor total del inventario')
        if not inventory_list:
            print(f'El inventario esta vacio, el valor total es 0')
        else:
            inventory_total = sum(total_product[1] * total_product[2] for total_product in inventory_list)  # Usando comprensión de listas
            print(f"El valor total del inventario es: {inventory_total:.2f} pesos")

    elif menu_product == 5:
        print(f'Saliendo del programa. ¡Hasta luego!')
        break
    else:
        print(f'Opcion no valida. Intente de nuevo')