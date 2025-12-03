L = [8, 24, 48, 2, 16]

compteur = 0

for valeur in L:
    if valeur % 3 == 0:
        compteur = compteur + 1

print(compteur)