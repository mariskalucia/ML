# Mariska de Vries
# 2223751

# Eerst inkomen vragen
salaris = int(input("Wat is uw salaris: "))

# belasting berekenen 
if (salaris < 10000):
    belasting = 0
    belasting = salaris
elif (salaris < 50000):
    belasting = (salaris - 10000) / 100 * 30
else:
    belasting = (salaris - 50000) / 2 

# Op het scherm printen
print("De belasting die u moet betalen is €" + str(belasting)) 
