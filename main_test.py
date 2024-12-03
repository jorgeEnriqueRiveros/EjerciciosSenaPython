import test_module


number1 = float(input(f'Ingrese el primer numero:\n'))
number2 = float(input(f'Ingrese el segundo numero:\n'))

suma = test_module.operation_sum(number1,number2)*1.20
restar = test_module.operation_subtract(number1,number2)*1.20
multiplicar = test_module.operation_multiply(number1,number2)*1.20
dividir = test_module.operation_divide(number1,number2)

#Mostrar resultados
print(f'Este es el resultado de la suma con 20% adicional: {suma}')
print(f'Este es el resultado de la resta con 20% adicional: {restar}')
print(f'Este es el resultado de la multiplicacion con 20% adicional: {multiplicar}')
if isinstance(dividir, str):
    print(f'Resultado de la division: {dividir}')
else:
    print(f'Resultado de la division con 20% adicional: {dividir * 1.20}')

# Importar funciones específicas usando from (descomenta las siguientes líneas para probar)
# from modulo_prueba import sumar, multiplicar, dividir

# Invocar las funciones con la nueva importación
# suma = sumar(num1, num2) * 1.20
# multiplicacion = multiplicar(num1, num2) * 1.20
# division = dividir(num1, num2)

# Mostrar resultados (la resta no está disponible y generará un error si se intenta utilizar)
# print(f"Resultado de la suma con 20% adicional (nueva importación): {suma}")
# print(f"Resultado de la multiplicación con 20% adicional (nueva importación): {multiplicacion}")
# if isinstance(division, str):  # Verifica si hay un mensaje de error
#     print(f"Resultado de la división: {division}")
# else:
#     print(f"Resultado de la división con 20% adicional (nueva importación): {division * 1.20}")
