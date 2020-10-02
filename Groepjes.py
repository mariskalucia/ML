# Mariska de Vries
# 223751

# Het inporteren van de code random
import random

# Een lijst met namen
namen = ["Kaya", "Debbie", "laurence", "Robbin", "Mariska",  "Rick", "Kalle", "Wilke", "Thomas.k", "Tim", "Menno", "Jonathan", "Sem", "Jan", "Willem", "Daniël", "Nimue", "Rowin", "Thomas.E", "Simon", "Mathijs", "Ate-Jan"]

# Hij begint bij groep 1
groep = 1 
# Er worden 5 personen bij in de groep gezet
aantalklasgenoten = 5

# Hij haalt alle namen uit de lijst weg
for name in namen[:]:
    # Hij stopt met namen er in te zetten als er er 5 inzitten
    if aantalklasgenoten == 5:
        # Hij print De groep en plaats telkens in de {1} {2} {3} enz.
        print("Groep {}:".format(groep))# Hij zet het onderelkaar neer
        # Hij reset de aantal klasgenoten weer naar 0
        aantalklasgenoten=0
        # De groep word van 1 naar 2 van naar 3 enz.
        groep+=1
    # Hij kiest een random naam uit de list namen
    persoon = random.choice(namen)
    print(persoon) 
    aantalklasgenoten+=1
    # Hij verwijderd de namen die dubble zijn
    namen.remove(str(persoon))


