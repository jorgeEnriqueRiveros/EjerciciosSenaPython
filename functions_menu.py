def saludar(name_user):
    """Saluda a la persona recibida como parametro."""
    print(f'Hola, {name_user}! Bienvenido/a.')

def calcular_anio_nacimiento(age_user):
    from datetime import datetime
    anio_actual = datetime.now().year
    anio_nacimiento = anio_actual - age_user
    return anio_nacimiento

def mostrar_menu_hamburguesas():
    """Muestra un menu de hamburguesas y retorna la seleccion del usuario."""
    while True:
        print(f'\nMenu hamburguesas:')
        print(f'1. Hamburguesa clasica')
        print(f'2. Hamburguesa doble queso')
        print(f'3. Hamburguesa vegana')
        print(f'4. Salir del menu')

        burger_menu = int(input(f'Selecciona una hamburguesa del menu: '))

        if burger_menu == 1:
            return "hamburguesa clasica"
        elif burger_menu == 2:
            return "hamburguesa doble queso"
        elif burger_menu == 3:
            return "hamburguesa vegana"
        elif burger_menu == 4:
            print(f'Has salido del menu hamburguesas')
            break
        else:
            print(f'Has seleccionado una opcion no valida')


if __name__ == '__main__':
    name_user = input(f'Por favor ingresa tu nombre:\n ')
    saludar(name_user)
    age_user = int(input(f'¿Cual es tu edad?\n'))
    print(f'Tu año de nacimiento es: {calcular_anio_nacimiento(age_user)}')
    print(f'Has seleccionado la {mostrar_menu_hamburguesas()}')