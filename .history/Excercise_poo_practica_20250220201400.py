class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def show_info(self):
        return f'Name: {self.__name},\n Price: {self.__price},\n Stock: {self.__stock}'

    def update_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            return f'Precio actualizado a ${new_price}'
        else:
            print("Error: El precio debe ser un valor positivo.")
    def add_stock(self, stock):
        if stock > 0:
            self.__stock += stock
            return f'Al producto {self.__name}\n Se han agregado {stock} unidades'
        else:
            print("Error: La cantidad de stock debe ser un valor positivo.")
    def buy(self, stock):
        if 0 < stock <= self.__stock:
            self.__stock -= stock
            return f'Compra exitosa de {self.__name}\n de estas {stock} unidades'
            print(f'Quedan estas unidades disponibles:\n')
            self.show_info()
        else:

buzos = Product('Tommy',)