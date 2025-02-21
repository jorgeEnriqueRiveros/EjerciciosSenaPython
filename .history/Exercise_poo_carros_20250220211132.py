class Lista_carros():
    def __init__(self, marca, modelo, velocidad, combustible):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__combustible = combustible
        
    def acelerar(self, cantidad):
        self.__velocidad += cantidad
        print(f'El carro aceleró a {self.__velocidad} km/h')
        
    def frenar(self, cantidad):
        self.__velocidad -= cantidad
        print(f'El carro frenó a {self.__velocidad} km/h')
        
    def repostar()    
