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

# # Reiniciamos el diccionario `dictionary_values` como un diccionario vacío
# dictionary_values = {}
#
# # Solicitamos al usuario que ingrese datos al diccionario
# entered_data = input(f'Ingresa datos al diccionario: \n')  # Esta línea no se usa en el código posterior
#
# # Usamos un bucle `while` para permitir al usuario agregar elementos al diccionario
# while True:
#     # Pedimos al usuario una clave
#     entered_key = input(f'Ingresa la clave (o escribe salir para terminar el programa): \n')
#     # Si la clave es "salir", salimos del bucle
#     if entered_key.lower() == "salir":
#         break
#     # Pedimos al usuario un valor asociado a la clave
#     value_entered = input(f'Ingresa el valor para la clave "{entered_key}": \n')
#     # Agregamos el par clave-valor al diccionario
#     dictionary_values[entered_key] = value_entered
#
# # Mostramos el diccionario final con los datos ingresados por el usuario
# print(f'\n Mi diccionario final:\n'
#       f'{dictionary_values}')
dic_values1 = {"nombre": "Jorge","Apellido": "Riveros", "cedula":1122128473, "Celular":3123347158,
               "Correo":"jorgjuanjo@gmail.com","Ciudad":"Castilla la Nueva"}
dic_values2 = {"nombre": "Alejandra","Apellido": "Martinez", "cedula":1110128543, "Celular":3108000270,
               "Correo":"Nagela2024@gmail.com","Ciudad":"Acacias"}
dic_values1.update(dic_values2)
print(dic_values1)
print(f'Aqui podemos saber las claves que se encuentran en el diccionario: \n'
      f'{dic_values1.keys(),type(dic_values1)}')
for i in dic_values1.keys():
    print(f'Claves: '
          f'{i} : {dic_values1[i]}')
