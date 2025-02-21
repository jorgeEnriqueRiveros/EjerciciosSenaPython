class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def show_info(self):
        return f'Name: {self.__name}, Price: {self.__price}, Stock: {self.__stock}'

    def update_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            return f'Precio actualizado a ${new_price}'
        else:
            return
    def add_stock(self, stock):
        return f'Se han agregado {stock} unidades al stock.'

    def buy(self, stock):
        return f'se han vendido {stock}' 