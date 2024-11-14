print(f'-----------forma de buscar numeros en una lista-------------------')
list_numbers = [33,40,18,30,19,50,70]
entered_number = int(input(f'Ingrese el numero a buscar: '))
if entered_number in list_numbers:
    print(f'El numero se encuentra en la lista {entered_number}')
else:
    print(f'no encontramos el numero {entered_number} no se encuentra en la lista')
print(f'------------forma de buscar letras en una lista-------------------')
list_names = ['a','e','i','o','u']
entered_words = input(f'por favor ingresa una letra a buscar: ').lower()
if entered_words in list_names:
    print(f'la letra {entered_words} que ingresaste esta en la lista')
else:
    print(f'la letra {entered_words} que ingresaste no esta en la lista')
print(f'-----------funcion index------------------')
entered_number = int(input(f'por favor ingresa un numero: '))
entered_index = list_numbers.index(entered_number)
print(f'el numero {entered_number} esta en el indice {entered_index}')
sub_numbers = list_numbers[1:4]
print(f'Esta es la sublista de los numeros {sub_numbers}')
print(f'------------funcion len y append-----------------')
count_list = len(list_numbers)
print(f'Esta es la cantidad de datos de la lista {count_list}')
print(f'-----------metodo appeend----------------')
print(f'esta es la lista antes de agregar el valor \n'
      f'{list_numbers}')
list_numbers.append(2024)
print(list_numbers)
print(f'----------metodo insert-----------------')
print(f'Esta es la lista antes de agregar un valor en un indice definido \n'
      f'{list_numbers}')
list_numbers.insert(4,3034)
print(f'Agregando un valor en el indice 4, \n'
      f'{list_numbers}')
print(f'---------------metodo remove------------------')
list_numbers.remove(33)
print(f'Se elimina un valor de la lista :(33) \n'
      f'{list_numbers}')
print(f'-----------------concatenar listas--------------------')
list_numbers = [33,40,50,70,33,40,80,90,2024,45,18,33]
print(f'{list_numbers}')
list_names = ['alejandra','angel','andrea','jorge','juanjose']
concatenate_lists = list_numbers + list_names
print(f'Estas son las 2 listas \n'
      f'{concatenate_lists}')
print(f'---------------funcion del para eliminar---------------')
del list_names[2]
print(f'Esta es la lista de nombres eliminando el indice 2 {list_names}')
#eliminando un rango de indices con la funcion del
del list_numbers[:-4]
print(f'Esta es la lista eliminando del indice 0 al 4 {list_numbers}')
print(f'------------metodo pop para eliminar un indice especifico-------------')
deleted_number = list_numbers.pop(2)
print(f'Eliminando un indice de la lista {list_numbers}')
print(f'El numero eliminado es: {deleted_number}')
print(f'-----------metodo count----------------')
list_numbers = [33,40,33,70,33,40,80,90,33,45,18,33]
print(f'{list_numbers}')
repeated_numbers = list_numbers.count(33)
print(f'El numero (33) esta repetido estas veces {repeated_numbers}')
print(f'---------metodo list--------------')
loop_name = 'Tecnico de software'
list_string = list(loop_name)
print(f'Esta es la lista de {list_string}')
count_list = len(list_string)
print(f'Esta son la cantidad de la lista {count_list}')