#!/usr/bin/env python
# -*- coding: utf-8 -*-
from au_bon_marche import *


def store():
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
    storage = Warehouse()

    for item in stock_initial:
        storage.add_product(Products(*item))

    return storage


if __name__ == "__main__":
    end_day = False
    finish_purchase = False
    while not end_day:
        first_name = input("Entrer votre prénom: ")
        last_name = input("Entrer votre nom: ")
        client = Clients(first_name, last_name)
        while not finish_purchase:
            for product in store():
                Warehouse.display_products(product)
            client_purchase = input("Que voulez vous acheter ? ")
            client_quantity = int(input("Combien en voulez vous ? "))
            Shoppingcart.add_line(store, client_purchase, client_quantity)

