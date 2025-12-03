a = float(input("Entrez la longueur a: "))
b = float(input("Entrez la longueur b: "))
c = float(input("Entrez la longueur c: "))

if a + b > c and a + c > b and b + c > a:
    print("Ces longueurs peuvent former un triangle.")

    if a == b == c:
        print("Le triangle est équilatéral.")
    elif a == b or b == c or a == c:
        print("Le triangle est isocèle.")
    else:
        print("Le triangle est quelconque.")

    if round(a**2 + b**2, 5) == round(c**2, 5) or \
       round(a**2 + c**2, 5) == round(b**2, 5) or \
       round(b**2 + c**2, 5) == round(a**2, 5):
        print("Le triangle est rectangle.")
else:
    print("Ces longueurs ne peuvent pas former un triangle.")
