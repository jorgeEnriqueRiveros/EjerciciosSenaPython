# Pedimos al usuario que ingrese un número
entered_number = int(input(f"Por favor ingresa el numero para el factorial: "))
# Inicializamos el resultado del factorial
factor_number = 1
# Calculamos el factorial usando un ciclo for
for i in range(1, entered_number + 1):
    factorial_result = factor_number
    factor_number *= i
    if factorial_result != 1:
        print(f'{factorial_result} * {i} = {factor_number}')
# Mostramos el resultado
print(f"El factorial de {entered_number} es: {factor_number}")