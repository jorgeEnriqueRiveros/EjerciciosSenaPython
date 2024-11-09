a , b = 33, 1991
a = a + 1
print("esta es la secuencia de a",a)
a -= 3
print("Este es el valor de a Restando 2 = ",a)
b *= 3
print("Este es el valor de b Multiplicado por 3 =",b,type(b))
b /= 3
print("Este es el valor de b divido en 3 = ",b,type(b))
a += b
print("Este es el valor de a Sumando el valor de b = ",a,type(a))
resultado = 1991 // 33
print("Este es el resultado de division con entero: ",resultado,type(resultado))
resultado = 1991 > 33
print(resultado,type(resultado))
resultado = 1991 != 33
print(f"""Valor de "a" : {a} 
Valor de "b" : {b}""",resultado,type(resultado))
resultado = 1991 == 33
print(f"""Esta es la comparacion de "1991": {1991} y "33": {33}""",type(resultado))
resultado = "Jorge" < "Angel"
print(resultado,type(resultado))
resultado = 1991 >= 33
print(resultado,type(resultado))
resultado = 33 <= 1991
print(resultado,type(resultado))
print(f"----------Ciclo while de 5 a 0---------------")
contador = 0
valor_max = 5
while contador <= valor_max:
    print(f'Esta es la secuencia del while {valor_max}')
    valor_max -=1
print(f"----------Ciclo while de 0 a 5---------------")
contador = 0
valor_max = 5
while contador <= valor_max:
    print(f'Esta es la secuencia del while {contador}')
    contador +=1
print(f'----------Ciclio Dowhile---------------------')
contador = 0
valor_max = 5
while True:
    print(f'Esta es la secuencia del while {contador}')
    contador +=1
    if contador > valor_max:
        break
print(f'------------Switch o segun-------------------')
number_entered = int(input(f"Por favor ingresa un numero para el menu: "))
if number_entered == 1:
    print("Opcion 1 del menu: ")
elif number_entered == 2:
    print("Opcion 2 del menu: ")
elif number_entered == 3:
    print("Opcion 3 del menu: ")
elif number_entered == 4:
    print("Opcion 4 del menu: ")
print(f'----------Ciclo For con range de 0 a 5-----------')
for i in range(5+1):
    print(i)
print(f'-------------ciclo for con una cadena sin salto de linea-------------')

for i in "Software":
    print(i, end="")
print("")
print(f'-------------ciclo for con una lista---------------------')
list_number = [3,5,15,18,21,24]
for i in list_number:
    print(i,end="")
print("")
print(f'-------Impresion de una lista-------------')
numeros = [20,33,50,70,19,16,5]
print(f'Esta es una lista de numeros: {numeros}')
print(f'------Accediendo a un indice---------')
print(f'El valor del indice 4 = {numeros[4]}')
print(f'-------cambiando datos de una lista--------')
numeros[1] = 100
print(f'Esta es una lista de numeros: {numeros}')
print(f'-------cambiando datos del indice por consola:')
indice = int(input('Por favor ingresa el indice que quieres modificar: '))
numeros[indice] = 203
print(f'Esta es la lista modificando el valor por consola: {numeros}')
print(f'--------sumando un valor a un indice-----------------')
numeros[2] = numeros[2] + 300
print(f'Esta es la lista modificando el valor por consola: {numeros}')
print(f'El valor del indice 3 = {numeros[3]}')
print(f'---------Impresion de la lista con ciclo for-----------------')
for i in enumerate(numeros):
    print(f'{i}')
print(f'----------Impresion de la lista del indice y el valor--------')
for i,valor in enumerate(numeros):
    print(f'indice {i} = {valor}')



