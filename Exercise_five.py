# Solicitar al usuario el número de kilómetro en el que se encuentra
kilometro = int(input("Ingrese el número de kilómetro en el que se encuentra: "))

# Verificar en qué municipio se encuentra según el kilómetro usando el operador and
if kilometro >= 0 and kilometro <= 10:
    print("Estás en el municipio de Castilla la Nueva.")
elif kilometro >= 11 and kilometro <= 20:
    print("Estás en el municipio de Guamal.")
elif kilometro >= 21 and kilometro <= 30:
    print("Estás en el municipio de Acacías.")
elif kilometro >= 31 and kilometro <= 40:
    print("Estás en el municipio de Villavicencio.")
else:
    print("Ubicación desconocida.")
