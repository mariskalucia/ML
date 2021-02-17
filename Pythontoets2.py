# Mariska de Vries
# 223751
# 12-2-2021
# Toets2

# Typen = string-int-float-boolean
naam = "Lucy"
print("String:", naam)
leeftijd = int(18)
print("Int:", leeftijd)
schoenmaat = float(41.5)
print("Float:", schoenmaat)
volwassen = True
print("Booleon:", volwassen)
print("")

# List
klas1 = ["Leon", "Lucia"]
print(klas1)

klas1.append("Kara")
klas1.append("Clark")
klas1.append("Sara")
print(klas1)

klas2 = ["Jax", "Kate", "Nate"]
klas1.extend(klas2)
print(klas1, "\n")

print("Er zijn:", len(klas1), "studenten")
print("Studenten:\n")
klas1.sort()
for studenten in klas1:
    print(studenten)
print("")

# Operatoren = / + - * %
getal1 = 4
getal2 = 3

print (getal1, "/", getal2, "=", getal1/getal2)
print (getal1, "-", getal2, "=", getal1 - getal2)
print (getal1, "+", getal2, "=", getal1+getal2)
print (getal1, "*", getal2, "=", getal1 * getal2)
print (getal1, "%", getal2, "=", getal1 % getal2)
print("")

# if, elif, else 

# While
doorgaan = True
tellertje = 0
while tellertje < 2:
    tellertje+=1
    print("iets")
print("")

# Functies
def optellen(num1, num2):
    return num1+num2 # Lokaal

# Scope
num1 = 20  # Globaal
num2 = 14  # Globaal

print(optellen(num1, num2))
print(optellen(5, 10))