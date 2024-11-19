#1.Crea una tupla de posiciones con precios e indica la cantidad de precios que contiene la tupla
tuple_prices = (12000,30000,40000,30000,50000,20000,30000,100000)
#count_tuple= len(tuple_prices)
print(f'Esta son la cantidad de la tupla {len(tuple_prices)}')
# 2. Imprimir el índice de un valor
price_entered = int(input(f'Ingresa el precio a buscar: \n'))
if price_entered in tuple_prices:
    print(f"El valor {price_entered} esta en el :", tuple_prices.index(price_entered))
else:
    print(f"El valor {price_entered} no se encuentra en la tupla.")
# 3. Contar cuántas veces existe un valor en la tupla
price_entered = int(input(f'Ingrese el valor a saber cuantas veces esta: \n'))
print(f"El valor {price_entered} aparece:", tuple_prices.count(price_entered), "veces en la tupla.")
# 4. Imprimir el valor máximo de la tupla
print("Valor máximo en la tupla:", max(tuple_prices))
# 5. Imprimir el valor mínimo de la tupla
print("Valor mínimo en la tupla:", min(tuple_prices))
# 6. Sumar todos los valores contenidos en la tupla
print("Suma de todos los valores en la tupla:", sum(tuple_prices))
# 7. Sumar los valores contenidos en la tupla desde el índice 1 hasta el 5
# Nota: En Python, el rango es excluyente en el índice final.
partial_sum = sum(tuple_prices[1:6])
print("Suma de los valores desde el índice 1 hasta el 5:", partial_sum)
# 8. Usar la función sorted() para ordenar de menor a mayor los precios de la tupla
sorted_prices = sorted(tuple_prices)
print(f'Precios ordenados de menor a mayor: \n'
      f'{sorted_prices}')
# 9. Crear una lista con 5 nombres y luego convertirla en una tupla
tuple_names = ["jorge", "andrea", "alejandra", "angel", "juanjose"]
print(f'Lista de nombres: \n'
      f'{tuple_names}')
names_tuple = tuple(tuple_names)
print(f'Tupla de nombres: \n{tuple_names}')