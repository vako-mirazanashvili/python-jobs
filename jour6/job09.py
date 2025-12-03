L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

minimum = L[0]
maximum = L[0]

for valeur in L:
    if valeur < minimum:
        minimum = valeur
    if valeur > maximum:
        maximum = valeur

print("Minimum:", minimum)
print("Maximum:", maximum)