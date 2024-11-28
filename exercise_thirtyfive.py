# Diccionario para almacenar un contacto temporal
contact_dictionary = dict()

# Lista para almacenar los contactos de la agenda
contact_list = []

# Menú interactivo
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

    # Captura de la opción seleccionada
    notebook_menu = int(input(f'Selecciona una opción de la agenda:\n'))

    if notebook_menu == 1:
        print(f'\nAgregar Contacto:')
        # Captura de datos del contacto
        name_user = input(f'Nombre: ')
        last_name = input(f'Apellido: ')
        try:
            age_user = int(input(f'Edad: '))
            phone_user = int(input(f'Teléfono: '))
        except ValueError:
            print("La edad y el teléfono deben ser números.")
            continue  # Volver al menú si hay un error
        email_user = input(f'Correo electrónico: ')

        # Mostrar los datos ingresados
        print(f'\nDatos ingresados:')
        print(f'Nombre: {name_user}')
        print(f'Apellido: {last_name}')
        print(f'Edad: {age_user}')
        print(f'Teléfono: {phone_user}')
        print(f'Correo electrónico: {email_user}')

        # Confirmación de los datos
        contact_confirmation = input(f'¿Son correctos los datos (Si/No)? ').strip().lower().capitalize()
        if contact_confirmation == "si":
            # Crear el diccionario con los datos confirmados
            contact_dictionary = {
                "Nombre": name_user,
                "Apellido": last_name,
                "Edad": age_user,
                "Teléfono": phone_user,
                "Correo electrónico": email_user
            }
            contact_list.append(contact_dictionary)  # Agregar el diccionario a la lista
            print('Contacto agregado correctamente.')
        elif contact_confirmation == "no":
            # Crear el diccionario temporal para corregir datos
            contact_dictionary = {
                "Nombre": name_user,
                "Apellido": last_name,
                "Edad": age_user,
                "Teléfono": phone_user,
                "Correo electrónico": email_user
            }
            # Permitir al usuario corregir un campo
            edited_field = input(f'¿Qué campo deseas corregir (Nombre, Apellido, Edad, Teléfono o Correo electrónico)? ').capitalize()
            if edited_field in contact_dictionary:
                # Validar si el campo es Edad o Teléfono (son números enteros)
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
                            print(f"El valor ingresado para {edited_field} no es válido. Debe ser un número.")
                else:
                    # Para otros campos, no es necesario validar el tipo
                    new_value = input(f'Ingrese el nuevo valor para {edited_field}: ')
                    contact_dictionary[edited_field] = new_value
                print(f'{edited_field} ha sido corregido exitosamente.')
                print(f'Datos actualizados: {contact_dictionary}')
            else:
                print('Campo no válido. Asegúrate de ingresar uno de los siguientes: Nombre, Apellido, Edad, Teléfono, Correo electrónico.')

            # Confirmar si agregar el contacto después de corregir
            final_confirmation = input(f'¿Deseas agregar el contacto corregido a la lista (Sí/No)? ').strip().lower()
            if final_confirmation == "sí":
                contact_list.append(contact_dictionary)  # Agregar el contacto corregido a la lista
                print('Contacto corregido y agregado a la lista.')
            else:
                print('El contacto no se agregó a la lista.')

    elif notebook_menu == 2:
        # Ver todos los contactos
        if contact_list:
            print('\nTodos los contactos:')
            for contact in contact_list:
                print(f'Nombre: {contact["Nombre"]}, '
                      f'Apellido: {contact["Apellido"]}, '
                      f'Edad: {contact["Edad"]}, '
                      f'Teléfono: {contact["Teléfono"]}, '
                      f'Correo electrónico: {contact["Correo electrónico"]}')
        else:
            print('La lista de contactos está vacía.')

    elif notebook_menu == 3:
        # Ver un contacto específico
        contact_position = int(input(f'Ingresa la posición del contacto (empezando de 0): '))
        if 0 <= contact_position < len(contact_list):
            contact = contact_list[contact_position]
            print(f'Nombre: {contact["Nombre"]}, '
                  f'Apellido: {contact["Apellido"]}, '
                  f'Edad: {contact["Edad"]}, '
                  f'Teléfono: {contact["Teléfono"]}, '
                  f'Correo electrónico: {contact["Correo electrónico"]}')
        else:
            print('Posición no válida.')

    elif notebook_menu == 4:
        # Ver nombre y teléfono de un contacto específico
        contact_position = int(input(f'Ingresa la posición del contacto (empezando de 0): '))
        if 0 <= contact_position < len(contact_list):
            contact = contact_list[contact_position]
            print(f'Nombre: {contact.get("Nombre")}, Teléfono: {contact.get("Teléfono")}')
        else:
            print('Posición no válida.')

    elif notebook_menu == 5:
        # Ver claves de los contactos
        if contact_list:
            print(f'\nClaves de los contactos:')
            for key in contact_list[0].keys():
                print(f'- {key}')
        else:
            print('La lista de contactos está vacía.')

    elif notebook_menu == 6:
        # Ver nombres con posiciones
        if contact_list:
            print(f'\nNombres con posiciones:')
            for i, contact in enumerate(contact_list):
                print(f'Posición {i}: {contact.get("Nombre")}')
        else:
            print('La lista de contactos está vacía.')

    elif notebook_menu == 7:
        # Buscar por nombre
        search_name = input(f'Ingresa el nombre del contacto a buscar: ')
        found = False
        for contact in contact_list:
            if contact["Nombre"].lower() == search_name.lower():
                print(f'Contacto encontrado: {contact}')
                found = True
        if not found:
            print('No se encontró ningún contacto con ese nombre.')

    elif notebook_menu == 8:
        # Buscar por teléfono
        try:
            search_phone = int(input(f'Ingresa el teléfono del contacto a buscar: '))
        except ValueError:
            print("El teléfono debe ser un número.")
            continue
        found = False
        for contact in contact_list:
            if contact["Teléfono"] == search_phone:
                print(f'Contacto encontrado: {contact}')
                found = True
        if not found:
            print('No se encontró ningún contacto con ese teléfono.')

    elif notebook_menu == 9:
        # Ver cantidad de contactos
        print(f'Hay {len(contact_list)} contactos en la lista.')

    elif notebook_menu == 10:
        # Eliminar un contacto
        print(f'\nEliminar un contacto:')
        for i, contact in enumerate(contact_list):
            print(f'{i}. {contact.get("Nombre")}')
        try:
            delete_index = int(input(f'Ingrese el índice del contacto que desea eliminar: '))
            if 0 <= delete_index < len(contact_list):
                contact_list.pop(delete_index)
                print('Contacto eliminado correctamente.')
            else:
                print('Índice fuera de rango.')
        except ValueError:
            print("Debes ingresar un número válido.")

    elif notebook_menu == 11:
        # Salir del programa
        print('Has salido de la agenda de contactos.')
        break

    else:
        print('Opción no válida. Por favor, selecciona una opción del menú.')