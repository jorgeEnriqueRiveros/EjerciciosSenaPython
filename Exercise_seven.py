month_entered = int(input("Por favor ingresa un numero para saber en que trimestre estas: "))

if month_entered >= 1 and month_entered <= 3:
    print(f'Te encuentras en el primer trimestre del año {month_entered}')
elif month_entered >= 4 and month_entered <= 6:
    print(f'Te encuentras en el segundo trimestre del año {month_entered}')
elif month_entered >= 7 and month_entered <= 9:
    print(f'Te encuentras en el tercer trimestre del año {month_entered}')
elif month_entered >= 10 and month_entered <= 12:
    print(f'Te encuentras en el cuarto trimestre del año {month_entered}')
else:
    print(f'Ingresaste un dato incorrecto, {month_entered} un mes del año')