#!/usr/bin/python3
# -*- coding: utf-8

import csv
import random

produits = []
usedCodes = set()
with open("produits.csv", "r", newline="",encoding="utf-8") as source:
    reader = csv.reader(source)
    for (name, code, price) in reader:
        produits.append( (name, code, float(price)) )
        usedCodes.add(code)

def genere_produit(generators):
    (nameGen, priceRange) = random.choice(generators)
    while True:
        code = "".join(random.choices("0123456789", k=6))
        if code not in usedCodes:
            usedCodes.add(code)
            break
    return (nameGen(), code, round(random.uniform(*priceRange),1))

def randomSize(): return random.choice(['XS','S','N','L','XL','XXL'])
def randomColor(): return random.choice(['BLA','JAU','NOIR','ROU','BLEU','VIO'])

gens = [
    (lambda : f"PANT {random.randint(1,5)*100} {randomSize()}", (20, 60)),
    (lambda : f"BIKE LOCK {random.randint(1,5)*100} {randomColor()}", (20, 60)),
    (lambda : f"ANTIVOL VELO {random.randint(1,5)*100} {randomSize()}", (20, 60)),
    (lambda : f"PORTE-BIDON {random.randint(20,35)*10} {randomColor()}", (20, 60)),
    (lambda : f"SLEEPING BAG {random.randint(1,5)*10} {randomColor()}", (20, 60)),
    (lambda : f"CHAUS R{random.randint(3,7)*100} {randomColor()}", (20, 60)),
    (lambda : f"SACOCHE VELO {random.randint(1,5)*100} {randomColor()}", (20, 60)),
    (lambda : f"POIDS {random.randint(1,50)}K {randomColor()}", (20, 60)),
    (lambda : f"TAPIS TRAINING {random.randint(1,5)*100}", (20, 60)),
    (lambda : f"CLIP {random.randint(1,5)*100} 2018 {randomColor()}", (20, 60))
]

with open("produits.csv","w",newline="",encoding="utf-8") as sink:
    writer = csv.writer(sink)
    writer.writerows(produits)
    for i in range(10000 - len(produits)):
        writer.writerow(genere_produit(gens))