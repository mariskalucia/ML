# Mariska de Vries
# 223751

# Hij importeert van random allen randint
from random import randint
print("Raad het getal!!!!!")
# Hij kiest een random getal tussen de 1 en 100
randomgetal = randint(1, 100)

getalgeraden = False
# Aantal keer geraden begint 0 
aantalkeer = 0

# Als het getal niet geraden word dan bijft hij door vragen
while not getalgeraden:
    raadhetgetal = int(input("kies een getal tussen de 1 t/m 100: "))
    # Hij telt de aantal keer dat je de input invult bij de variable aantalkeer op 
    aantalkeer += 1
    # Als raadhetgetal gelijk is aan randomgetal dan:
    if (raadhetgetal == randomgetal):
        # Als je het in 1 keer geraden hebt print hij:
        if (aantalkeer == 1):
            print("Super fantastisch, Je hebt het getal in 1 keer geraden.")
            # En dan stopt hij de code ook 
            getalgeraden = True
        # Als je het in 2,3 of 4 keer geraden hebt print hij:
        elif (aantalkeer == 2 or 3 or 4):
            print("Fantastisch, je hebt het getal in", aantalkeer, "keer geraden")
            # En dan stopt hij de code ook
            getalgeraden = True
        # Als je het in 5,6 of 7 keer geraden hebt print hij:
        elif (aantalkeer == 5 or 6 or 7):
            print("Prima, je hebt het getal in", aantalkeer, "keer geraden")
            # En dan stopt hij de code ook 
            getalgeraden = True
        # Als je het in 8,9,10,11 of 12 keer geraden hebt print hij:
        elif (aantalkeer == 8 or 9 or 10 or 12):
            print("Goed, je hebt het getal in", aantalkeer, "keer geraden.")
            # En dan stopt hij de code ook 
            getalgeraden = True
        # Als je het in 13,14,15,16,17,18,19,20 keer geraden hebt print hij:
        elif (aantalkeer == 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20):
            print("Goed , je hebt het getal in", aantalkeer, "keer geraden Probeer de volgende keer of je het sneller kunt.")
            # En dan stopt hij de code ook
            getalgeraden = True
    # Als je 20x gegokt hebt en nog steeds niet geraden dan stopt de code
    elif (aantalkeer == 20):
        print("Jammer dan, het is niet je geluksdag.")
        getalgeraden = True
    # Als het getal kleiner is dan randomgetal print hij: 
    elif (raadhetgetal < randomgetal):
        print("Te laag! probeer opnieuw.")
    else:
        # Anders print hij:
        print("Te hoog! probeer opnieuw.")