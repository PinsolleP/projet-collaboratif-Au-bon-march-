class Products:

    def __init__(self, name, price, stock, unity):
        self.name = name
        self.price = price
        self.stock = stock
        self.unity = unity

    def decrease_stock(self, quantity):
        self.stock -= quantity
        return round(self.stock, 2)

    def display_product(self):
        return f"L'article {self.name} existant en {self.stock} exemplaire(s) coute {self.price} / {self.unity}"

    def check_quantity(self, quantity):
        if self.unity == "pièce" and quantity != int(quantity):
            return False
        return True


class Shoppingcartline:
    """Représente une ligne dans le panier (produit + quantité)."""

    def __init__(self, product: Products, quantity):
        self.product = product
        self.quantity = quantity if quantity > 0 else 1

    def total_price_line(self) -> float:
        """Retourne le prix total pour cette ligne."""
        return round((self.product.price * self.quantity),2)

    def display_line(self):
        return f"{self.product.name} x {self.quantity} = {self.total_price_line():} €"


class Shoppingcart:
    """Classe représentant un panier d'achat."""

    def __init__(self):
        self.lines = []

    def add_line(self, product, quantity):
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


class Clients:

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


class Warehouse:
    def __init__(self):
        self.products = []
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("=====STOCK DU MAGASIN=====")
        for i in self.products:
            print(f"{i.name} {i.price} €/{i.unity}")

    def day_summary(self):
        print("=====Bilan de la journée===== :")
        print(len(self.clients), " clients")
        for client in self.clients:
            print(f"{client.first_name} , {client.surname} : {client.get_total()} €")
        print("total de la journée :", sum(client.get_total() for client in self.clients), "€")

        print("stock restant :")
        for product in self.products:
            print(f"{product.name} : {round(product.stock, 2)}  {product.unity}")
