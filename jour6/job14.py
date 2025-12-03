def longueur_mot(mot):
    c = 0
    for _ in mot:
        c = c + 1
    return c

def my_long_word(n, phrase):
    phrase_sans_virgule = ""
    for caractere in phrase:
        if caractere == ",":
            phrase_sans_virgule = phrase_sans_virgule + " "
        else:
            phrase_sans_virgule = phrase_sans_virgule + caractere
    mots = phrase_sans_virgule.split(" ")
    resultat = []
    for mot in mots:
        if mot != "":
            if longueur_mot(mot) > n:
                resultat.append(mot)
    texte = ""
    premier = True
    for mot in resultat:
        if premier:
            texte = mot
            premier = False
        else:
            texte = texte + " " + mot
    return texte

phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, phrase))