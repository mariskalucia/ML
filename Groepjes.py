# Mariska de Vries
# 223751

# Het inporteren van de code random
import random

# Een lijst met namen
namen = ["Kaya", "Debbie", "laurence", "Robbin", "Mariska",  "Rick", "Kalle", "Wilke", "Thomas.k", "Tim", "Menno", "Jonathan", "Sem", "Jan", "Willem", "Daniël", "Nimue", "Rowin", "Thomas.E", "Simon", "Mathijs", "Ate-Jan"]
# Hier zet hij de lest namen onderelkaar als het geprint word

groep = 1 
aantalklasgenoten = 5

for name in namen[:]:
    if aantalklasgenoten == 5:
        print("Groep {}:".format(groep))
        aantalklasgenoten=0
        groep+=1
    persoon = random.choice(namen)
    print(persoon) 
    aantalklasgenoten+=1
    namen.remove(str(persoon))


