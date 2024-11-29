# Función para agregar un contacto
def agregar_contacto(contact_list, name_user, last_name, age_user, phone_user):
    generated_email = (
        name_user[:3].lower() +
        last_name[-3:].lower() +
        str(phone_user)[-4:] +
        "@gmail.com"
    )
    contact_dictionary = {
        "Nombre": name_user,
        "Apellido": last_name,
        "Edad": age_user,
        "Teléfono": phone_user,
        "Correo electrónico": generated_email
    }
    contact_list.append(contact_dictionary)
    return contact_list

# Función para ver todos los contactos
def ver_contactos(contact_list):
    return contact_list

# Función para ver un contacto específico
def ver_contacto_especifico(contact_list, contact_position):
    if 0 <= contact_position < len(contact_list):
        return contact_list[contact_position]
    else:
        return None

# Función para ver nombre y teléfono de un contacto específico
def ver_nombre_y_telefono(contact_list, contact_position):
    if 0 <= contact_position < len(contact_list):
        contact = contact_list[contact_position]
        return f'Nombre: {contact["Nombre"]}, Teléfono: {contact["Teléfono"]}'
    else:
        return None

# Función para ver claves de los contactos
def ver_claves(contact_list):
    if contact_list:
        return contact_list[0].keys()
    else:
        return []

# Función para ver nombres con posiciones
def ver_nombres_con_posiciones(contact_list):
    return [(i, contact["Nombre"]) for i, contact in enumerate(contact_list)]

# Función para buscar por nombre
def buscar_por_nombre(contact_list, search_name):
    found_contacts = [contact for contact in contact_list if contact["Nombre"].lower() == search_name.lower()]
    return found_contacts

# Función para buscar por teléfono
def buscar_por_telefono(contact_list, search_phone):
    found_contacts = [contact for contact in contact_list if contact["Teléfono"] == search_phone]
    return found_contacts

# Función para eliminar un contacto por posición
def eliminar_por_posicion(contact_list, delete_index):
    if 0 <= delete_index < len(contact_list):
        return contact_list.pop(delete_index)
    else:
        return None

# Función para eliminar un contacto por nombre
def eliminar_por_nombre(contact_list, delete_name):
    removed_contacts = [contact for contact in contact_list if contact["Nombre"].lower() == delete_name.lower()]
    contact_list = [contact for contact in contact_list if contact["Nombre"].lower() != delete_name.lower()]
    return contact_list, removed_contacts

# Función para eliminar un contacto por teléfono
def eliminar_por_telefono(contact_list, delete_phone):
    removed_contacts = [contact for contact in contact_list if contact["Teléfono"] == delete_phone]
    contact_list = [contact for contact in contact_list if contact["Teléfono"] != delete_phone]
    return contact_list, removed_contacts
