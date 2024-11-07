# Solicitar al usuario que ingrese un número
numero = float(input("Ingresa un número: "))

#Estructura if para verificar el número
if numero > 0:
    print(f'El numero ingresado {numero} es positivo')
elif numero < 0:
    print(f'El numero ingresado {numero} es negativo')
else:
    print(f'El numero ingresado {numero} es cero')