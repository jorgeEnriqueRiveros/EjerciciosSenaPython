import random  # Importa el módulo random para generar números aleatorios

# Solicita al usuario que ingrese su nombre, apellido y número de identificación
name_user = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
num_id = input("Ingrese su numero de indentificacion: ")

# Toma las dos primeras letras del nombre y las convierte en mayúsculas
part_name = name_user[:2].upper()
# Toma las dos primeras letras del apellido y las convierte en mayúsculas
part_last = last_name[-2:].upper()
# Toma los tres primeros caracteres del número de identificación y los convierte en mayúsculas
part_id = num_id[-3:]
# Genera un número aleatorio entre 10 y 99
random_number = random.randint(10, 99)

# Combina las partes generadas para crear el nombre de usuario
generated_username = f"{part_name}{part_last}{part_id}{random_number}"

# Imprime el nombre de usuario generado
print(f'''Este es tu nombre de usuario generado
{generated_username}''')