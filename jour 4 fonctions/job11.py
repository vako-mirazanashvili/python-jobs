def time_to_text(minutes: int):
    heure = int(minutes / 60)
    minuterestant = minutes - (heure * 60)
    print(f"{heure} heures et {minuterestant} minutes ")

calcul = int(input("ecir"))
time_to_text(calcul)
    