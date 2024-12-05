def contar_caracteres(string_entered):
    """Cuenta el numero de caracteres de una cadena"""
    return len(string_entered)

def crear_y_confirmar_contrasenas():
    """Permite crear y confirmar contraseñas"""
    contrasena = input(f'Crea una contraseña: \n')
    confirmacion = input(f'Confirma tu contraseña: \n')
    if contrasena == confirmacion:
        print(f'Contraseña confirmada')
        return contrasena
    else:
        print(f'Contraseñas no coinciden')
        return None

if __name__ == '__main__':
    string_entered = input(f'Escribe un texto:\n')
    print(f'El texto tiene {contar_caracteres(string_entered)} caracteres.')
    crear_y_confirmar_contrasenas()