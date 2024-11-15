# Crear una lista vacía
shopping_list = []

# Variable para controlar el menú
shopping_menu = ""

while shopping_menu != "5":
    print("\n--- Menú de Lista de Compras ---")
    print("1. Agregar artículos a la lista")
    print("2. Modificar un artículo de la lista")
    print("3. Eliminar un artículo de la lista")
    print("4. Mostrar la lista de compras")
    print("5. Salir")

    shopping_menu = input("Seleccione una opción: ")

    shopping_list = shopping_list
    if shopping_menu == "1":
        # Agregar artículos a la lista
        print("\nAgregar 5 artículos a la lista de compras:")
        for i in range(5):
            article_index = input(f"Ingrese el artículo {i + 1} para la lista de compras: ")
            shopping_list.append(article_index)
        print("Artículos agregados a la lista de compras.")

    elif shopping_menu == "2":
        # Modificar un artículo de la lista
        if shopping_list:
            print("\nLista de compras con índices:")
            for purchasing_index, article_index in enumerate(shopping_list):
                print(f"{purchasing_index}: {article_index}")

            try:
                modify_index = int(input("\nIngrese el índice del artículo que desea modificar: "))
                if 0 <= modify_index < len(shopping_list):
                    new_article = input("Ingrese el nuevo artículo: ")
                    shopping_list[modify_index] = new_article
                    print("Artículo modificado exitosamente.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            print("La lista de compras está vacía. No hay nada para modificar.")

    elif shopping_menu == "3":
        # Eliminar un artículo de la lista
        if shopping_list:
            print("\nLista de compras con índices:")
            for purchasing_index, article_index in enumerate(shopping_list):
                print(f"{purchasing_index}: {article_index}")

            try:
                delete_index = int(input("\nIngrese el índice del artículo que desea eliminar: "))
                if 0 <= delete_index < len(shopping_list):
                    shopping_list.pop(delete_index)
                    print("Artículo eliminado exitosamente.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            print("La lista de compras está vacía. No hay nada para eliminar.")

    elif shopping_menu == "4":
        # Mostrar la lista de compras
        if shopping_list:
            print("\nLista de compras actual:")
            for purchasing_index, article_index in enumerate(shopping_list):
                print(f"{purchasing_index}: {article_index}")
        else:
            print("La lista de compras está vacía.")

    elif shopping_menu == "5":
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")
