def leg_fruit (type , saison):
    if type == "fruite" and saison == "hiver":
        print(f"orange , mandarine et kiwi")
    elif type == "fruite" and saison == "été":
        print(f"poire, fraise, cassis")
    elif type == "fruite" and saison == "été":
        print(f"poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print(f"carrotte, topinambeur, endive")
    elif type == "legume" and saison == "été":
        print(f"artichaut" * 2)

fruit = input("type")
leg = input ("saison")
leg_fruit(fruit,leg)

