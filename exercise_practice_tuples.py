tuple_names = ('juanjose','andrea','andres','jorge','angel')
tuple_heterogeneous = ('enrique',33,True,'software',False)
tuple_numbers = (33,70,2024,1991,20)
print(f'--------(Estas son las diferentes tuplas)-------')
print(f'Esto es una tupla de nombres \n'
      f'{tuple_names}')
print(f'Esto es una tupla de herogenea \n'
      f'{tuple_heterogeneous}')
print(f'Esto es una tupla de numeros \n'
      f'{tuple_numbers}')
print(f'-------Imprimiendo tuplas con el ciclo for y funcion enumerate-------')
for i in enumerate(tuple_names):
    print(f'{i}')
for i in tuple_numbers:
    print(f'{i}')
print(f'-------impresion de valores por indice de una tupla-------')
print(f'Valor del indice 1: {tuple_numbers[1]}')
print(f'valor del ultimo indice: {tuple_numbers[-2]}')
entered_number = int(input(f'Ingrese el numero a buscar: '))
if entered_number in tuple_numbers:
    print(f'El numero ingresado {entered_number}, existe en la tupla y esta en el indice {tuple_numbers.index(entered_number)}')
else:
    print(f'no encontramos el numero {entered_number} no se encuentra en la lista')
print(f'Esta parte es usando la funcion tuple, list para convertir')
list_numbers = [33,40,18,30,19,50,70]
tuple_number = tuple(list_numbers)
print(f'Esto es usando la funcion tuple para pasar una lista a tupla'
      f'{tuple_number}')
string_entered = input(f'Ingresa por favor una cadena para convertir a tupla: \n')
tuple_string = tuple(string_entered)
print(f'Aqui se convierte una cadena a una tupla \n'
      f'{tuple_string}')
