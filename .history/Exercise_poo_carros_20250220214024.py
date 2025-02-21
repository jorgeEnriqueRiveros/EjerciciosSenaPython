class Coche:
    def __init__(self, marca, modelo, combustible):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = 0  # El coche inicia detenido
        self.__combustible = combustible

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    def mostrar_info(self):
        print(f"🚗 Marca: {self.__marca}")
        print(f"📊 Modelo: {self.__modelo}")
        print(f"💨 Velocidad: {self.__velocidad} km/h")
        print(f"⛽ Combustible: {self.__combustible} litros")

    def acelerar(self, cantidad):
        if self.__combustible <= 0:
            print("❌ No puedes acelerar, combustible agotado.")
            return

        self.__velocidad += cantidad
        consumo = cantidad // 10  # 1 litro por cada 10 km/h
        self.__combustible -= consumo

        if self.__combustible < 0:
            self.__combustible = 0

        print(f"🚀 Acelerando {cantidad} km/h.")

    def frenar(self):
        self.__velocidad = 0
        print("🛑 El coche se ha detenido.")

    def repostar(self, litros):
        if litros > 0:
            self.__combustible += litros
            print(f"⛽ Repostado con {litros} litros.")
        else:
            print("❌ No se puede añadir una cantidad negativa de combustible.")

# Crear un coche
mi_coche = Coche("Toyota", "Corolla", 50)

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

# Cambiar la marca del coche
mi_coche.marca = "Honda"

# Mostrar información modificada
# mi_coche.mostrar_info()