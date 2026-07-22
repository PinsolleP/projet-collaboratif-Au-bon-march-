class Products:

    def __init__(self, name, type_product, price, stock, unity):
        self.name = name
        self.price = price
        self.type_product = type_product
        self.stock = stock
        self.unity = unity

    def decrease_stock(self):
        nb_article = Shoppingcartline.quantity
        self.stock -= nb_article
        return self.stock

    def dissplay_product(self):
        print(
            f"L'article {self.name} existant en {self.stock} exemplaire(s) coute {self.price} / {self.unity}")


class Shoppingcartline(Products):
    """Représente une ligne dans le panier (produit + quantité)."""

    quantity = None

    def __init__(self, product: Products, quantity, name, type_product, price, stock, unity):
        super().__init__(name, type_product, price, stock, unity)
        self.product = product
        self.quantity = quantity if quantity > 0 else 1

    def total_price_line(self) -> float:
        """Retourne le prix total pour cette ligne."""
        return self.product.price * self.quantity

    def display_line(self):
        return f"{self.product.name} x {self.quantity} = {self.total_price_line():} €"


class Shoppingcart:
    """Classe représentant un panier d'achat."""

    def __init__(self):
        self.lines = []

    def add_product(self, product, quantity):
        """Ajoute un produit ou augmente la quantité s'il est déjà présent."""
        for line in self.lines:
            if line.product.name == product.name:
                line.quantity += quantity if quantity > 0 else 1
                return
            self.lines.append(Shoppingcartline(product, quantity))

    def display_lines(self):
        if not self.lines:
            print("Panier vide.")
            return
        for line in self.lines:
            print(line.display_line())
        print(f"Total : {self.totalcart()} €")

    def totalcart(self):
        return sum(line.total_price_line() for line in self.lines)


class Clients(Shoppingcart):

    def __init__(self, surname, first_name):
        self.surname = surname
        self.first_name = first_name
        self.basket = Shoppingcart()

    def get_total(self):
        return self.basket.totalcart()

    def display_tickets(self):
        print(f"Client : {self.surname} - {self.first_name}")
        self.basket.display_lines()
        print(f"Total : {self.get_total()} €")


class Store(Products, Clients):
    def __init__(self, product: Products, name, type_product, price, stok, unity, client: Clients, first_name, surname):
        super().__init__(name, type_product, price, stok, unity, first_name, surname)
        self.product = product
        self.client = client

