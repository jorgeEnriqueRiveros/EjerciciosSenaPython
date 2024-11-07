while True:
    # Solicitar el valor de las compras
    shopping_value = float(input("Ingrese el valor de sus compras: $ "))
    # Solicitar el tipo de tarjeta
    card_type = int(input("Ingrese el tipo de tarjeta (1, 2, 3 o 4): "))

    # Verificar el tipo de tarjeta y calcular el descuento
    if card_type == 1:
        discount = 0.05
    elif card_type == 2:
        discount = 0.10
    elif card_type == 3:
        discount = 0.15
    elif card_type == 4:
        discount = 0.20
    else:
        print("Tipo de tarjeta no válido.")
        continue  # Si el tipo de tarjeta no es válido, continuar con la siguiente iteración

    # Calcular el valor del descuento
    discount_amount = shopping_value * discount

    # Calcular el valor total con descuento
    total_value = shopping_value - discount_amount

    # Imprimir los resultados
    print(f"Descuento: ${discount_amount:.2f}")
    print(f"Valor total con descuento: ${total_value:.2f}")

    # Preguntar al usuario si desea continuar o salir
    continue_shopping = input("¿Desea continuar? (Escriba 'salir' para salir): ").strip()

    if continue_shopping.lower() == 'salir':
        print("Gracias por su compra. ¡Hasta pronto!")
        break
