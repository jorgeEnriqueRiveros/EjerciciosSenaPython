# Pedimos al usuario que ingrese el número de términos deseado para la serie de Fibonacci
num_terms = int(input("Ingrese el número de términos para la serie de Fibonacci: "))

# Inicializamos los dos primeros términos de la serie
a, b = 0, 1
iterations_result = 0
# Imprimimos los términos de la serie de Fibonacci uno a uno
print("Serie de Fibonacci con", num_terms, "términos:")
for i in range(2,num_terms):
    iterations_result = a + b
    print(f'{a} + {b} = {iterations_result}')
    a = b
    b = iterations_result


