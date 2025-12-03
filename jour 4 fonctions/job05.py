def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Opérateur invalide"





cal = input("choisisez operateur ")
calcule(cal)#print(calcule(5, "+", 3))   
#print(calcule(10, "-", 2))  
#print(calcule(6, "*", 4))   
#print(calcule(9, "/", 3))  
#print(calcule(9, "%", 4))   