def decale_lettre(lettre, decalage):
    code = ord(lettre)
    if lettre >= "a" and lettre <= "z":
        debut = ord("a")
        position = code - debut
        position = (position + decalage) % 26
        return chr(debut + position)
    if lettre >= "A" and lettre <= "Z":
        debut = ord("A")
        position = code - debut
        position = (position + decalage) % 26
        return chr(debut + position)
    return lettre

def cesar(message, decalage):
    resultat = ""
    for caractere in message:
        resultat = resultat + decale_lettre(caractere, decalage)
    return resultat

texte = "Bonjour Jules Cesar"
print(cesar(texte, 3))
