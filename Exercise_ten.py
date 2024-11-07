# Inicializar el contador de vueltas
turns = 0

# Bucle para contar las vueltas
while turns < 10:
    # Simular una vuelta (en un caso real, esto podría ser un evento que se active)
    input("Presiona Enter para dar una vuelta...")
    turns += 1
    print(f"Vueltas completadas: {turns}")

# Mensaje cuando se cumplen las 10 vueltas
print(f"""***Felicitaciones***
has terminado la carrera""")
