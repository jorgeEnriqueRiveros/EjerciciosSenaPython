have_vacation = input("¿Tienes vacaciones? (True/False): ")
have_vacation = (have_vacation.lower() == 'true')

its_weekend = input("¿Es fin de semana? (True/False): ")
its_weekend = (its_weekend.lower() == 'true')

if have_vacation or its_weekend:
    print(f'¡Puedes ir a pescar!')
else:
    print(f'No puedes ir a pescar')