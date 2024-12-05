# Importar las funciones desde el módulo functions_product_thirtyeight
from functions_product_thirtyeight import show_menu, create_product, show_products, buy_product, show_invoice

def main():
    """Gestiona el flujo principal del programa."""
    while True:
        menu_shopping = show_menu()
        if menu_shopping == 1:
            create_product()
        elif menu_shopping == 2:
            show_products()
        elif menu_shopping == 3:
            buy_product()
        elif menu_shopping == 4:
            show_invoice()
        elif menu_shopping == 5:
            print(f'\nGracias por tu compra. ¡Adiós!\n')
            break  # Salir del bucle
        else:
            print(f'\nOpción no válida. Por favor, inténtalo de nuevo.\n')

if __name__ == '__main__':
    main()
