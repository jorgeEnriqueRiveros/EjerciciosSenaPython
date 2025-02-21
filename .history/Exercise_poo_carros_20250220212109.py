class Lista_carros():
    def __init__(self, marca, modelo, velocidad, combustible):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__combustible = combustible
        
    def acelerar(self, cantidad):
        if self.__combustible <= 0:
            print("❌ No puedes acelerar, combustible agotado.")
            return
        self.__velocidad += cantidad
        consumo = cantidad // 10
        self.__combustible -= consumo

        if self.__combustible < 0:
            self.__combustible = 0
        print(f"🚀 Acelerando {cantidad} km/h.")    
        
    def frenar(self, cantidad):
        self.__velocidad -= cantidad
        print("🛑 El coche se ha detenido.")
        
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

if __name__ == "__main__":
    # Crear un coche
    mi_coche = Lista_carros('Toyota', 'Corolla', 50, 1000
                            )

    # Mostrar información inicial
    mi_coche.mostrar_info()

    # Acelerar y mostrar información
    mi_coche.acelerar(60)
    mi_coche.mostrar_info()

    # Frenar el coche
    mi_coche.frenar()
    mi_coche.mostrar_info()

    # Repostar combustible
    mi_coche.repostar(20)
    mi_coche.mostrar_info()
