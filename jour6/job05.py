L = [1, 2, 3, 4, 5]

print(L[1])

def change_list(liste):
    liste[3] = liste[2] + liste[4]

change_list(L)
print(L)
print(L[-1])