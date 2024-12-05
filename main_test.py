from test_module import operation_sum, operation_multiply, operation_divide, operation_subtract


number1 = float(input(f'Ingrese el primer numero: \n'))
number2 = float(input(f'Ingrese el segundo numero: \n'))

suma = operation_sum(number1,number2)
restar = operation_subtract(number1,number2)*0.20
multiplicar = operation_multiply(number1,number2)*0.20
dividir = operation_divide(number1,number2)

resultado1 = suma + (suma*0.2)
resultado2 =  restar + (restar*0.2)
resultado3 = multiplicar + (multiplicar*0.2)
resultado4 = dividir + (dividir*0.2)

#Mostrar resultados
print(f'Este es el resultado de la {suma} con 20% adicional: {resultado1}')
print(f'Este es el resultado de la {restar} con 20% adicional: {resultado2}')
print(f'Este es el resultado de la {multiplicar} con 20% adicional: {resultado3}')
if isinstance(dividir, str):
    print(f'Resultado de la division: {dividir}')
else:
    print(f'Resultado de la {dividir} con 20% adicional: {resultado4}')

# Importar funciones específicas usando from (descomenta las siguientes líneas para probar)
# from modulo_prueba import sumar, multiplicar, dividir

# Invocar las funciones con la nueva importación
# suma = sumar(num1, num2) * 0.20
# multiplicacion = multiplicar(num1, num2) * 0.20
# division = dividir(num1, num2)

# Mostrar resultados (la resta no está disponible y generará un error si se intenta utilizar)
# print(f"Resultado de la suma con 20% adicional (nueva importación): {suma}")
# print(f"Resultado de la multiplicación con 20% adicional (nueva importación): {multiplicacion}")
# if isinstance(division, str):  # Verifica si hay un mensaje de error
#     print(f"Resultado de la división: {division}")
# else:
#     print(f"Resultado de la división con 20% adicional (nueva importación): {division * 0.20}")