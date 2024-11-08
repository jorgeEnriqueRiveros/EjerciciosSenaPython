# Inicializamos las variables de acumulación
product_pairs = 1
odd_product = 1
# Primer ciclo para multiplicar los números pares
for number in range(2,11,2): # Solo números pares: 2, 4, 6, 8, 10
    auxiliary_multiply = product_pairs
    product_pairs *= number
    print(f'{auxiliary_multiply} * {number} = {product_pairs}')
print("------------------------------------------------------------")
# Segundo ciclo para multiplicar los números impares
for number in range(1,11,2): # Solo números impares: 1, 3, 5, 7, 9
    auxiliary_multiply = odd_product
    odd_product *= number
    print(f'{auxiliary_multiply} * {number} = {odd_product}')
# Mostramos los resultados finales
print(f"Multiplicacion de los numeros pares de 1 a 10: {product_pairs}")
print(f"Multiplicacion de los numeros impares de 1 a 10: {odd_product}")