def moyenne(note1, note2, note3):
    moyenne_eleve = (note1 + note2 + note3) / 3

    if moyenne_eleve >= 15:
        print("Très bon élève")
    elif 8 <= moyenne_eleve < 10:
        print("Élève moyen")
    elif 0 < moyenne_eleve < 7:
        print("Élève doit faire des efforts")

note1 = int(input("Première note : "))
note2 = int(input("Deuxième note : "))
note3 = int(input("Troisième note : "))

moyenne(note1, note2, note3)
