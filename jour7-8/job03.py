def tapis(n):
    taille = n + 1
    ligne = 0
    while ligne < taille:
        colonne = 0
        texte = ""
        while colonne < taille:
            if colonne == taille - 1 - ligne:
                texte = texte + "\"
            else:
                texte = texte + "#"
            colonne = colonne + 1
        print(texte)
        ligne = ligne + 1

tapis(10)
