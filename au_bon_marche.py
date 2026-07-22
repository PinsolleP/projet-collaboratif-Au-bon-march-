class Product:

    def __init__(self, name, type, price, stock, unity):
        self.name = name
        self.price = price
        self.type = type
        self.stock = stock
        self.unity = unity
        Product.append(self)
