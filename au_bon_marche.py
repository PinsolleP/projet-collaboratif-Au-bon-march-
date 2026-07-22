class Products:

    def __init__(self, name, type, price, stock, unity):
        self.name = name
        self.price = price
        self.type = type
        self.stock = stock
        self.unity = unity


class Shoppingcartline(Products):
    """Représente une ligne dans le panier (produit + quantité)."""

    def __init__(self, name, quantity):
        super().name = name
        self.quantity = quantity

    def total_price_line(self) -> float:
        """Retourne le prix total pour cette ligne."""
        return self.name.price * self.quantity
     
