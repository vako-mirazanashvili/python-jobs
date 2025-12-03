def verifier_nombre(nombre):
    if nombre % 1 != 0:
        print("Ce n'est pas un nombre entier.")
    elif nombre < 0:
        print("Le nombre doit être positif.")
    elif nombre % 2 == 0:
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")

verifier_nombre(4)     
verifier_nombre(7)      
verifier_nombre(-3)    
verifier_nombre(2.5)   
verifier_nombre(0)     
