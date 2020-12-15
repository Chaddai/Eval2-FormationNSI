# %% [markdown]
# # Une caisse automatique pour NSIThlon : Correction
# 
# ## Partie A
# 
# 1. On constate que les identifiants RFID d'articles similaires partagent les mêmes 6 premiers chiffres. Par la suite on appellera ceci le code produit. Par exemple les deux "CHAUSS RS500 BLA" ont pour identifiants **428228** 6203 et **428228** 9929.
# 2. Par exemple dans le ticket le produit de nom "CHAUSS RS500 BLA" a pour prix 4.50 € et pour code produit "428228" donc :
#   a.Le type de donnée approprié pour :
#     - Le nom est une chaîne de caractère (<em>str</em> en Python)
#     - Le prix est un nombre à virgule flottante (<em>float</em>)
#     - Le code produit est une chaîne de caractère (<em>str</em>), de 6 chiffres plus précisément. Ce n'est pas un entier, aucune opération numérique n'est effectué sur le code produit.
#   b. Un produit est décrit par trois informations de types différents, on les regroupe donc dans un triplet (<em>tuple</em> en Python) car les types sont hétérogènes et un produit est a priori immuable (il ne changera pas de nom, de prix ou de code produit, sinon ce n'est plus le même produit).
# 3. Après recopie, on arrange les guillemets ", les parenthèses () (pour les triplets), les crochets [] (pour la liste) et les virgules , pour créer une liste des triplets représentants nos produits : 

# %%
## 3)

exemple_produits = [
    ("PANT SH100", "000255", 30.00 ),
    ("CHAUS RS500 BLA", "428228", 4.50),
    ("PNEU VTT 26X2", "768489", 10.00),
    ("BAS 100 NOIR", "000179", 5.00)
]

# %% [markdown]
# 4. Une liste comme dans la question 3 n'est pas approprié : en effet l'ordre des produits dans la liste n'a pas d'importance et il va falloir parcourir toute la liste pour retrouver le code produit qui nous intéresse. Nous souhaitons un accès immédiat par le code produit et l'ordre n'importe pas, la structure de données qui s'impose est donc un dictionnaire où les clés sont les codes produit et les valeurs sont les produits (qu'on peut maintenant simplement décrire par le couple nom et prix puisque le code produit est dans la clé).
# 5. On crée un dictionnaire vide qu'on remplit en parcourant notre liste `exemple_produits` avec une boucle Pour :

# %%
## 5)

produits = dict()
for (nom, code, prix) in exemple_produits:
    produits[code] = (nom, prix)

# %% [markdown]
#   On peut ensuite tester notre structure de donnée en vérifiant que le code produit extrait de **000179** 7890 permet bien de retrouver le produit "BAS 100 NOIR" correspondant (et son prix) :

# %%
print(produits['000179'])
# devrait afficher :
# ('BAS 100 NOIR', 5.0)

# %% [markdown]
# ## Partie B
# 
# 6. Nous devons garder seulement les 6 premiers chiffres d'un identifiant RFID (qui est une chaîne de 10 chiffres). Nous créons donc une nouvelle chaîne vide à laquelle nous concaténons un par un les caractères d'indices 0 à 5 de l'identifiant :

# %%
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

# %% [markdown]
#   N'oubliez pas d'inclure une chaîne de caractère documentant votre fonction et les types de ses paramètres et de la valeur renvoyée, vous pouvez aussi inclure un exemple d'utilisation dans la console Python (qui pourra être automatiquement testé par le module `doctest`). Visualisez le résultat ci-dessous :

# %%
help(rfid_vers_code)

# %% [markdown]
# 7. Cette fonction est plus complexe mais du fait que nous avons utilisé un dictionnaire pour nos produits, le passage de l'identifiant RFID au produit nécessite juste d'indexer `produits` par le résultat de l'appel de `rfid_vers_code` sur le RFID. On crée donc une liste vide à laquelle on ajoute (avec `append`) les produits correspondants aux RFID du `panier` dans une boucle Pour :

