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
            print("Error: El precio debe ser un valor positivo.")
    def add_stock(self, stock):
        if stock > 0:
            self.__stock += stock
            return f'Al producto Se han agregado {stock} unidades'

    def buy(self, stock):
        if 0 < stock <= self.__stock:
            self.__stock -= stock
            return f'Compra exitosa de {self.__name}, de estas {stock} unidades'