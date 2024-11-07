

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
number_entered = int(input("Por favor ingresa un numero para el menu"))
if number_entered == 1:
    print("Opcion 1 del menu: ")
elif number_entered == 2:
    print("Opcion 2 del menu: ")
elif number_entered == 3:
    print("Opcion 3 del menu: ")
elif number_entered == 4:
    print("Opcion 4 del menu: ")