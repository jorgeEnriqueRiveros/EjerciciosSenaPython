# Solicitar al usuario que ingrese un número
entered_number = int(input(f"Por favor ingresa el numero de la tabla de multiplicar que quieres saber: "))

# Usar un ciclo for para generar la tabla de multiplicar
for i in range(1,11):
    multiplication_result = entered_number * i
    # Imprimir la operación realizada en cada paso
    print(f"{entered_number} * {i} = {multiplication_result}")