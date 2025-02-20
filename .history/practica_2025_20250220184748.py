class Lista_Animales:
    def __init__(self,nombre,especie,sexo,peso):
        self.__nombre = nombre
        self.especie = especie
        self._sexo = sexo
        self.peso = peso

    def comer(self,alimento):
        print(f'{self.__nombre} esta comiendo {alimento}')
        
    def dormir(self):
        print(f'{self.__nombre} esta durmiendo')

    def correr(self):
