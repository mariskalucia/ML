print("Vul getal 0 in om het programma te sluiten.")
# Door vragen van de input
doorgaan = True
aantal = 0
totaal = 0
while (doorgaan):
    getal = int(input("Getal: "))
    totaal = totaal + getal
    aantal = aantal + 1
    # als een getal kleiner is dan 0 geeft hij een waarschuwing
    if (getal < 0):
        # Het - getal er afhalen
        totaal = totaal - getal
        aantal = aantal - 1
        print("Waarschuwing alleen getallen boven de nul invullen. Bijv: 1")
        # De input opnieuw vragen
        getal
    # Als er 0 word ingevuld stopt het programma en geeft hij je uitkomst
    elif (getal == 0):
        doorgaan = False
        aantal = aantal - 1
        print("Het gemiddelde is: " + str(totaal/aantal))
  

        