class Estudiante():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__List_Notas = []

        def agregar_nota(self, nota):
            self.__List_Notas.append(nota)
            self.__nota = List_Notas

        def calcular_promedio(self):
            promedio = sum(self.__nota) / len(self.__nota)
            print (f'El promedio de {self.__nombre} es {promedio}')

        def mostrar_info(self):
            print(f"👨‍🎓 Nombre: {self.__nombre}")   

