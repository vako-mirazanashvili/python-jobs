def arrondir_notes(notes):
    nouvelles_notes = []
    for note in notes:
        if note < 40:
            nouvelles_notes.append(note)
        else:
            reste = note % 5
            difference = 5 - reste
            if difference < 3:
                nouvelles_notes.append(note + difference)
            else:
                nouvelles_notes.append(note)
    return nouvelles_notes

liste_notes = [38, 40, 41, 42, 83, 82, 57]
print(arrondir_notes(liste_notes))
