class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.__titular = titular
        self.__saldo = saldo
    def depositar(self,monto):
        self.__saldo += monto
        print(f'Deposito exitoso depositaste ${monto}.\n Saldo actual: ${self.__saldo}')
    def retirar(self,monto):
        if monto > self.__saldo:
            print("Fondos insuficientes")
        else:
            self.__saldo -= monto
            print(f'Retiro exitoso Retiraste ${monto}.\n Saldo actual: ${self.__saldo}')
    def mostrar_saldo(self):
        print(f'Mostrar saldo: ${self.__saldo}')
    def mostrar_titular(self):
        pass

cuenta1 = CuentaBancaria("Jorge riveros", 100000)
cuenta1.depositar(50000)