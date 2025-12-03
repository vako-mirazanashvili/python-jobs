L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

nouvelle_liste = []

for valeur in L:
    deja = False
    for v in nouvelle_liste:
        if v == valeur:
            deja = True
    if deja == False:
        nouvelle_liste.append(valeur)

print(nouvelle_liste)