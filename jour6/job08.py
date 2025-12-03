L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

somme = 0

for valeur in L:
    if valeur % 2 == 0:
        somme = somme + valeur

print(somme)