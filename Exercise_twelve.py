import random

# Generar número secreto aleatorio entre 1 y 50
numero_secreto = random.randint(1, 50)

intentos = 0
adivinado = False

print("¡Adivina el número entre 1 y 50!")

# Bucle hasta que el número sea adivinado
while not adivinado:
    intento = int(input("Introduce tu intento: "))
    intentos += 1

    if intento < numero_secreto:
        print("El número es mayor.")
    elif intento > numero_secreto:
        print("El número es menor.")
    else:
        adivinado = True
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")