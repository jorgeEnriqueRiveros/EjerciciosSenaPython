class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def show_info(self):
        return f'Name: {self.__name}, Price: {self.__price}, Stock: {self.__stock}'

    def update_price(self, new_price):
        if new_price > 0:
            self.__price = nuevo_precio
        else:
            print("Error: El precio debe ser un valor positivo.")
    def add_stock(self, stock):
        return f'Se han agregado {stock} unidades al stock.'

    def buy(self, stock):
        return f'se han vendido {stock}' 