# Listas vacías para almacenar los productos y las compras
list_products = []
shopping_list = []

def show_menu():
    """Muestra el menú principal y captura la opción seleccionada por el usuario."""
    print(f'--- MENU PRINCIPAL ---\n'
          f'1. Crear producto\n'
          f'2. Mostrar productos\n'
          f'3. Comprar producto\n'
          f'4. Mostrar factura\n'
          f'5. Salir del menu de compras')
    menu_shopping = int(input(f'Selecciona una opcion del menu de compras:\n'))
    return menu_shopping

def create_product():
    """Solicita datos al usuario para crear un producto y agregarlo a la lista de productos."""
    product_code = int(input(f'Ingresa el codigo del producto:\n'))
    product_name = input(f'Ingresa el nombre del producto:\n')
    product_price = float(input(f'Ingresa el precio del producto:\n'))
    product_quantity = int(input(f'Ingresa la cantidad del producto:\n'))

    # Crear el diccionario con los campos del producto
    product_description = {
        "Codigo del producto": product_code,
        "Nombre del producto": product_name,
        "Precio del producto": product_price,
        "Cantidad del producto": product_quantity
    }

    # Agregar el producto a la lista
    list_products.append(product_description)
    print(f'\nProducto generado con éxito.\n')

def show_products():
    """Muestra todos los productos almacenados en la lista."""
    if not list_products:
        print(f'\nNo hay productos disponibles.\n')
        return
    print(f'\nProductos disponibles:\n')
    for product_description in list_products:
        print(f'Código: {product_description["Codigo del producto"]}, '
              f'Nombre: {product_description["Nombre del producto"]}, '
              f'Precio: {product_description["Precio del producto"]}, '
              f'Cantidad: {product_description["Cantidad del producto"]}\n')

def buy_product():
    """Permite al usuario comprar un producto por código."""
    search_code = int(input(f'\nIngrese el código del producto que desea comprar:\n'))
    for product_description in list_products:
        if product_description["Codigo del producto"] == search_code:
            if product_description["Cantidad del producto"] > 0:
                product_description["Cantidad del producto"] -= 1
                shopping_list.append({
                    "Nombre del producto": product_description["Nombre del producto"],
                    "Precio del producto": product_description["Precio del producto"]
                })
                print(f'\nProducto comprado con éxito.\n')
                return
            else:
                print(f'\nProducto agotado.\n')
                return
    print(f'\nProducto no encontrado.\n')

def show_invoice():
    """Muestra los productos comprados y el total pagado."""
    if not shopping_list:
        print(f'\nNo ha realizado ninguna compra.\n')
        return
    total_purchases = 0
    print(f'\nFactura de compra:')
    for buy_index in shopping_list:
        print(f'Nombre: {buy_index["Nombre del producto"]}, Precio: {buy_index["Precio del producto"]}')
        total_purchases += buy_index["Precio del producto"]
    print(f'\nTotal pagado: {total_purchases}\n')