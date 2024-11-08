# Inicializar la variable de suma acumulativa
cumulative_sum = 0

# Bucle for para sumar los números del 1 al 10
for number in range(1, 11):
    # Imprimir el proceso de suma
    print(f"El valor de la suma es: {cumulative_sum} + {number}")

    # Sumar el número actual a la suma acumulativa
    cumulative_sum += number

    # Imprimir el resultado actual de la suma acumulativa
    print(f"Resultado acumulado: {cumulative_sum}")