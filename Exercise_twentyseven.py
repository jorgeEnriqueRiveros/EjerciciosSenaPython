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
print(f"La cantidad de vocales en la palabra '{word}' es: {count}")

def contar_letras(palabra):
  """Cuenta las vocales y consonantes en una palabra.

  Args:
    palabra: La palabra a analizar.

  Returns:
    Una tupla con el número de vocales y consonantes.
  """

  vocales = "aeiouáéíóú"
  consonantes = "bcdfghjklmnñpqrstvwxyz"
  contador_vocales = 0
  contador_consonantes = 0

  for letra in palabra.lower():  # Convertimos a minúsculas para facilitar la comparación
    if letra in vocales:
      contador_vocales += 1
    elif letra in consonantes:
      contador_consonantes += 1

  return contador_vocales, contador_consonantes

# Pedimos al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# Llamamos a la función y obtenemos los resultados
num_vocales, num_consonantes = contar_letras(palabra)

# Imprimimos los resultados
print("La palabra", palabra, "tiene:")
print(num_vocales, "vocales")
print(num_consonantes, "consonantes")