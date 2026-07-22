class Products:

    def __init__(self, name, type_product, price, stock, unity):
        self.name = name
        self.price = price
        self.type_product = type_product
        self.stock = stock
        self.unity = unity


class Shoppingcartline(Products):
    """Représente une ligne dans le panier (produit + quantité)."""

    def __init__(self, product: Products, quantity):
        self.product = product
        self.quantity = quantity if quantity > 0 else 1

    def total_price_line(self) -> float:
        """Retourne le prix total pour cette ligne."""
        return self.product.price * self.quantity

    def display_line(self):
        return f"{self.name.name} x {self.quantity} = {self.total_price_line():} €"

    def decrease_stock(self):
        nb_article = Shoppingcartline.quantity
        self.stock -= nb_article

