# Diccionario temporal para almacenar un contacto
from contact_functions import add_contact, view_all_contacts, view_contact_by_position, view_name_and_phone, view_keys, \
    view_names_with_positions, search_by_name, search_by_phone, count_contacts, delete_contact_by_position, \
    delete_contact_by_phone, delete_contact_by_name

contact_dictionary = dict()

# Lista para almacenar los contactos de la agenda
contact_list = []

# Menú interactivo usando un bucle 'while True'
while True:
    print("\nMenú:")
    print("1. Agregar un contacto")
    print("2. Ver todos los contactos")
    print("3. Ver un contacto específico")
    print("4. Ver nombre y teléfono de un contacto específico")
    print("5. Ver claves de los contactos")
    print("6. Ver nombres con posiciones")
    print("7. Buscar por nombre")
    print("8. Buscar por teléfono")
    print("9. Ver cantidad de contactos")
    print("10. Eliminar un contacto por posición")
    print("11. Eliminar un contacto por nombre")
    print("12. Eliminar un contacto por teléfono")
    print("13. Salir")

    # Solicitar al usuario que seleccione una opción del menú
    try:
        notebook_menu = int(input("Selecciona una opción de la agenda: "))
    except ValueError:
        print("Opción no válida. Por favor, ingresa un número.")
        continue

    if notebook_menu == 1:  # Agregar un contacto
        print('Agregar Contacto:\n')
        add_contact(contact_list)

    elif notebook_menu == 2:  # Ver todos los contactos
        print(f'\nTodos los contactos:')
        view_all_contacts(contact_list)

    elif notebook_menu == 3:  # Ver un contacto específico
        print(f'\nVer un contacto especifico')
        view_contact_by_position(contact_list)

    elif notebook_menu == 4:  # Ver nombre y teléfono de un contacto específico
        print(f'\nVer nombre y telefono de un contacto')
        view_name_and_phone(contact_list)

    elif notebook_menu == 5:  # Ver claves de los contactos
        print('\nClaves de los contactos:')
        view_keys(contact_list)

    elif notebook_menu == 6:  # Ver nombres con posiciones
        print('\nNombres con posiciones:')
        view_names_with_positions(contact_list)

    elif notebook_menu == 7:  # Buscar por nombre
        print(f'\nBuscar contacto por nombre')
        search_by_name(contact_list)

    elif notebook_menu == 8:  # Buscar por teléfono
        print(f'\nBuscar contacto por telefono')
        search_by_phone(contact_list)

    elif notebook_menu == 9:  # Ver cantidad de contactos
        print(f'\nCantidad de contactos en la lista')
        count_contacts(contact_list)

    elif notebook_menu == 10:  # Eliminar un contacto por posición
        print(f'\nEliminar contacto por posicion')
        delete_contact_by_position(contact_list)

    elif notebook_menu == 11:  # Eliminar un contacto por nombre
        print(f'\nBuscar nombres repetidos y eliminar contacto especifico')
        delete_contact_by_name(contact_list)

    elif notebook_menu == 12:  # Eliminar un contacto por teléfono
        print(f'\nBuscar numeros repetidos y eliminar contacto especifico')
        delete_contact_by_phone(contact_list)
    elif notebook_menu == 13:  # Salir
        print('Has salido de la agenda de contactos.')
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")