def longueur(liste):
    c = 0
    for _ in liste:
        c = c + 1
    return c

def my_sort(liste):
    n = longueur(liste)
    coups = 0
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if liste[j] > liste[j + 1]:
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
                coups = coups + 1
            j = j + 1
        i = i + 1
    print("Nombre de coups:", coups)
    return liste

L = [5, 3, 8, 1, 4]
print(my_sort(L))
