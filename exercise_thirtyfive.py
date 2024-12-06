# Diccionario y lista para almacenar contactos
contact_dictionary = dict()
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
        name_user = input('Nombre: ').strip()
        last_name = input('Apellido: ').strip()

        try:
            age_user = int(input('Edad: '))
            if age_user <= 0:
                print("La edad debe ser un número positivo. Inténtalo de nuevo.")
                continue
        except ValueError:
            print("Edad inválida. Por favor, ingresa solo números.")
            continue

        try:
            phone_user = int(input('Teléfono: '))
            if phone_user < 1000:
                print("El número de teléfono debe tener al menos 4 dígitos. Inténtalo de nuevo.")
                continue
        except ValueError:
            print("Teléfono inválido. Por favor, ingresa solo números.")
            continue

        # Generar correo automáticamente
        generated_email = (
            name_user[:3].lower() +
            last_name[-3:].lower() +
            str(phone_user)[-4:] +
            "@gmail.com"
        )
        print(f"Correo generado automáticamente: {generated_email}")

        # Mostrar los datos ingresados junto con el correo generado
        print(f'\nDatos ingresados:\n'
              f'Nombre: {name_user}\n'
              f'Apellido: {last_name}\n'
              f'Edad: {age_user}\n'
              f'Teléfono: {phone_user}\n'
              f'Correo generado: {generated_email}')

        contact_confirmation = input('¿Son correctos los datos (Si/No)? ').strip().lower()
        if contact_confirmation == "si":
            # Crear el diccionario con los datos confirmados
            contact_dictionary = {
                "Nombre": name_user,
                "Apellido": last_name,
                "Edad": age_user,
                "Teléfono": phone_user,
                "Correo electrónico": generated_email
            }
            contact_list.append(contact_dictionary)  # Agregar el diccionario a la lista
            print('Contacto agregado correctamente.')
        else:
            print("Se canceló el registro del contacto.")

    elif notebook_menu == 2:  # Ver todos los contactos
        print(f'\nTodos los contactos:')
        if not contact_list:
            print("No hay contactos en la lista.")
        else:
            for i, contact in enumerate(contact_list):
                print(f'{i + 1}. Nombre: {contact["Nombre"]}, '
                      f'Apellido: {contact["Apellido"]}, '
                      f'Edad: {contact["Edad"]}, '
                      f'Teléfono: {contact["Teléfono"]}, '
                      f'Correo: {contact["Correo electrónico"]}')

    elif notebook_menu == 3:  # Ver un contacto específico
        print(f'\nVer un contacto específico')
        try:
            contact_position = int(input("Ingresa la posición del contacto a ver: ")) - 1
            if 0 <= contact_position < len(contact_list):
                contact = contact_list[contact_position]
                print(f'Contacto en posición {contact_position + 1}:\n'
                      f'Nombre: {contact["Nombre"]}\n'
                      f'Apellido: {contact["Apellido"]}\n'
                      f'Edad: {contact["Edad"]}\n'
                      f'Teléfono: {contact["Teléfono"]}\n'
                      f'Correo: {contact["Correo electrónico"]}')
            else:
                print("Posición fuera de rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    elif notebook_menu == 4:  # Ver nombre y teléfono de un contacto específico
        print(f'\nVer nombre y teléfono de un contacto')
        try:
            contact_position = int(input("Ingresa la posición del contacto a ver: ")) - 1
            if 0 <= contact_position < len(contact_list):
                contact = contact_list[contact_position]
                print(f'Nombre: {contact["Nombre"]}, Teléfono: {contact["Teléfono"]}')
            else:
                print("Posición fuera de rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    elif notebook_menu == 5:  # Ver claves de los contactos
        print('\nClaves de los contactos:')
        if not contact_list:
            print("No hay contactos para mostrar claves.")
        else:
            print(f'Las claves de un contacto son:')
            for key in contact_list[0].keys():
                print(key)

    elif notebook_menu == 6:  # Ver nombres con posiciones
        print('\nNombres con posiciones:')
        if not contact_list:
            print("No hay contactos en la lista.")
        else:
            for i, contact in enumerate(contact_list):
                print(f'Posición {i + 1}: {contact.get("Nombre")}')

    elif notebook_menu == 7:  # Buscar por nombre
        print(f'\nBuscar contacto por nombre')
        search_name = input("Ingresa el nombre del contacto a buscar: ").strip().lower()
        found_contact = False
        for contact in contact_list:
            if contact["Nombre"].lower() == search_name.lower():
                print(f'Contacto encontrado: {contact}')
                found_contact = True
        if not found_contact:
            print(f'No se encontró ningún contacto con ese nombre.')

    elif notebook_menu == 8:  # Buscar por teléfono
        print(f'\nBuscar contacto por teléfono')
        try:
            search_phone = int(input("Ingresa el teléfono del contacto a buscar: "))
            found_contact = False
            for contact in contact_list:
                if contact["Teléfono"] == search_phone:
                    print(f'Contacto encontrado: {contact}')
                    found_contact = True
            if not found_contact:
                print("No se encontró ningún contacto con ese teléfono.")
        except ValueError:
            print("Por favor, ingresa un número de teléfono válido.")

    elif notebook_menu == 9:  # Ver cantidad de contactos
        print(f'\nCantidad de contactos en la lista:')
        print(f'Número de contactos en la lista: {len(contact_list)}')

    elif notebook_menu == 10:  # Eliminar un contacto por posición
        print(f'\nEliminar contacto por posición')
        try:
            delete_index = int(input("Ingresa el índice del contacto a eliminar: ")) - 1
            if 0 <= delete_index < len(contact_list):
                removed_contact = contact_list.pop(delete_index)
                print(f'Contacto eliminado: {removed_contact}')
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    elif notebook_menu == 11:  # Eliminar un contacto por nombre
        print(f'\nEliminar contacto por nombre')
        delete_name = input("Ingresa el nombre del contacto a eliminar: ").strip()
        matches = [
            (index, contact) for index, contact in enumerate(contact_list)
            if contact["Nombre"].lower() == delete_name.lower()
        ]
        if not matches:
            print("No se encontró ningún contacto con ese nombre.")
        else:
            print("\nContactos encontrados con ese nombre:")
            for index, contact in matches:
                print(f'{index + 1}. Nombre: {contact["Nombre"]}, '
                      f'Apellido: {contact["Apellido"]}, '
                      f'Teléfono: {contact["Teléfono"]}, '
                      f'Correo: {contact["Correo electrónico"]}')
            try:
                delete_index = int(input("Selecciona el índice del contacto a eliminar: ")) - 1
                if delete_index in [index for index, _ in matches]:
                    removed_contact = contact_list.pop(delete_index)
                    print(f'Contacto eliminado: {removed_contact}')
                else:
                    print("El índice seleccionado no es válido.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    elif notebook_menu == 12:  # Eliminar un contacto por teléfono
        print(f'\nEliminar contacto por teléfono')
        try:
            delete_phone = int(input("Ingresa el teléfono del contacto a eliminar: "))
            matches = [
                (index, contact) for index, contact in enumerate(contact_list)
                if contact["Teléfono"] == delete_phone
            ]
            if not matches:
                print("No se encontró ningún contacto con ese teléfono.")
            else:
                print("\nContactos encontrados con ese número de teléfono:")
                for index, contact in matches:
                    print(f'{index + 1}. Nombre: {contact["Nombre"]}, '
                          f'Apellido: {contact["Apellido"]}, '
                          f'Teléfono: {contact["Teléfono"]}, '
                          f'Correo: {contact["Correo electrónico"]}')
                try:
                    delete_index = int(input("Selecciona el índice del contacto a eliminar: ")) - 1
                    if delete_index in [index for index, _ in matches]:
                        removed_contact = contact_list.pop(delete_index)
                        print(f'Contacto eliminado: {removed_contact}')
                    else:
                        print("El índice seleccionado no es válido.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
        except ValueError:
            print("Por favor, ingresa un número de teléfono válido.")

    elif notebook_menu == 13:  # Salir
        print('Has salido de la agenda de contactos.')
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")