# %%
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
    for RFID in panier:
        code = rfid_vers_code(RFID)
        liste_achats.append(produits[code])
    return liste_achats

# %% [markdown]
# 8. Finalement, il faut calculer le total des achats dans une liste d'achats. On va procéder à l'aide d'une variable accumulateur `somme` qui sera initialisée à 0 et à laquelle on ajoutera le prix de chaque produit dans la liste d'achats, parcourue par une boucle Pour :

# %%
## 8)

def total(liste_achats):
    """
        paramètre liste_achats : (list( (str,float) )) Une liste de produits achetés sous la forme de tuples (nom,prix)
        sortie : (float) Le prix total des achats passés en paramètre

    >>> total([('CHAUS RS500 BLA', 4.5), ('PANT SH100', 30.0)])
    34.5
    """
    somme = 0
    for (_nom, prix) in liste_achats:
        somme += prix
    return somme

# %% [markdown]
# ## Pour aller plus loin
# 
# 9. La fonction `ticket` doit produire un ticket similaire au ticket d'origine (mais légèrement simplifié, notamment pour l'alignement, difficile à reproduire dans une simple chaîne de caractère). On initialise une variable `resultat` à une chaîne de caractères vide dans laquelle on va construire le ticket au fur et à mesure. Donc on commence par récupérer la liste des produits achetés à l'aide de la fonction `achats` puis pour chaque achat il est nécessaire d'ajouter le nom du produit, un espacement (on a choisi deux caractères tabulation qu'on obtient à l'aide de `\t` et qui produisent un alignement passable tant que les noms de produits sont de longueurs similaires) puis le prix. Si l'on choisit d'inclure l'identifiant RFID, il est important de parcourir les indices des achats plutôt que les éléments de cette liste afin de pouvoir retrouver l'identifiant correspondant dans le `panier`. Finalement on calcule le total à l'aide de la fonction `total` et on l'ajoute à la fin du ticket.
# 
#   N'oubliez pas de convertir les nombres en chaînes de caractères (avec la fonction `str`) avant de les concaténer.

# %%
## 9)

def ticket(panier, produits):
    """
        paramètre panier : (list(str)) Une liste d'identifiants RFID (chaîne de 10 chiffres) représentant le contenu d'un panier
        paramètre produits : (dict( str:(str,float) )) Un dictionnaire indexé par le code produit (6 chiffres) contenant les couples (nom, prix) de produits
        sortie : (str) Un ticket décrivant les achats et le total à payer

    >>> print(ticket(['4282281234', '0002554224'], produits))
    CHAUS RS500 BLA		4.5
    RFID : 4282281234
    PANT SH100		30.0
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

# %% [markdown]
# 10. On adapte légèrement le code proposé pour qu'il charge le bon fichier et transforme ses données en un dictionnaire de produits. Attention le lecteur csv renvoie des listes de chaînes de caractères, nous devons convertir les prix en nombres à virgule flottante pour récupérer une structure de données compatible avec nos fonctions.

# %%
## 10)

import csv

fichier_source = open('produits.csv', 'r', newline='')

lecteur_produits = csv.reader(fichier_source)
produits_complet = dict()
for (nom, code, chainePrix) in lecteur_produits:
    produits_complet[code] = (nom, float(chainePrix))
    
fichier_source.close()

# %% [markdown]
# 11. On vérifie que le code fonctionne :

# %%
## 11)

import nsithlon as nsi
nsi.genere_panier()

# %% [markdown]
# 12. Nous répétons simplement 10 fois à l'aide d'une boucle Pour la génération aléatoire d'un panier puis l'affichage du ticket correspondant :

# %%
## 12)

for _ in range(10):
    panier_aleatoire = nsi.genere_panier()
    print(ticket(panier_aleatoire, produits_complet))
    print() # pour une ligne vide entre chaque ticket


