# Inicializar la variable de sumatoria
summation = 0

# Bucle para solicitar números al usuario
while True:
    # Pedir al usuario que ingrese un número
    number_entered = int(input("Ingresa un número entero positivo (0 para salir): "))

    # Verificar si el número es 0 para salir del bucle
    if number_entered == 0:
        break
    # Verificar si el número es positivo
    elif number_entered > 0:
        summation += number_entered
    else:
        print("Por favor, ingresa un número entero positivo o 0 para salir.")

# Imprimir la sumatoria total
print(f"La sumatoria de los números ingresados es: {summation}")
