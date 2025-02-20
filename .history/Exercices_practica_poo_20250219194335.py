class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.__titular = titular
        self.__saldo, = saldo
    def depositar(self,monto:)
        self.__saldo += monto

    def retirar(self,monto:)
        if monto > self.__saldo:
            print("Fondos insuficientes")
        else:
            self.__saldo -= monto
            print(f"Retiro exitoso Retiraste ${monto}.\n Saldo actual: ${self.__saldo}')
    def mostrar_saldo():
        pass
    def mostrar_titular():
        pass