class Lista_carros():
    def __init__(self, marca, modelo, velocidad, combustible):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = 0 # el carro inicia detenido
        self.__combustible = combustible
        
    def acelerar(self, cantidad):
        if self.__combustible 
        
    def frenar(self, cantidad):
        self.__velocidad -= cantidad
        print(f'El carro frenó a {self.__velocidad} km/h')
        
    def repostar(self, litros):
        if self.__combustible - litros >= 0:
            self.__combustible -= litros
            print(f'El carro repostó {litros} litros de combustible')
        else:
            print('No hay suficiente combustible')
    def mostrar_info(self):
        print(f"🚗 Marca: {self.__marca}")
        print(f"📊 Modelo: {self.__modelo}")
        print(f"💨 Velocidad: {self.__velocidad} km/h")
        print(f"⛽ Combustible: {self.__combustible} litros")            
