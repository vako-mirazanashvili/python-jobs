def longueur(liste):
    c = 0
    for _ in liste:
        c = c + 1
    return c

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

L = [5, 3, 1, 4, 2]
print(trier_croissant(L))