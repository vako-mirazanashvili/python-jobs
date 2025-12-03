investment=6000
tax=3

gain=investment * tax/100

print(f"investment : {investment} € ")
print(f"Annual return rate: {tax}%")
print(f"Annual gain: {gain} €")


investment += 5000
tax += 2


gain = investment * tax / 100
print(f"New investment amount: {investment} €")
print(f"New return rate: {tax}%")
print(f"New annual gain: {gain} €")


investment *= 0.9     
tax -= 1      


gain = investment * tax / 100
print(f"Final investment amount: {investment} €")
print(f"Final return rate: {tax}%")
print(f"Final annual gain: {round(gain, 2)} €")