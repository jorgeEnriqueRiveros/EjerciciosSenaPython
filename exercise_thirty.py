list_grades = []  # Inicializa una lista vacía donde se almacenarán las calificaciones de los estudiantes.

number_students = int(input("Ingrese el número de estudiantes: "))  # Solicita al usuario que ingrese el número de estudiantes y lo convierte a un entero.

for i in range(number_students):  # Comienza un bucle que se ejecutará 'number_students' veces, una por cada estudiante.
    while True:  # Inicia un bucle interno que continuará hasta que se ingrese una calificación válida.
        entered_grade = float(input(f"Ingrese la calificación del estudiante {i+1} (0-10): "))  # Solicita la calificación del estudiante actual y la convierte en un número de punto flotante (float).
        if 0 <= entered_grade <= 10:  # Verifica que la calificación esté en el rango de 0 a 10 (inclusive).
            list_grades.append(entered_grade)  # Si la calificación es válida, la agrega a la lista de calificaciones.
            break  # Sale del bucle interno, ya que se ha ingresado una calificación válida.
        else:
            print("Calificación inválida. Ingrese un valor entre 0 y 10.")  # Si la calificación no es válida, muestra un mensaje de error.

# Mostrar lista de calificaciones
print(f"Lista de calificaciones: \n"
      f"{list_grades}")  # Imprime la lista completa de calificaciones de todos los estudiantes.

# Calcular estadísticas
highest_rating = max(list_grades)  # Encuentra la calificación más alta de la lista usando la función max().
minimum_rating = min(list_grades)  # Encuentra la calificación más baja de la lista usando la función min().
average_grade = sum(list_grades) / len(list_grades)  # Calcula el promedio de las calificaciones dividiendo la suma de las calificaciones por la cantidad de estudiantes.

print(f"\nCalificación máxima: {highest_rating}")  # Imprime la calificación máxima.
print(f"Calificación mínima: {minimum_rating}")  # Imprime la calificación mínima.
print(f"Promedio: {average_grade:.2f}")  # Imprime el promedio de las calificaciones, formateado a dos decimales.

# Buscar una calificación
rating_search = float(input("\nIngrese la calificación a buscar: "))  # Solicita una calificación a buscar en la lista y la convierte a un número de punto flotante.

if rating_search in list_grades:  # Verifica si la calificación ingresada está en la lista de calificaciones.
    print(f"La calificación {rating_search} se encontró en la lista.")  # Si se encuentra, imprime un mensaje indicando que la calificación está presente.
    print(f"Aparece {list_grades.count(rating_search)} veces.")  # Cuenta cuántas veces aparece la calificación en la lista usando la función count() y la muestra.
else:
    print(f"La calificación {rating_search} no se encontró en la lista.")  # Si no se encuentra, imprime un mensaje indicando que la calificación no está en la lista.

# Ordenar las calificaciones
sorted_grades = sorted(list_grades)  # Ordena las calificaciones de menor a mayor utilizando la función sorted().
print(f'Lista de calificaciones ordenadas:\n'  # Muestra la lista de calificaciones ordenadas.
      f'{sorted_grades}')