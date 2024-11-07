import random

def crear_nombre_usuario(nombre, apellido, identidad):
    # Tomar los dos primeros caracteres del nombre y convertirlos a mayúsculas
    parte_nombre = nombre[:2].upper()
    # Tomar los dos últimos caracteres del apellido y convertirlos a mayúsculas
    parte_apellido = apellido[-2:].upper()
    # Tomar los tres últimos dígitos del número de identidad
    parte_identidad = identidad[-3:]
    # Generar un número aleatorio de dos dígitos
    numero_aleatorio = random.randint(10, 99)
    # Concatenar todas las partes para formar el nombre de usuario
    nombre_usuario = f"{parte_nombre}{parte_apellido}{parte_identidad}{numero_aleatorio}"
    return nombre_usuario

# Solicitar los datos del usuario
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
identidad = input("Introduce tu número de identidad: ")

# Generar el nombre de usuario
usuario = crear_nombre_usuario(nombre, apellido, identidad)

# Mostrar el nombre de usuario generado
print("Tu nombre de usuario es:", usuario)
