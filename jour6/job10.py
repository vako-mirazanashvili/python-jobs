L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

produit = 1
a_trouve = False

for valeur in L:
    if valeur >= 25 and valeur <= 90:
        produit = produit * valeur
        a_trouve = True

if a_trouve:
    print(produit)
else:
    print("Aucune valeur dans l intervalle")