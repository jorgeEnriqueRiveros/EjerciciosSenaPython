# Creamos dos conjuntos vacíos:
# 'set_quotes' para almacenar las personas con citas asignadas y 'attended_set' para las personas atendidas.
set_quotes = set()
attended_set = set()

# Creamos un menú interactivo usando un bucle 'while True' para mostrar las opciones hasta que el usuario decida salir.
while True:
    # Mostramos el menú principal con las opciones disponibles.
    print(f'\n---Menú de citas---')
    print(f'1. Sacar citas')
    print(f'2. Atender paciente')
    print(f'3. Mostrar personas con citas')
    print(f'4. Mostrar personas atendidas')
    print(f'5. Mostrar personas pendientes por atender')
    print(f'6. Buscar personas en citas')
    print(f'7. Salir')

    # Solicitamos al usuario que seleccione una opción del menú.
    menu_appointments = int(input(f'Selecciona una opcion:  \n'))

    # Opción 1: Asignar una cita a un paciente.
    if menu_appointments == 1:
        # Verificamos si el número máximo de citas (10) ya ha sido alcanzado.
        if len(set_quotes) < 10:
            # Solicitamos el nombre del paciente, eliminamos espacios y lo convertimos a minúsculas para uniformidad.
            patient_name = input(f'Ingresa el nombre del paciente para asignarle la cita: \n').strip().lower()
            # Agregamos el nombre del paciente al conjunto de citas asignadas.
            set_quotes.add(patient_name)
            print(f'Cita asignada al paciente {patient_name}')
        else:
            # Mensaje si ya se alcanzó el límite máximo de citas para el día.
            print(f'Ya se alcanzo el limite maximo de citas para el dia (10).')

    # Opción 2: Atender a un paciente con cita asignada.
    elif menu_appointments == 2:
        # Verificamos si hay pacientes con citas pendientes.
        if set_quotes:
            # Solicitamos el nombre del paciente que será atendido.
            patient_name = input(f'Ingresa el nombre del paciente que sera atendido: \n').strip().lower()
            # Verificamos si el paciente tiene cita asignada.
            if patient_name in set_quotes:
                # Removemos al paciente del conjunto de citas y lo agregamos al conjunto de atendidos.
                set_quotes.remove(patient_name)
                attended_set.add(patient_name)
                print(f'{patient_name} ha sido atendido el paciente.')
            else:
                # Mensaje si el paciente no tiene cita asignada.
                print(f'{patient_name} no tiene cita asignada. ')
        else:
            # Mensaje si no hay citas pendientes.
            print(f'No hay pacientes con citas pendientes. ')

    # Opción 3: Mostrar las personas que tienen citas asignadas.
    elif menu_appointments == 3:
        print(f'\n Personas con citas en el dia: \n')
        # Mostramos los nombres de las personas con citas o un mensaje si no hay citas asignadas.
        print(", ".join(set_quotes) if set_quotes else "No hay personas con cita.")

    # Opción 4: Mostrar las personas que ya fueron atendidas.
    elif menu_appointments == 4:
        print(f'\nPersonas atendidas en el dia: \n')
        # Mostramos los nombres de las personas atendidas o un mensaje si no se ha atendido a nadie.
        print(", ".join(attended_set) if attended_set else "No se ha atendido ninguna persona. ")

    # Opción 5: Mostrar las personas pendientes por atender (tienen cita, pero no han sido atendidas).
    elif menu_appointments == 5:
        # Calculamos las personas pendientes como la diferencia entre 'set_quotes' y 'attended_set'.
        pending_appointments = set_quotes - attended_set
        print(f'Personas pendientes por atender: \n')
        # Mostramos los nombres de las personas pendientes o un mensaje vacío si no hay pendientes.
        print(", ".join(pending_appointments) if pending_appointments else "")

    # Opción 6: Buscar el estado de una persona específica (con cita, atendida o sin cita).
    elif menu_appointments == 6:
        # Solicitamos el nombre de la persona a buscar.
        patient_name = input(f'Ingresa el nombre de la persona que deseas buscar: \n').strip().lower()
        # Verificamos si la persona ya fue atendida.
        if patient_name in attended_set:
            print(f'{patient_name} El paciente ya fue atendido.')
        # Verificamos si la persona tiene cita, pero no ha sido atendida.
        elif patient_name in set_quotes:
            print(f'{patient_name} Esta pendiente por atender.')
        # Mensaje si la persona no tiene cita asignada.
        else:
            print(f'{patient_name} no saco cita en el dia.')

    # Opción 7: Salir del programa.
    elif menu_appointments == 7:
        # Mostramos un mensaje de despedida y salimos del bucle.
        print(f'Saliendo del programa. ¡Hasta luego!.')
        break

    # Mensaje si la opción ingresada no es válida.
    else:
        print(f'Opcion invalida. Intenta de nuevo')
