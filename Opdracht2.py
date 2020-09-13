# Mariska de Vries
# 223751

# Vragen om de prijs van het toegangs kaartje
toegangsprijs = int(input("Wat is de prijs van het toegangskaartje: "))
# Vragen om de leeftijd
leeftijd1 = int(input("Wat is uw leeftijd: "))
leeftijd2 = int(input("Wat is uw leeftijd: "))
leeftijd3 = int(input("Wat is uw leeftijd: "))
leeftijd4 = int(input("Wat is uw leeftijd: "))

# leeftijd 1
if (leeftijd1 < 4):
    toegangsprijs = 0
elif (leeftijd1 < 12):
    toegangsprijs = 10
elif (leeftijd1 < 65):
    toegangsprijs = 20
elif (leeftijd1 > 64):
    toegangsprijs = 10
  
# leeftijd 2
if (leeftijd2 < 4):
    toegangsprijs2 = 0
elif (leeftijd2 < 12):
    toegangsprijs2 = 10   
elif (leeftijd2 < 65):
    toegangsprijs2 = 20
elif (leeftijd2 > 64):
    toegangsprijs2 = 10
   
# leeftjid 3
if (leeftijd3 < 4):
    toegangsprijs3 = 0 
elif (leeftijd3 < 12):
    toegangsprijs3 = 10
elif (leeftijd3 < 65):
    toegangsprijs3 = 20 
elif (leeftijd3 > 64):
    toegangsprijs3 = 10
    
# leeftijd 4
if (leeftijd4 < 4):
    toegangsprijs4 = 0   
elif (leeftijd4 < 12):
    toegangsprijs4 = 10  
elif (leeftijd4 < 65):
    toegangsprijs4 = 20 
elif (leeftijd4 > 64):
    toegangsprijs4 = 10
    

print("Intotaal te betalen: " + str(toegangsprijs + toegangsprijs2 + toegangsprijs3 + toegangsprijs4))
