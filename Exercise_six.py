note_entered = float(input("Por favor ingresa una nota para registrar: "))

if note_entered >= 0 and note_entered <= 5:
    print(f'Tu nota es insuficiente {note_entered}')
elif note_entered >= 6 and note_entered <= 7.5:
    print(f'Tu nota es aceptable {note_entered}')
elif note_entered >= 7.5 and note_entered <= 8.9:
    print(f'Tu nota es alta {note_entered}')
elif note_entered >= 9 and note_entered <= 10:
    print(f'Tu nota es excelente {note_entered}')
else:
    print(f'Error: puntuacion fuera de rango')
