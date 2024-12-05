from mathematical_operations_exercise_thirtysix import operation_subtraction, operation_divide,operation_multiply, opoperation_sum
import exercise_thirtysix_messages

def main():
    exercise_thirtysix_messages.greet_calculator()

    # Solicitar al usuario la operación y los números
    while True:
        print(f'Operaciones disponibles:\n'
              f'1. suma\n'
              f'2. resta\n'
              f'3. multiplicacion\n'
              f'4. division\n'
              f'5. salir')
        menu_operations = int(input(f'Elige una operacion: \n'))

        if menu_operations == 5:
            print(f'Has salido de la calculadora')
            break
        elif menu_operations in [1, 2, 3, 4]:
            num1 = float(input(f'Introduce el primer numero: '))
            num2 = float(input(f'Introduce el segundo numero: '))

            if menu_operations == 1:
                total_result = print(f'El resultado de la suma es:\n'
                                     f'{opoperation_sum(num1,num2)}')
            elif menu_operations == 2:
                total_result = print(f'El resultado de la resta es:\n'
                                     f'{operation_subtraction(num1,num2)}')
            elif menu_operations == 3:
                total_result = print(f'El resultado de la multiplicacion es:\n'
                                     f'{operation_multiply(num1,num2)}')
            elif menu_operations == 4:
                total_result = print(f'El resultado de la division es:\n'
                                     f'{operation_divide(num1,num2)}')

            exercise_thirtysix_messages.show_result(total_result)
        else:
            print("Operacion no valida")

if __name__ == '__main__':
    main()
