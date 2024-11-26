# Definimos un diccionario con información variada sobre un usuario
dictionary_values = {"name_user": "jorge", "last_name": "riveros", True: "Verdadero", "Edad": 33,
                     "NumeroDocumento": 1122128473}

# Imprimimos el contenido del diccionario en formato amigable
print(f'Este es mi diccionario:\n'
      f'{dictionary_values}')

# Definimos un diccionario con información sobre un carro
# Nota: Al usar claves duplicadas, las últimas sobreescriben a las anteriores
dictionary_cars = {"Placa": "PIX830", "Clase de traccion": "4x4", "Marca": "lotus", True: "Radio",
                   "aireAcondicionado": True, "llantas": 5, "Color": "verde", "Color": "azul", True: "VidriosElectricos",
                   "Marca": "Chevrolet"}

# Mostramos el contenido del diccionario de carros
print(f'Este es el diccionario de carros: \n'
      f'{dictionary_cars}')

# Accedemos a un valor específico del diccionario utilizando su clave
print(f'Esta es la marca del carro: \n'
      f'{dictionary_cars["Marca"]}')

# Mostramos información del diccionario de carros usando interpolación de strings
# Interpolación permite mostrar valores de manera directa en una cadena de texto
print(f'----Aqui estamos interpolando sin el metodo get:-----')
print(f'Estos son los datos del diccionario carro:\n'
      f'Esta es la marca del carro: {dictionary_cars["Marca"]}\n'  # Accedemos directamente con []
      f'Esta es la placa del carro: {dictionary_cars["Placa"]}\n'
      f'Este es el color del carro: {dictionary_cars["Color"]}')

# Mostramos información del diccionario usando el método `get`
# `get` es útil porque no lanza un error si la clave no existe, sino que devuelve `None`
print(f'----Esta parte del codigo estamos usando get para buscar el valor:-----')
print(f'Estos son los datos del diccionario carro:\n'
      f'Esta es la marca del carro: {dictionary_cars.get("Marca")}\n'
      f'Esta es la placa del carro: {dictionary_cars.get("Placa")}\n'
      f'Este es el color del carro: {dictionary_cars.get("Color")}')

# Obtenemos la cantidad de elementos (pares clave-valor) en el diccionario
print(f'Esta es la cantidad de valores del diccionario:\n'
      f'{len(dictionary_cars)}')

# Modificamos el valor de una clave existente en el diccionario `dictionary_values`
dictionary_values["name_user"] = "Enrique"
# Mostramos el diccionario después de la modificación
print(f'Aqui se modifica la clave y el valor del diccionario valores:\n'
      f'{dictionary_values}')

# Agregamos una nueva clave-valor al diccionario `dictionary_cars`
dictionary_cars["Peso"] = 2000
# Usamos `setdefault` para agregar una nueva clave solo si no existe
dictionary_cars.setdefault("Ciudad", "Villavicencio")
# Mostramos el diccionario de carros después de agregar nuevos valores
print(f'Aqui esta el diccionario carro agregando un nuevo valor\n'
      f'{dictionary_cars}')

# Mostramos nuevamente el diccionario, aunque esta línea repite el mismo contenido que la anterior
print(f'Aqui se agrega un valor al diccionario carro a lo ultimo:\n'
      f'{dictionary_cars}')
#Esto fue lo que iniciamos hacer hoy de hacer varios cambios al diccionario y demás, 25/11/2024
# Creamos dos diccionarios `dic_values1` y `dic_values2` con información sobre personas
dic_values1 = {"nombre": "Jorge", "Apellido": "Riveros", "cedula": 1122128473, "Celular": 3123347158,
               "Correo": "jorgjuanjo@gmail.com", "Ciudad": "Castilla la Nueva", "edad": 33, True: "verdadero"}
dic_values2 = {"nombre": "Alejandra", "Apellido": "Martinez", "cedula": 1110128543, "Celular": 3108000270,
               "Correo": "Nagela2024@gmail.com", "Ciudad": "Acacias", "edad": 33, True: "verdadero"}

# Unimos los diccionarios `dic_values1` y `dic_values2` usando el método `update`
dic_values1.update(dic_values2)
print(dic_values1)

# Mostramos las claves que se encuentran en el diccionario
print(f'Aqui podemos saber las claves que se encuentran en el diccionario: \n'
      f'{dic_values1.keys(),type(dic_values1)}')

# Iteramos sobre las claves del diccionario e imprimimos cada una junto con su valor
for i in dic_values1.keys():
    print(f'Claves: '
          f'{i} : {dic_values1[i]}')

# Mostramos todos los valores del diccionario sin mostrar las claves
print(f'\t\t\t\t\t\t Aqui se imprime todos valores sin su clave: \n'
      f'{dic_values1.values()}')

# Solicitamos al usuario que ingrese una clave para buscarla en el diccionario
key_entered = input(f'Por favor ingresa una clave a buscar:\n').strip().lower()

