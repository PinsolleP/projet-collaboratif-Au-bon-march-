class Shoppingcartline(Products):
    """Représente une ligne dans le panier (produit + quantité)."""
    def __init__(self, produit: Products, quantite):
        self.produit = produit
        self.quantite = quantite

    def total_price_line(self) -> float:
        """Retourne le prix total pour cette ligne."""
        return self.produit.price * self.quantite

