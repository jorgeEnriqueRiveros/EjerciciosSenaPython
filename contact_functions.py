# Archivo: contact_functions.py

def add_contact(contact_list):
    """Función para agregar un nuevo contacto a la lista."""
    print('Agregar Contacto:\n')
    name_user = input('Nombre: ').strip()
    last_name = input('Apellido: ').strip()

    try:
        age_user = int(input('Edad: '))
        if age_user <= 0:
            print("La edad debe ser un número positivo. Inténtalo de nuevo.")
            return
    except ValueError:
        print("Edad inválida. Por favor, ingresa solo números.")
        return

    try:
        phone_user = int(input('Teléfono: '))
        if phone_user < 1000:
            print("El número de teléfono debe tener al menos 4 dígitos. Inténtalo de nuevo.")
            return
    except ValueError:
        print("Teléfono inválido. Por favor, ingresa solo números.")
        return

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
    elif contact_confirmation == "no":
        print("Se canceló el registro del contacto.")


def view_all_contacts(contact_list):
    """Función para mostrar todos los contactos."""
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


def view_contact_by_position(contact_list):
    """Función para ver un contacto por su posición."""
    try:
        contact_position = int(input("Ingresa la posición del contacto a ver: "))
        if 0 <= contact_position < len(contact_list):
            contact = contact_list[contact_position]
            print(f'Contacto en posición {contact_position}:\n'
                  f'Nombre: {contact["Nombre"]}, '
                  f'Apellido: {contact["Apellido"]}, '
                  f'Edad: {contact["Edad"]}, '
                  f'Teléfono: {contact["Teléfono"]}, '
                  f'Correo: {contact["Correo electrónico"]}')
        else:
            print("Posición fuera de rango.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def view_name_and_phone(contact_list):
    """Función para ver solo el nombre y teléfono de un contacto."""
    try:
        contact_position = int(input("Ingresa la posición del contacto a ver (solo nombre y teléfono): "))
        if 0 <= contact_position < len(contact_list):
            contact = contact_list[contact_position]
            print(f'Nombre: {contact["Nombre"]}, Teléfono: {contact["Teléfono"]}')
        else:
            print("Posición fuera de rango.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def view_keys(contact_list):
    """Función para ver las claves de un contacto."""
    if not contact_list:
        print("No hay contactos para mostrar claves.")
        return
    print(f'Las claves de un contacto son:')
    contact = contact_list[0]  # Mostrar claves de cualquier contacto
    for key in contact.keys():
        print(key)


def view_names_with_positions(contact_list):
    """Función para ver nombres de contactos con su posición."""
    print(f'Nombres con posiciones:')
    if not contact_list:
        print("No hay contactos en la lista.")
    else:
        for i, contact in enumerate(contact_list):
            print(f'Posición {i}: {contact["Nombre"]}')


def search_by_name(contact_list):
    """Función para buscar un contacto por su nombre."""
    search_name = input("Ingresa el nombre del contacto a buscar: ").strip()
    found_contact = False
    for contact in contact_list:
        if contact["Nombre"].lower() == search_name.lower():
            print(f'Contacto encontrado: {contact}')
            found_contact = True
    if not found_contact:
        print(f'No se encontró ningún contacto con ese nombre.')


def search_by_phone(contact_list):
    """Función para buscar un contacto por su teléfono."""
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


def count_contacts(contact_list):
    """Función para ver la cantidad de contactos."""
    print(f'Número de contactos en la lista: {len(contact_list)}')


def delete_contact_by_position(contact_list):
    """Función para eliminar un contacto por posición."""
    try:
        delete_index = int(input("Ingresa el índice del contacto a eliminar: "))
        if 0 <= delete_index < len(contact_list):
            removed_contact = contact_list.pop(delete_index)
            print(f'Contacto eliminado: {removed_contact}')
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def delete_contact_by_name(contact_list):
    """Función para eliminar un contacto por nombre con selección de posición."""
    delete_name = input("Ingresa el nombre del contacto a eliminar: ").strip()
    matches = [
        (index, contact) for index, contact in enumerate(contact_list)
        if contact["Nombre"].lower() == delete_name.lower()
    ]

    if not matches:
        print("No se encontró ningún contacto con ese nombre.")
        return

    print("\nContactos encontrados con ese nombre:")
    for index, contact in matches:
        print(f'{index}. Nombre: {contact["Nombre"]}, '
              f'Apellido: {contact["Apellido"]}, '
              f'Teléfono: {contact["Teléfono"]}, '
              f'Correo: {contact["Correo electrónico"]}')

    try:
        delete_index = int(input("Selecciona el índice del contacto a eliminar: "))
        if delete_index in [index for index, _ in matches]:
            removed_contact = contact_list.pop(delete_index)
            print(f'Contacto eliminado: {removed_contact}')
        else:
            print("El índice seleccionado no es válido.")
    except ValueError:
        print("Por favor, ingresa un número válido para el índice.")


def delete_contact_by_phone(contact_list):
    """Función para eliminar un contacto por teléfono con selección de posición."""
    try:
        delete_phone = int(input("Ingresa el teléfono del contacto a eliminar: "))
        matches = [
            (index, contact) for index, contact in enumerate(contact_list)
            if contact["Teléfono"] == delete_phone
        ]

        if not matches:
            print("No se encontró ningún contacto con ese teléfono.")
            return

        print("\nContactos encontrados con ese número de teléfono:")
        for index, contact in matches:
            print(f'{index}. Nombre: {contact["Nombre"]}, '
                  f'Apellido: {contact["Apellido"]}, '
                  f'Teléfono: {contact["Teléfono"]}, '
                  f'Correo: {contact["Correo electrónico"]}')

        try:
            delete_index = int(input("Selecciona el índice del contacto a eliminar: "))
            if delete_index in [index for index, _ in matches]:
                removed_contact = contact_list.pop(delete_index)
                print(f'Contacto eliminado: {removed_contact}')
            else:
                print("El índice seleccionado no es válido.")
        except ValueError:
            print("Por favor, ingresa un número válido para el índice.")
    except ValueError:
        print("Por favor, ingresa un número de teléfono válido.")

