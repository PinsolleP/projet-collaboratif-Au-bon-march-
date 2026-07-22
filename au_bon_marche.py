class Products(Shoppingcartline):

    def __init__(self, name, type, price, stock, unity):
        self.name = name
        self.price = price
        self.type = type
        self.stock = stock
        self.unity = unity

    def decrease_stock(self):
        nb_article = Shoppingcartline.quantity
        self.stock -= nb_article
