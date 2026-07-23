#!/usr/bin/env python
# -*- coding: utf-8 -*-
from au_bon_marche import *


def store():
    stock_initial = [
        ["Clémentine", "Fruit", 2.90, 6, "kg"],
        ["Datte", "Fruit", 7.00, 4, "kg"],
        ["Grenade", "Fruit", 4.00, 3, "kg"],
        ["Kaki", "Fruit", 2.50, 12, "kg"],
        ["Carotte", "Légume", 1.30, 7, "kg"],
        ["Orange", "Fruit", 1.50, 8, "kg"],
        ["Pamplemousse", "Fruit", 2.00, 8, "pièce"],
        ["Poire", "Fruit", 2.50, 5, "kg"],
        ["Pomme", "Fruit", 1.50, 8, "kg"],
        ["Kiwi", "Fruit", 3.50, 5, "kg"],
        ["Mandarine", "Fruit", 2.80, 6, "kg"],
        ["Choux de Bruxelles", "Légume", 4.00, 7, "kg"],
        ["Choux vert", "Légume", 2.50, 12, "pièce"],
        ["Courge butternut", "Légume", 2.50, 6, "pièce"],
        ["Endive", "Légume", 2.50, 5, "kg"],
        ["Epinard", "Légume", 2.60, 4, "kg"],
        ["Poireau", "Légume", 1.20, 5, "kg"],
        ["Potiron", "Légume", 2.50, 6, "pièce"],
        ["Radis noir", "Légume", 5.00, 10, "pièce"],
        ["Salsifis", "Légume", 2.50, 3, "kg"],
    ]
    storage = Warehouse()

    for item in stock_initial:
        storage.add_product(Products(*item))

    return storage


if __name__ == "__main__":
    end_day = False
    finish_purchase = False
    while finish_purchase is False and end_day is False:
        Clients.first_name = input("Entrer votre prénom: ")
        Clients.last_name = input("Entrer votre nom: ")
        for product in store:
            Products.display_product(product)
        client_purchase = input("Que voulez vous acheter ? ")
        client_quantity = int(input("Combien en voulez vous ? "))
        Shoppingcart.add_line(store, client_purchase, client_quantity)

