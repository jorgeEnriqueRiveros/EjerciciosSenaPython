# Pedimos al usuario que ingrese una palabra
word = input("Ingrese una palabra: ")
# Definimos las vocales
vowels = "aeiou"
count = 0
# Usamos un ciclo for con enumerate para recorrer cada letra con su índice
for letter in word.lower():
        if letter in vowels:
    # Sumamos 1 si la letra es una vocal (True se cuenta como 1 en Python)
            count += 1
# Mostramos el resultado
print("La cantidad de vocales en la palabra es:", count)