# Diccionario para almacenar un contacto temporal
contact_dictionary = dict()

# Lista para almacenar los contactos de la agenda
contact_list = []

# Creamos un menú interactivo usando un bucle 'while True' para que el programa se ejecute hasta que el usuario elija salir.
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
    print("10. Eliminar un contacto")
    print("11. Salir")

    # Solicitar al usuario que seleccione una opción del menú
    notebook_menu = int(input('Selecciona una opción de la agenda:\n'))

    # Opción 1: Agregar un contacto
    if notebook_menu == 1:
        print('Agregar Contacto:\n')

        # Pedir al usuario los datos del contacto
        name_user = input('Nombre: ')
        last_name = input('Apellido: ')
        age_user = int(input('Edad: '))
        phone_user = int(input('Teléfono: '))
        email_user = input('Correo electrónico: ')

        # Mostrar los datos ingresados para confirmar si son correctos
        print(f'\nDatos ingresados:\n'
              f'Nombre: {name_user}\n'
              f'Apellido: {last_name}\n'
              f'Edad: {age_user}\n'
              f'Teléfono: {phone_user}\n'
              f'Correo electrónico: {email_user}')

        # Confirmar si los datos son correctos
        contact_confirmation = input('¿Son correctos los datos (Sí/No): ').lower()

        if contact_confirmation == "sí":
            # Crear un diccionario con los datos del contacto
            contact_dictionary = {
                "Nombre": name_user,
                "Apellido": last_name,
                "Edad": age_user,
                "Teléfono": phone_user,
                "Correo electrónico": email_user
            }
            # Agregar el contacto a la lista
            contact_list.append(contact_dictionary)
            print('Contacto agregado correctamente.')
        elif contact_confirmation == "no":
            # Crear el diccionario para corregir
            contact_dictionary = {
                "Nombre": name_user,
                "Apellido": last_name,
                "Edad": age_user,
                "Teléfono": phone_user,
                "Correo electrónico": email_user
            }
            # Permitir al usuario corregir un campo específico
            edited_field = input('¿Qué campo deseas corregir (Nombre, Apellido, Edad, Teléfono o Correo electrónico)? ').capitalize()
            if edited_field in contact_dictionary:
                # Validar si el campo es Edad o Teléfono (ambos son números enteros)
                if edited_field in ["Edad", "Teléfono"]:
                    while True:
                        try:
                            new_value = int(input(f'Ingrese el nuevo valor para {edited_field}: '))
                            if new_value > 0:
                                contact_dictionary[edited_field] = new_value
                                break
                            else:
                                print("Por favor, ingresa un valor válido mayor que 0.")
                        except ValueError:
                            print(f"{edited_field} no válido. Ingresa solo números.")
                else:
                    # Para otros campos, no es necesario validar el tipo
                    new_value = input(f'Ingrese el nuevo valor para {edited_field}: ')
                    contact_dictionary[edited_field] = new_value
                print(f'{edited_field} ha sido corregido exitosamente.')
            else:
                print('Campo no válido. Los campos disponibles son: Nombre, Apellido, Edad, Teléfono, Correo electrónico.')

    # Opción 2: Ver todos los contactos
    elif notebook_menu == 2:
        print('\nTodos los contactos:')
        # Mostrar cada contacto en la lista
        for contact_dictionary in contact_list:
            print(f'Nombre: {contact_dictionary["Nombre"]}, '
                  f'Apellido: {contact_dictionary["Apellido"]}, '
                  f'Edad: {contact_dictionary["Edad"]}, '
                  f'Teléfono: {contact_dictionary["Teléfono"]}, '
                  f'Correo electrónico: {contact_dictionary["Correo electrónico"]}')

    # Opción 3: Ver un contacto específico
    elif notebook_menu == 3:
        contact_position = int(input('Ingresa la posición del contacto (empezando en 0): '))
        if 0 <= contact_position < len(contact_list):
            # Mostrar el contacto en la posición especificada
            contact_dictionary = contact_list[contact_position]
            print(contact_dictionary)
        else:
            print('Posición no válida.')

    # Opción 4: Ver nombre y teléfono de un contacto específico
    elif notebook_menu == 4:
        contact_position = int(input('Ingresa la posición del contacto (empezando en 0): '))
        if 0 <= contact_position < len(contact_list):
            contact_dictionary = contact_list[contact_position]
            # Mostrar solo el nombre y teléfono del contacto
            print(f'Nombre: {contact_dictionary.get("Nombre")}, Teléfono: {contact_dictionary.get("Teléfono")}')
        else:
            print('Posición no válida.')

    # Opción 5: Ver claves de los contactos
    elif notebook_menu == 5:
        print('\nClaves de los contactos:')
        # Mostrar las claves del diccionario
        for contact_key in contact_dictionary.keys():
            print(contact_key)

    # Opción 6: Ver nombres con posiciones
    elif notebook_menu == 6:
        print('\nNombres con posiciones:')
        # Enumerar cada contacto y mostrar su posición junto con el nombre
        for i, contact_value in enumerate(contact_list):
            print(f'Posición {i}: {contact_value.get("Nombre")}')

    # Opción 7: Buscar por nombre
    elif notebook_menu == 7:
        search_name = input('Ingresa el nombre del contacto a buscar: ')
        found_contact = False
        # Buscar el contacto en la lista por nombre
        for contact_value in contact_list:
            if contact_value.get("Nombre") == search_name:
                print(f'Contacto encontrado: {contact_value}')
                found_contact = True
        if not found_contact:
            print('No se encontró ningún contacto con este nombre.')

    # Opción 8: Buscar por teléfono
    elif notebook_menu == 8:
        search_phone = int(input('Ingresa el teléfono del contacto a buscar: '))
        found_contact = False
        # Buscar el contacto en la lista por teléfono
        for contact_value in contact_list:
            if contact_value.get("Teléfono") == search_phone:
                print(f'Contacto encontrado: {contact_value}')
                found_contact = True
        if not found_contact:
            print('No se encontró ningún contacto con este teléfono.')

    # Opción 9: Ver cantidad de contactos
    elif notebook_menu == 9:
        print(f'Hay {len(contact_list)} contactos en la lista.')

    # Opción 10: Eliminar un contacto
    elif notebook_menu == 10:
        print('\nEliminar un contacto:')
        for i, contact_value in enumerate(contact_list):
            print(f'{i}. {contact_value.get("Nombre")}')
        delete_index = int(input('Ingrese el índice del contacto que desea eliminar: '))
        if 0 <= delete_index < len(contact_list):
            contact_list.pop(delete_index)
            print('Contacto eliminado correctamente.')
        else:
            print('Índice fuera de rango.')

    # Opción 11: Salir del programa
    elif notebook_menu == 11:
        print('Has salido de la agenda de contactos.')
        break

    # Opción inválida
    else:
        print('Opción no válida. Por favor, selecciona una opción del menú.')




