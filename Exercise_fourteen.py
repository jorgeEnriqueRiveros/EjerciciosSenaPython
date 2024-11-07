# Simulamos un ciclo Do-While
while True:
    # Pedimos al usuario que ingrese un número
    number_entered = int(input("Ingresa un número entre 1 y 20: "))

    # Verificamos si el número está en el rango de 1 a 20
    if 1 <= number_entered <= 20:
        break  # Si el número es válido, salimos del ciclo

# Imprimimos el mensaje de validación cuando el número es correcto
print(f'Numero validado = {number_entered}')
