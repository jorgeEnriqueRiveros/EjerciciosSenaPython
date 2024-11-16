# Paso 1: Crear una lista de productos
list_products = ['manzanas','bananos','peras','uvas','naranjas']
print(f'Inventario inicial \n'
      f'{list_products}')
print(f'')
# Paso 2: Agregar productos al inventario
# Agrega "mangos" al final de la lista
list_products.append('mangos')
print(f'Lista despues de agregar el producto "mangos" \n'
      f'{list_products}')
print(f'')
# Agrega "bananos" en el índice 3
list_products.insert(3,'bananos')
print(f'Lista despues de agregar en el indice 3 el producto "bananos" \n'
      f'{list_products}')
print(f'')
# Imprime en qué índice está ubicado el producto "uvas"
grape_index = list_products.index('uvas')
print(f'El indice de "uvas" es: \n'
      f'', grape_index)
print(f'')
# Paso 3: Eliminar productos
# Elimina el producto "peras"
list_products.remove('peras')
print(f'Esta es la lista despues de eliminar "peras": \n'
      f'{list_products}')
print(f'')
# Elimina el último producto de la lista
list_products.pop()
print(f'Despues de eliminar el ultimo elemento de la lista: \n'
      f'{list_products}')
print(f'')
# Paso 4: Verificar existencia de un producto
# Verifica si "manzanas" está en la lista
apple_stock = 'manzanas' in list_products
print(f'¿Esta "manzanas" en la lista?', apple_stock)
print(f'')
# Paso 5: Contar productos
# Cuenta cuántas veces aparece "bananos" en la lista
quantity_apples = list_products.count('bananos')
print(f'La cantidad de "bananos": ', quantity_apples)
print(f'')
# Paso 6: Editar productos
# Cambia el valor del índice 1 por "Guanábana"
list_products[1] = 'Guanábana'
print(f'Despues de cambiar el indice 1 a "Guanábana" \n'
      f'{list_products}')
print(f'')
# Paso 7: Mostrar el inventario final
print(f'Inventario final: \n'
      f'{list_products}')