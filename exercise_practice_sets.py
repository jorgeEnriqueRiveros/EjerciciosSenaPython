#los conjuntos no tienen inidices y no admiten valor duplicados y no manejan un orden de impresión
assorted_set = {'Jorge',33,40.6,True,'Angel',(33,40,70),33,'Jorge',70,True}
print(f'Este es un conjunto de varios tipos de datos:'
      f'{assorted_set}')
print(f'------Imprimir el conjunto con ciclo for')
for i in enumerate(assorted_set):
    print(f'{i}')
print(f'-----Buscando dentro del conjunto por valor------')
value_entered = (33,40,70)
if value_entered in assorted_set:
    print(f'El valor {value_entered} que ingresaste esta en el conjunto')
else:
    print(f'El valor {value_entered} que ingresaste no esta en el conjunto')
print(f'------Aqui se imprime la cantida de elementos del conjunto-------')
print(f'Esta es la cantidad de valores {len(assorted_set)} del conjunto\n'
      f'y la cantidad de valores en el conjunto no imprime los repetidos')
print(f'-------eliminar un elemento del producto---------')
assorted_set.remove('Jorge')
print(f'Este es el conjunto {assorted_set} eliminando el elemento "jorge"')
print(f'--------conjunto de numeros con el numero 5 repetido 4 veces-----')
numbers_set = {5,20,5,33,5,40,5,70,50,1991}
numbers_set.remove(5)
print(f'Este es el conjunto {numbers_set} eliminando el elemento 5 \n'
      f'pero como en los conjuntos los valores repetidos solo los deja\n'
      f'una sola vez pues solo elimina uno de los elementos')
list_numbers = list(numbers_set)
print(f'Aqui se pasa el conjunto a una lista:\n'
      f'{list_numbers}')
numbers_set = set(list_numbers)
print(f'Aqui se pasa una lista a un conjunto:\n'
      f' {numbers_set}')
string_entered = "tecnico de software"
set_string = set(string_entered)
print(f'Esto es convertir una cadena a un conjunto:\n'
      f'{set_string}')
numbers_set.add(2024)
print(f'Este es el conjunto de numero agregando un nuevo elemento:\n'
      f'{numbers_set}')
numbers_set.pop()
print(f'Este es el conjunto eliminando un valor aleatorio con pop\n'
      f'{numbers_set}')
numbers_set.add(3034)
print(f'{numbers_set}')
numbers_set.pop()
print(f'Eliminando nuevamente un valor aleatorio despues de agregar otro\n'
      f'{numbers_set}')
#eliminando valor de un conjunto mediante un for
numbers_set.clear()
print(f'Eliminando valores del conjunto con clear\n'
      f'{numbers_set}')
#Estamos convirtiendo una lista a un conjunto
list_value = [33,5,50,5,40,5,70,18,5,5]
set_value2 = set(list_value)
print(f'{set_value2}\n'
      f'',type(set_value2))
#Estamos convirtiendo una tupla a conjunto
tuple_value = ('jorge','andrea','juanjose','enrique','angel',33,40,5)
set_value = set(tuple_value)
print(f'{set_value}\n'
      f'',type(set_value))
#Vamos a empezar a usar metodos para realizar una union de varios conjuntos
print(f'Uniendo conjuntos:\n'
      f'{set_value2.union(set_value)}')
#Vamos a usar el metodo de interseccion para retornar los valores comunes ambos conjuntos
print(f'Usando intersection\n'
      f'{set_value2.intersection(set_value)}')
#Vamos a usar el metodo de diffrence para relacion los valores si son diferentes de un conjunto al otro
print(f'Usando el metodo difference\n'
      f'{set_value.difference(set_value2)}')
#Vamos a usar el metodo de symmtric_difference devuelve un nuevo conjunto con los elementos
#que podran aparecer en uno u otro conjunto pero no en ambos
print(f'Usando el metodo symmetric_difference\n'
      f'{set_value2.symmetric_difference(set_value)}')