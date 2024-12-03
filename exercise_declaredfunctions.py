def saludar():
    print(f'Hola mundo, estoy en una funcion')

#llamando a la funcion saludar()
saludar()

def saludar():
    print(f'Hola {nombre} {apellido}, esta es tu edad {edad}, estas en una funcion')

nombre = input(f'Ingresa un nombre:\n').capitalize()
apellido = input(f'Ingresa tu apellido:\n').capitalize()
edad = int(input(f'Ingresa tu edad:\n'))
saludar()

def calcular_descuento():
    precio = float(input(f'Ingresa el precio a calcular:\n'))

    descuento = precio * 0.30
    total = precio - descuento

    print(f'El descuento es: {descuento:.2f}')
    print(f'El total a pagar: {total:.2f}')

calcular_descuento()

def multiplicar():
    number1 = float(input(f'Ingresa un numero:\n'))
    number2 = float(input(f'Ingresa un nuevo numero:\n'))
    resultado = number1 * number2
    return resultado

resultado = multiplicar()
print(f'Este es el resultado de la multiplicacion: {resultado}')

def obtener_datos():

    name_user = input(f'Ingresa tu nombre:\n')
    age_user = int(input(f'Ingresa tu edad:\n'))
    number_phone = int(input(f'Ingresa tu telefono:\n'))

    return [name_user,age_user,number_phone]

datos = obtener_datos()
print(f'Datos ingresados: {datos}')
