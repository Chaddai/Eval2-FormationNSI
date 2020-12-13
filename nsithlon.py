#!/usr/bin/python3
# -*- coding: utf-8 
import random as rd
import csv
with open('produits.csv', 'r', newline='') as fich_source:
    lecteur_produits = csv.reader(fich_source)
    codes_produits = [code for (nom, code, prix) in lecteur_produits]

def genere_panier():
    """ 
        paramètre : aucun
        sortie : list(str) Une liste d'identifiant RFID (chaîne de 10 chiffres)
    """
    qte = rd.randint(1,10)
    codes = rd.choices(codes_produits, k=qte)
    return [code + ''.join(rd.choices("0123456789", k=4)) for code in codes]