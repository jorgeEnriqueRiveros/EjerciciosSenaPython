list_numbers = [10,33,40,50,70,1991,20,5]
print(f'Lista homogenea de solo un tipo de dato {list_numbers}')
list_names = ["juanjose","andrea","jorge","angel","alejandra"]
print(f'{list_names}')
miscellaneous_list = ["jorge",True,40,19.12,'A',"Riveros"]
print(f'{miscellaneous_list}')
print(f'-----impresion del indice 1 de todas las listas------')
print(f'{list_numbers[1]}')
print(f'{list_names[1]}')
print(f'{miscellaneous_list[1]}')
print(f'------imprimiendo la lista con ciclo for-------------')
for i in list_numbers:
    print(i,end=" ")
print("")
for i in list_names:
    print(i,end=" ")
print("")
for i in miscellaneous_list:
    print(i,end=" ")
print("")
print(f'----------Impresion de la lista del indice y el valor--------')
for i,valor in enumerate(list_numbers):
    print(f'indice {i} = {valor}')
print("--------------------------------------------------------------")
for i,valor in enumerate(list_names):
    print(f'indice {i} = {valor}')
print("--------------------------------------------------------------")
for i,valor in enumerate(miscellaneous_list):
    print(f'indice {i} = {valor}')
print("----------listas cambiando el indice 2-----------------------")
list_numbers[2] = 2024
print(f'{list_numbers[2]}')
list_names[2] = "software"
print(f'{list_names[2]}')
miscellaneous_list[2] = 3034
print(f'{miscellaneous_list[2]}')
print(f'-----Esto es para llamar un valor de una lista-------------')
entered_number = 33
if entered_number in list_numbers:
    print(f'El numero {entered_number} Encontrado')
else:
    print(f'El numero {entered_number} No encontrado')
print(f'-------------Buscar un dato en una lista-----------')
entered_number = 1991
index_number = list_numbers.index(entered_number)
print(f'El indice en el que se encuentra el valor {entered_number} es: {index_number}')
#crea una sublista de la list_numbers
sub_list = list_numbers[0:3]
print(f'Esta es la impresion de la sublista {sub_list}')
print(f'----------Imprimir la cantidad de datos de la lista----------')
length_list = len(list_numbers)
print(f'Esta la longitud de la lista {length_list}')
#forma para agregar un dato a la lista con la funcion append
list_numbers.append(18)
print(f'Lista con nuevo valor {list_numbers}')
print(f'--------Aqui estamos usando la funcion insert--------------')
print(f'Impresion de la lista sin agregar dato {list_numbers}')
list_numbers.insert(2,3034)
print(f'Lista agregando valor en el indice {list_numbers}')
length_list = len(list_numbers)
print(f'Esta la longitud de la lista {length_list}')
#Usando la funcion o metodo remove para eliminar un valor de la lista
list_numbers.remove(3034)
print(f'lista despues de eliminar el valor agregado antes 3034: {list_numbers}')