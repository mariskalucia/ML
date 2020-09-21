# Mariska de Vries
# 223751

doorgaan = True

# De lijst met getallen
getallen = [1, 10, 14, 33, 23, 56, 78, 4, 294]
# Hij maakt van de lijst getallen een som
getallensum = sum(getallen)
# Hij telt de lengte van de getallen op
getallenlengte = len(getallen)

# Hier begint de loop
while (doorgaan):
    # De input word door gevraagd
    getal = int(input("Een positief getal: "))
    # Hier word het getal dat word in gevuld bij de getallen opgeteld
    getallensum = getallensum + getal
    # Hier word de aantal getallen bij geteld
    getallenlengte = getallenlengte + 1
    # Als er 0 word ingevoerd dan stopt het programma
    if (getal == 0):
        doorgaan = False
        # 0 word weer bij de lengte er afgehaalt
        getallenlengte = getallenlengte - 1
        # Hij berekend het gemiddelde en print het op het scherm
        print("Het gemiddelde is ", getallensum/getallenlengte)



