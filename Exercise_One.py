# Solicita al usuario que ingrese su primer nombre, primer apellido y año de nacimiento
name_user = input("Ingrese su primer nombre: ")
last_name = input("Ingrese su primer apellido: ")
year_of_birth = input("Ingresa tu año de nacimiento: ")

# Toma los primeros tres caracteres del nombre en minúsculas
name_part = name_user[:3].lower()
# Toma los primeros tres caracteres del apellido en minúsculas
last_name_part = last_name[:3].lower()
# Toma los últimos dos dígitos del año de nacimiento
year_of_birth_part = year_of_birth[2:]

# Combina las partes generadas para crear un correo corporativo con el dominio dado
correo = f"{name_part}{last_name_part}{year_of_birth_part}@castillalanueva.edu.co"

# Muestra el mensaje de éxito y el correo creado con una estructura de texto más organizada
print(f'''Tu email corporativo se ha creado exitosamente. 
\t\t\ttu email es:
\t{correo}
\t\t---Felicitaciones---''')

# Muestra el mensaje de éxito y el correo creado en un formato alternativo
print(f"""Tu email corporativo se ha creado exitosamente
            tu email es:
   {correo}
     ---Felicitaciones---""")
