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
