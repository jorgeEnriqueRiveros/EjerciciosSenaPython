class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def mostrar_info(self):
        pass

    def update_price(self, price