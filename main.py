#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""import de toutes les classes de au_bon_marche"""
import au_bon_marche


def store():
    """permet d'initialiser le stock"""
    stock_initial = [
        ["Clémentine", 2.90, 6, "kg"],
        ["Datte", 7.00, 4, "kg"],
        ["Grenade", 4.00, 3, "kg"],
        ["Kaki", 2.50, 12, "kg"],
        ["Carotte", 1.30, 7, "kg"],
        ["Orange", 1.50, 8, "kg"],
        ["Pamplemousse", 2.00, 8, "pièce"],
        ["Poire", 2.50, 5, "kg"],
        ["Pomme", 1.50, 8, "kg"],
        ["Kiwi", 3.50, 5, "kg"],
        ["Mandarine", 2.80, 6, "kg"],
        ["Choux de Bruxelles", 4.00, 7, "kg"],
        ["Choux vert", 2.50, 12, "pièce"],
        ["Courge butternut", 2.50, 6, "pièce"],
        ["Endive", 2.50, 5, "kg"],
        ["Epinard", 2.60, 4, "kg"],
        ["Poireau", 1.20, 5, "kg"],
        ["Potiron", 2.50, 6, "pièce"],
        ["Radis noir", 5.00, 10, "pièce"],
        ["Salsifis", 2.50, 3, "kg"],
    ]
    storage = au_bon_marche.Warehouse()

    for item in stock_initial:
        storage.add_product(au_bon_marche.Products(*item))

    return storage


if __name__ == "__main__":
    """
    Point d'entrée du programme de gestion du magasin "Au Bon Marché".

    Cette partie du programme permet de simuler une journée de vente en magasin.

    Fonctionnement :
        - Initialise le magasin et son stock.
        - Accueille successivement plusieurs clients.
        - Demande le prénom et le nom de chaque client.
        - Affiche les produits disponibles.
        - Permet au client de sélectionner un produit et une quantité.
        - Vérifie que le produit existe et que la quantité demandée est valide.
        - Ajoute le produit au panier si le stock est suffisant.
        - Met à jour le stock et retire le produit de la liste lorsqu'il est épuisé.
        - Répète les achats jusqu'à ce que le client ait terminé.
        - Affiche le ticket de caisse du client et enregistre celui-ci dans le magasin.
        - Répète le processus pour les clients suivants jusqu'à la fin de la journée.
        - Affiche enfin un récapitulatif de la journée.
    """
    warehouse = store()
    end_day = False
    print("=====Bienvenue au bon marché=====")

    while not end_day:
        first_name = input("Entrer votre prénom:")
        last_name = input("Entrer votre nom:")
        client = au_bon_marche.Clients(last_name, first_name)
        finish_purchase = False
        while not finish_purchase:
            warehouse.display_products()
            client_purchase = input("Que voulez vous acheter ? ")
            selected_product = None
            for products in warehouse.products:
                if products.name.lower() == client_purchase.lower():
                    selected_product = products
                    break
            if selected_product is None:
                print("Produit inconnu")
            else:
                quantity = float(input("Combien en voulez vous ? "))
                if not selected_product.check_quantity(quantity):
                    print("Quantité invalide pour ce produit")
                else:
                    if quantity <= selected_product.stock:
                        client.basket.add_line(selected_product, quantity)
                        selected_product.decrease_stock(quantity)
                        print("Produit ajouté au panier")
                        if selected_product.stock == 0:
                            warehouse.products.remove(selected_product)
                            print("Ce produit n'est plus en stock")
                    else:
                        print("Stock insuffisant")

            answer_user = input("Avez-vous fini ? (o/n) ")
            if answer_user == "o":
                print("=====TICKET DE CAISSE=====")
                client.basket.display_lines()
                finish_purchase = True
                warehouse.add_client(client)
        end = input("Est-ce la fin de la journée ? (o/n) ")
        if end == "o":
            warehouse.day_summary()
            end_day = True
