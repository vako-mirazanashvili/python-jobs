L = [1, 2, 3, 4, 5]

temp = L[0]
L[0] = L[-1]
L[-1] = temp

print(L)