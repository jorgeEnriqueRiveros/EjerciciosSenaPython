# Conjuntos de libros de las bibliotecas
library_set_one = {"El Principito", "1984", "Cien Años de Soledad", "Don Quijote", "El Hobbit"}
library_set_two = {"El Hobbit", "Orgullo y Prejuicio", "1984", "Drácula", "Cien Años de Soledad"}

# Simulación de un "do-while"
# Se usa un bucle infinito con la condición de romperlo manualmente para simular un "do-while"
while True:
    # Muestra el menú de opciones al usuario
    print(f'\nMenú de opciones: ')
    print(f'1. Mostrar todos los libros que tienen ambas bibliotecas (sin duplicados): ')
    print(f'2. Mostrar los libros que están presentes en ambas bibliotecas: ')
    print(f'3. Mostrar los libros que están en la biblioteca 1 pero no en la biblioteca 2: ')
    print(f'4. Mostrar los libros que están en la biblioteca 2 pero no en la biblioteca 1: ')
    print(f'5. Mostrar los libros que están en las bibliotecas, pero no en ambas al mismo tiempo: ')
    print(f'6. Salir del programa')

    # Solicita al usuario una opción del menú
    menu_library = int(input(f'Elige una opción del menú: \n'))

    # Verifica qué opción eligió el usuario
    if menu_library == 1:
        # Opción 1: Unir ambos conjuntos de libros y mostrar todos los libros sin duplicados
        total_books = library_set_one.union(library_set_two)
        print(f'Todos los libros en ambas bibliotecas: \n'
              f'{total_books}')
    elif menu_library == 2:
        # Opción 2: Mostrar los libros que están en ambas bibliotecas (intersección)
        common_books = library_set_one.intersection(library_set_two)
        print(f'Libros en ambas bibliotecas: \n'
              f'{common_books}')
    elif menu_library == 3:
        # Opción 3: Mostrar los libros que están en la biblioteca 1, pero no en la biblioteca 2 (diferencia)
        books_only_B1 = library_set_one.difference(library_set_two)
        print(f'Libros solo en la biblioteca 1: \n'
              f'{books_only_B1}')
    elif menu_library == 4:
        # Opción 4: Mostrar los libros que están en la biblioteca 2, pero no en la biblioteca 1 (diferencia)
        books_only_B2 = library_set_two.difference(library_set_one)
        print(f'Libros solo en la biblioteca 2: \n'
              f'{books_only_B2}')
    elif menu_library == 5:
        # Opción 5: Mostrar los libros exclusivos de cada biblioteca (diferencia simétrica)
        exclusive_books = library_set_one.symmetric_difference(library_set_two)
        print(f'Libros exclusivos de una sola biblioteca: \n'
              f'{exclusive_books}')
    elif menu_library == 6:
        # Opción 6: Salir del programa
        print(f'Saliendo del programa ¡Adiós!')
        break  # Rompe el bucle y termina el programa
    else:
        # Mensaje en caso de que la opción no sea válida
        print(f'Opción no válida. Por favor, elige una opción del 1 al 6')