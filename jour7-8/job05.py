def distance_parcourue(marches, hauteur):
    aller_retour = marches * hauteur * 2
    par_jour = aller_retour * 5
    par_semaine_cm = par_jour * 7
    par_semaine_m = par_semaine_cm / 100
    return par_semaine_m

marches = 10
hauteur = 20
distance = distance_parcourue(marches, hauteur)
print("Pour", marches, "marches de", hauteur, "cm, le gardien parcourt", format(distance, ".2f"), "m par semaine.")
