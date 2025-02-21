class Estudiante():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__List_Notas = []

        def agregar_nota(self, nota):
            if not isinstance(nota, (int, float)):
                print('La nota debe ser un número.')
                return
            self.__List_Notas.append(nota)
            print(f'La nota {nota} ha sido agregada correctamente.')

        def calcular_promedio(self):
            promedio = sum(self.__List_Notas) / len(self.__)
            print (f'El promedio de {self.__nombre} es {promedio}')

        def mostrar_info(self):
            print(f"👨‍🎓 Nombre: {self.__nombre}")   

