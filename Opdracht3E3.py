# De vraag oneinig laten doorgaan
doorgaan = True


aantal = 0
totaal = 0

while (doorgaan):
    getal = int(input("Vul een getal in: "))
    # Hier telt hij de getallen opelkaar
    totaal = totaal + getal
    # Hier telt de aantal getallen dat je hebt ingevuld op
    aantal = aantal + 1
    # Als een getal groter dan 500 is dan stopt het programma
    if (totaal > 500):
        doorgaan = False
        print("Aantal getallen zijn:", aantal)
        print("Het totaal =", totaal)
    # Als er 10x een getal is in gevult dan stopt het programma ook
    elif (aantal > 9):
        doorgaan = False
        print("Aantal getallen zijn:", aantal)
        print("Het totaal =", totaal)
        