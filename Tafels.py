print("Vul 0 in om het programma te sluiten.")
doorgaan = True
# Vragen om het getal
while (doorgaan):
    getal = int(input("Van welk getal wil je de tafel: "))
    if (getal == 0):
        doorgaan = False
        print("Het programma is gesloten.")
    else:
        # De range zetten van de loop
        for getal2 in range(1,11):
            # Het printen op het scherm
            print(getal, "*", getal2,"=", getal*getal2) # Aan het einde getal x getal2



