# Lista para almacenar los estudiantes como tuplas
student_list = []

while True:  # Simulación de un do-while
    # Mostrar el menú
    print("\n--- Menú de Opciones ---")
    print("1. Agregar estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Estudiante con mejor promedio")
    print("5. Salir")

    # Solicitar opción al usuario
    menu_students = input("Selecciona una opción: ")

    if menu_students == "1":  # Agregar estudiante
        print("\n--- Agregar Estudiante ---")
        student_name = input("Nombre completo: ").strip().lower()
        student_age = int(input("Edad: "))

        # Validar que el promedio esté en el rango de 1 a 5
        while True:
            student_average = float(input("Promedio final (entre 1 y 5): "))
            if 1 <= student_average <= 5:
                break  # Salir del bucle si el promedio es válido
            else:
                print("El promedio debe estar entre 1 y 5. Inténtalo de nuevo.")

        # Crear la tupla y agregarla a la lista
        tuple_students = (student_name, student_age, student_average)
        student_list.append(tuple_students)
        print(f"Estudiante {student_name} agregado correctamente.")

    elif menu_students == "2":  # Listar estudiantes
        print("\n--- Lista de Estudiantes ---")
        if not student_list:
            print("No hay estudiantes registrados.")
        else:
            for i, estudiante in enumerate(student_list):
                print(f"{i + 1}. Nombre: {estudiante[0]}, Edad: {estudiante[1]}, Promedio: {estudiante[2]}")

    elif menu_students == "3":  # Buscar estudiante por nombre
        print("\n--- Buscar Estudiante ---")
        student_name = input("Nombre del estudiante a buscar: ").strip().lower()
        student_found = False
        for estudiante in student_list:
            if estudiante[0] == student_name:  # Comparar nombres
                print(f'Estudiante encontrado: \n'
                      f'Nombre: {estudiante[0]}, Edad: {estudiante[1]}, Promedio: {estudiante[2]}')
                student_found = True
                break
        if not student_found:
            print("Estudiante no encontrado.")

    elif menu_students == "4":  # Estudiante con mejor promedio
        print("\n--- Estudiante con Mejor Promedio ---")
        if not student_list:
            print("No hay estudiantes registrados.")
        else:
            estudiante = max(student_list, key=lambda x: x[2])  # Comparar por promedio
            print(f"El estudiante con el mejor promedio es {estudiante[0]} con un promedio de {estudiante[2]}.")

    elif menu_students == "5":  # Salir
        print("Saliendo del programa. ¡Hasta luego!")
        break  # Salir del bucle

    else:
        print("Opción no válida. Inténtalo de nuevo.")