# Verificamos si la clave existe en el diccionario
if key_entered in dic_values1.keys():
    print(f'La clave ingresada si se encuentra en el diccionario')
    # Si existe, pedimos un nuevo valor para reemplazarlo
    value_entered = input(f'Ingresa el valor para el valor a cambiar:\n ').strip().lower()
    dic_values1[key_entered] = value_entered  # Actualizamos el valor de la clave
    print(f'Este es el diccionario 1 cambiando la clave por consola {dic_values1}')
else:
    print(f'La clave no encontrada intentalo de nuevo')

# Usamos (enumerate): para iterar sobre el diccionario, mostrando el índice y la clave
for i, claves in enumerate(dic_values1.keys()):
    print(f'{i} = {claves} | {dic_values1[claves]}')

# Verificamos si una clave existe y si existe, cambiamos su valor por un nuevo valor
print(f'----Verificando si una clave existe y colocando la cadena "software-----"')
key_entered = input(f'Por favor ingresa una clave a buscar:\n').strip().lower()
if key_entered in dic_values1.keys():
    print(f'La clave ingresada si se encuentra en el diccionario')
    value_entered = input(f'Ingresa el valor para el valor a cambiar:\n ').strip().lower()
    dic_values1[key_entered] = value_entered
    print(f'Este es el diccionario 1 cambiando la clave por consola: \n'
          f'{dic_values1}')
else:
    print(f'La clave no encontrada intentalo de nuevo')

# Convertimos las claves del diccionario a una lista y la mostramos
print(f'-----convirtiendo las claves del diccionario a una lista-----')
key_list = list(dic_values1.keys())
print(f'Lista de claves del diccionario 1:\n'
      f'{key_list}')

# Iteramos sobre los valores del diccionario y los mostramos
print(f'----iterando con un for los valores-----')
for i in dic_values1.values():
    print(f'{i}')

# Definimos un diccionario con números y buscamos el valor máximo
dictionary_numbers = {1: 33, 2: 70, 3: 2024, 4: 65, 5: 1991, 6: 3034, 7: 105}
maximum_number = max(dictionary_numbers.values())  # Buscamos el valor máximo

print(f'Buscando el valor maximo del diccionario:\n'
      f'{maximum_number}')

# Utilizamos comprensión de diccionario para encontrar las claves asociadas al valor máximo
max_dict = {k: v for k, v in dictionary_numbers.items() if v == maximum_number}
print(f'Buscando el valor máximo del diccionario:\n{maximum_number}')
print(f'Elementos asociados al valor máximo:\n{max_dict}')

# Realizamos la suma de los valores del diccionario
print(f'Esta es la suma de los valores del diccionario {sum(dictionary_numbers.values())}')

# Convertimos los valores del diccionario a una tupla y la mostramos
numbers_tuple = tuple(dictionary_numbers.values())
print(f'Pasando los valores a una tupla:\n'
      f'{numbers_tuple}')

# Imprimimos el diccionario con el método `items()` que muestra las claves y valores juntos
print(f'Este es el diccionario con items:\n'
      f'{dictionary_numbers.items()}', type(dictionary_numbers))

# Iteramos sobre el diccionario con `enumerate()` para mostrar índices, claves y valores
for i, (clave, valor) in enumerate(dictionary_numbers.items()):
    print(f'{i} = clave {clave} : valor {valor}')

# Solicitar clave al usuario y buscarla en el diccionario
search_key = int(input("Ingresa la clave que deseas buscar: "))
for i, (clave, valor) in enumerate(dictionary_numbers.items()):
    if clave == search_key:
        print(f'La clave {clave} fue encontrada en el índice {i + 1} con el valor {valor}.')
        break
else:
    print(f'La clave {search_key} no está en el diccionario.')

# Solicitar clave al usuario para actualizar su valor
search_key = int(input("Ingresa la clave cuyo valor deseas cambiar: "))

if search_key in dictionary_numbers:
    new_value = int(input(f"Ingresar el nuevo valor para la clave {search_key}: "))
    dictionary_numbers[search_key] = new_value
    print(f"Clave {search_key} actualizada con el valor {new_value}.")
else:
    print(f"La clave {search_key} no está en el diccionario.")

# Imprimir el diccionario actualizado
print(f"Diccionario actualizado: {dictionary_numbers}")

# Solicitar la clave actual y la nueva clave al usuario
current_key = int(input("Ingresa la clave cuyo nombre deseas cambiar: "))

# Verificar si la clave actual existe en el diccionario
if current_key in dictionary_numbers.keys():
    # Almacenar el valor de la clave actual
    valor = dictionary_numbers[current_key]
    # Eliminar la clave antigua
    del dictionary_numbers[current_key]
    new_key = int(input("Ingresa la nueva clave: "))
    # Agregar la nueva clave con el mismo valor
    dictionary_numbers[new_key] = valor
    print(f"La clave {current_key} ha sido cambiada a {new_key} con el valor {valor}.")
else:
    print(f"La clave {current_key} no está en el diccionario.")
# Imprimir el diccionario actualizado
print(f"Diccionario actualizado: {dictionary_numbers}")