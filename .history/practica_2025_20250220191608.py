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

    def __correr(self):
        print(f'{self.__nombre} esta corriendo')

if __name__ == '__main__':
    animal1 = Lista_Animales('Paluza','Caballo','Macho',15)
    animal2 = Lista_Animales('Lola','Conejo','Hembra',5)
    animal3 = Lista_Animales('Firulais','Perro','Macho',10)
    animal4 = Lista_Animales('Chester','Gato','Macho',7)

    animal4.dormir()
    animal3.comer('croquetas')


