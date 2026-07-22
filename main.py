from au_bon_marche import *

if __name__ == "__main__":
    end_day = False
    finish_purchase = False
    while finish_purchase is False and end_day is False:
        Clients.first_name = input("Entrer votre prénom ")
        Clients.last_name = input("Entrer votre nom: ")
        for product in store:
            Products.display_product(product)
        client_purchase = input("Que voulez vous acheter ? ")
        client_quantity = int(input("Combien en voulez vous ? "))
        Shoppingcart.add_line(store, client_purchase, client_quantity)

