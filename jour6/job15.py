def longueur(liste):
    c = 0
    for _ in liste:
        c = c + 1
    return c

def arrondir_nombre(x):
    entier = int(x)
    fraction = x - entier
    if fraction >= 0.5:
        return entier + 1
    else:
        return entier

def trier_croissant(liste):
    n = longueur(liste)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if liste[j] > liste[j + 1]:
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
            j = j + 1
        i = i + 1
    return liste

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

L_arrondie = []

for valeur in L:
    L_arrondie.append(arrondir_nombre(valeur))

print(trier_croissant(L_arrondie))