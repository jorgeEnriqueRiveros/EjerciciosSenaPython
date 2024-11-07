import random

number_secret = random.randint(1,50)
number_entered = 0
contador = 0

while number_entered != number_secret:
    while True:
        number_entered = int(input("ingrese un numero de 1 a 50: "))
        if 0 < number_entered <= 50:
            break
        print("el numero ingresado no esta en el rango de 1 a 50")

    if number_entered < number_secret:
        print("El numero es Mayor al secreto")
    elif number_entered > number_secret:
        print("El numero es Menor al secreto")

    contador += 1
print(f'Felicitaciones has adivinado el numero secreto = {number_secret}'
          f' Usaste esta cantidad de intentos {contador}')