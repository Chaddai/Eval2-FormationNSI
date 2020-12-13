#!/usr/bin/python3
# -*- coding: utf-8 
import nsithlon as nsi

## 3)

exemple_produits = [
    ("PANT SH100", "000255", 30.00 ),
    ("CHAUS RS500 BLA", "428228", 4.50),
    ("PNEU VTT 26X2", "768489", 10.00),
    ("BAS 100 NOIR", "000179", 5.00)
]

## 5)

produits = dict()
for (nom, code, prix) in exemple_produits:
    produits[code] = (nom, prix)

# print(produits['000179'])
# affiche bien :
# ('BAS 100 NOIR', 5.0)

## 6)

def rfid_vers_code(RFID):
    """
        paramètre RFID : (str) une chaîne de 10 chiffres
        sortie : (str) les 6 premiers chiffres de RFID, correspondant au code produit

    >>> rfid_vers_code('1234567890') 
    '123456'
    """
    code = ""
    for i in range(0,6):
        code += RFID[i]
    return code

## 7)

def achats(panier, produits):
    """
        paramètre panier : (list(str)) Une liste d'identifiants RFID (chaîne de 10 chiffres) représentant le contenu d'un panier
        paramètre produits : (dict( str:(str,float) )) Un dictionnaire indexé par le code produit (6 chiffres) contenant les couples (nom, prix) de produits
        sortie : (list( (str,float) )) Une liste des produits (nom,prix) contenus dans le panier

    >>> achats(['4282281234', '0002554224'], produits)
    [('CHAUS RS500 BLA', 4.5), ('PANT SH100', 30.0)]
    """
    liste_achats = []
    for rfid in panier:
        liste_achats.append(produits[rfid_vers_code(rfid)])
    return liste_achats

## 8)

def total(achats_produits):
    """
        paramètre achats_produits : (list( (str,float) )) Une liste de produits achetés sous la forme de tuple (nom,prix)
        sortie : (float) Le prix total des achats passés en paramètre

    >>> total([('CHAUS RS500 BLA', 4.5), ('PANT SH100', 30.0)])
    34.5
    """
    somme = 0
    for (nom, prix) in achats_produits:
        somme += prix
    return somme

## 9)

def ticket(panier, produits):
    """
        paramètre panier : (list(str)) Une liste d'identifiants RFID (chaîne de 10 chiffres) représentant le contenu d'un panier
        paramètre produits : (dict( str:(str,float) )) Un dictionnaire indexé par le code produit (6 chiffres) contenant les couples (nom, prix) de produits
        sortie : (str) Un ticket décrivant les achats et le total à payer

    >>> print(ticket(['4282281234', '0002554224'], produits))
    CHAUS RS500 BLA     4.5
    RFID : 4282281234
    PANT SH100      30.0
    RFID : 0002554224
    ---
    Total : 34.5
    """
    resultat = ""
    liste_achats = achats(panier, produits)
    # parcourons la liste par indice pour connaître l'identifiant RFID correspondant
    for i in range(len(liste_achats)): 
        (nom, prix) = liste_achats[i]
        rfid = panier[i]
        resultat += nom + "\t\t" + str(prix) + "\nRFID : " + rfid + "\n"
    resultat += "---\nTotal : " + str(total(liste_achats))
    return resultat

## 10)

import csv

fichier_source = open('produits.csv', 'r', newline='')

lecteur_produits = csv.reader(fichier_source)
produits_complet = dict()
for (nom, code, strPrix) in lecteur_produits:
    produits_complet[code] = (nom, float(strPrix))
    
fichier_source.close()

## 12)

import nsithlon as nsi

for _ in range(10):
    print(ticket(nsi.genere_panier(), produits_complet))
    print() # pour une ligne vide entre chaque ticket

