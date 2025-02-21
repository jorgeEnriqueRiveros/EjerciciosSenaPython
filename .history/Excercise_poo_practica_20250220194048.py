class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def show_info(self):
        return f'Name: {self.__name}, Price: {self.__price}, Stock: {self.__stock}'

    def update_price(self, new_price):
        pass

    def add_stock(self, stock):
        pass

    def buy(self, stock):
        pass