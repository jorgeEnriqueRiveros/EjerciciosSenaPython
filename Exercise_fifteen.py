# Pedimos al usuario un correo electrónico
entered_email = input("Ingresa tu correo electrónico: ")

# Inicializamos el ciclo while para comparar las contraseñas
while True:
    # Pedimos la contraseña
    password_entered = input("Ingresa tu contraseña: ")
    # Realizamos la confirmación de la contraseña
    confirm_password = input("Por favor confirma tu contraseña: ")
    if password_entered == confirm_password:
        break
    else:
        print("Las contraseñas no coinciden. Debes confirmar las contraseñas correctamente.")

# Continuamos solicitando los demás datos para el registro
name_user = input("Por favor ingresa tus nombres: ")
first_surname = input("Por favor ingresa tu primer apellido: ")
second_lastname = input("Por favor ingresa tu segundo apellido: ")
document_number = input("Por favor ingresa tu número de documento: ")
post = input("Por favor ingresa tu cargo: ")

# Confirmamos el registro exitoso
print("¡Felicitaciones, registro exitoso!")

# Guardamos los datos del usuario
registered_user = {
    "correo": entered_email,
    "contraseña": password_entered,
    "nombres": name_user,
    "primer_apellido": first_surname,
    "segundo_apellido": second_lastname,
    "numero_documento": document_number,
    "cargo": post
}

print("\n---- Inicio de Sesión ----")

# El ciclo se repetirá hasta que el correo y la contraseña sean correctos
while True:
    entered_email = input("Ingresa tu correo para iniciar sesión: ")
    password_entered = input("Ingresa tu contraseña para iniciar sesión: ")

    if entered_email == registered_user["correo"] and password_entered == registered_user["contraseña"]:
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Correo o contraseña incorrectos. Inténtalo de nuevo.")

# Mostrar los datos del usuario después de iniciar sesión
print("\n---- Datos del Usuario ----")
print(f"Correo: {registered_user['correo']}")
print(f"Nombres: {registered_user['nombres']}")
print(f"Primer apellido: {registered_user['primer_apellido']}")
print(f"Segundo apellido: {registered_user['segundo_apellido']}")
print(f"Número de documento: {registered_user['numero_documento']}")
print(f"Cargo: {registered_user['cargo']}")