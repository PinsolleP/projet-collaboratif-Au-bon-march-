class Products:
    """Représente un produit vendu dans le magasin."""

    def __init__(self, name, price, stock, unity):
        """Initialise un produit.
        args: nom, prix, stock et unité."""

        self.name = name
        self.price = price
        self.stock = stock
        self.unity = unity

    def decrease_stock(self, quantity):
        """Diminue le stock du produit de la quantité achetée.
        args: quantity du produit
        retourne le stock du produit arrondi a 2 après la virgule"""

        self.stock -= quantity
        return round(self.stock, 2)

    def display_product(self):
        """Affichage d'un produit si besoin."""
        return f"L'article {self.name} existant en {self.stock} exemplaire(s) coute {self.price} / {self.unity}"

    def check_quantity(self, quantity):
        """Vérifie que la quantité est valide selon l'unité du produit
        args: quantité du produit.
        Retourne vrai ou faux selon l'unité du produit.
        ex: on ne peut pas sélectionner 1.4 Potirons car ils sont vendus à la pièce"""

        if self.unity == "pièce" and quantity != int(quantity):
            return False
        return True


class Shoppingcartline:
    """Représente une ligne dans le panier (produit + quantité)."""

    def __init__(self, product: Products, quantity):
        """Initialise une ligne du panier.
        args: un produit et sa quantité."""

        self.product = product
        self.quantity = quantity if quantity > 0 else 1

    def total_price_line(self) -> float:
        """Retourne le prix total pour cette ligne."""

        return round((self.product.price * self.quantity), 2)

    def display_line(self):
        """Affichage de la ligne du produit."""

        return f"{self.product.name} x {self.quantity} = {self.total_price_line():} €"


class Shoppingcart:
    """Représente un panier d'achat d'un client."""

    def __init__(self):
        """Initialise un panier d'achat."""

        self.lines = []

    def add_line(self, product, quantity):
        """Ajoute un produit au panier d'achat ou augmente la quantité s'il est déjà présent.
        args: un produit et sa quantité"""

        for line in self.lines:
            if line.product.name == product.name:
                line.quantity += quantity if quantity > 0 else 1
                return
        self.lines.append(Shoppingcartline(product, quantity))

    def display_lines(self):
        """Affiche le contenu du panier."""

        if not self.lines:
            print("Panier vide.")
            return
        for line in self.lines:
            print(line.display_line())
        print(f"Total : {self.totalcart()} €")

    def totalcart(self):
        """Calcule et Affiche le montant total du panier."""

        return sum(line.total_price_line() for line in self.lines)


class Clients:
    """Représente un client du magasin."""

    def __init__(self, surname, first_name):
        """Initialise un client du magasin."""

        self.surname = surname
        self.first_name = first_name
        self.basket = Shoppingcart()

    def get_total(self):
        """Retourne le montant total des achats du client."""

        return self.basket.totalcart()

    def display_tickets(self):
        """Affiche le ticket de caisse du client."""

        print(f"Client : {self.surname} - {self.first_name}")
        self.basket.display_lines()
        print(f"Total : {self.get_total()} €")


class Warehouse:
    """Représente le magasin avec ses produits et ses clients."""

    def __init__(self):
        """Initialise une liste de clients et de produits du magasin."""

        self.products = []
        self.clients = []

    def add_client(self, client):
        """Ajoute un client à la liste des clients de la journée.
        args: un client du magasin."""

        self.clients.append(client)

    def add_product(self, product):
        """Ajoute un produit à la liste des produits du magasin.
        args: un produit du magasin."""

        self.products.append(product)

    def display_products(self):
        """Affiche tous les produits disponibles dans le magasin."""

        print("=====STOCK DU MAGASIN=====")
        for i in self.products:
            print(f"{i.name} {i.price} €/{i.unity}")

    def day_summary(self):
        """Affiche le bilan de la journée : clients, chiffre d'affaires et stock restant."""
        
        print("=====Bilan de la journée===== :")
        print(len(self.clients), " clients")
        for client in self.clients:
            print(f"{client.first_name} , {client.surname} : {client.get_total()} €")
        print("total de la journée :", sum(client.get_total() for client in self.clients), "€")

        print("stock restant :")
        for product in self.products:
            print(f"{product.name} : {round(product.stock, 2)}  {product.unity}")
