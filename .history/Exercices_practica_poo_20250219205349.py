class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.__titular = titular
        self.__saldo = saldo
    def depositar(self,monto):
        self.__saldo += monto
        print(f'Deposito exitoso depositaste ${monto}.\nSaldo actual: ${self.__saldo}')
    def retirar(self,monto):
        if monto > self.__saldo:
            print("Fondos insuficientes")
        else:
            self.__saldo -= monto
            print(f'Retiro exitoso Retiraste ${monto}.\n Saldo actual: ${self.__saldo}')
    def mostrar_saldo(self):
        print(f'Saldo actual:${self.__saldo}')

    def mostrar_titular(self):
        print(f'Titular de la cuenta: {self.__titular}')

cuenta1 = CuentaBancaria("Jorge riveros", 100000)
cuenta1.depositar(50000)
cuenta1.mostrar_titular()
cuenta2 = CuentaBancaria("Jennfier riveros", 250000)
cuenta2.depositar(300000)
cuenta2.mostrar_saldo()