# Paso 1: Crear la lista
shopping_list = []

# Paso 2: Agregar elementos a la lista
for i in range(5):
    article_entered = input(f"Ingrese el artículo {i+1} para la lista de compras: ")
    shopping_list.append(article_entered)
# Paso 3: Mostrar la lista
print("\nLista de compras actual:")
print(shopping_list)
# Paso 4: Modificar un artículo
print("\nLista de compras con índices:")
for purchasing_index, article_entered in enumerate(shopping_list):
    print(f"{purchasing_index}: {article_entered}")
modify_index = int(input("\nIngrese el índice del artículo que desea modificar: "))
new_article = input("Ingrese el nuevo artículo: ")
shopping_list[modify_index] = new_article
# Paso 5: Eliminar un artículo
delete_index = int(input("\nIngrese el índice del artículo que desea eliminar: "))
shopping_list.pop(delete_index)

# Paso 6: Mostrar la lista final
print("\nLista de compras final:")
print(shopping_list)