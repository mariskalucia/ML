# Mariska de Vries
# 223751

# Opdracht:
# Voornaam, achternaam, mobiel, vast, creditcard/paypal.
# V,A verplicht ingevuld. verplicht 1 telefoon nummer. Bij betaling moet 1 worden uitgekozen.
# Is het ingevuld moet er T of F zijn om het goed te keuren
# xor(^),or(}}),and(&&)  

# Hier laat hij de code zolang opnieuw doen tot dat de input goed is ingevuld. 
doorgaan = True
 
while (doorgaan):
    # Hier word de input gevraagd
    voornaam = input("Voornaam: ")
    achternaam = input("Achternaam: ") 
    # Hier word de code gecheckt als het klopt
    if voornaam == "Mariska" and achternaam == "de Vries":
        print(voornaam, achternaam) 
    else:
        # Geeft aan als de code niet klopt
        print("Uw voor of achtenaam is niet goed ingevuld.")   
    
    # Hier word de input gevraagd
    nummer = input("Vul een vaste of mobiele nummer in: ")
    # Hier word de code gecheckt als het klopt
    if nummer == "0621359959" or nummer == "0512352630":
        print(nummer)
    else:
        # Geeft aan als de code niet klopt
        print("U moet een vaste of mobiele nummer invullen.")
    
    # Hier word de input gevraagd
    betaling = input("Betaling met Creditcard of Paypal: ")           
    # Hier word de code gecheckt als het klopt
    if betaling == "Creditcard" or betaling == "Paypal":
        print(betaling)
    else:
        # Geeft aan als de code niet klopt
        print("U moet 1 van de gegeven betalingen uitkiezen.")

    # Hier word de code gecheckt als het klopt
    if ((voornaam == "Mariska") and (achternaam == "de Vries") and (nummer == "0621359959" or nummer == "0512352630") and (betaling == "Creditcard" or betaling == "Paypal")):
        # Als alles klopt dan stopt de loop
        doorgaan = False
        print("Het is goed ingevuld. U kunt nu verder met bestellen.")
    else:
        # Als het niet klopt dan word de code opniew gevraagd
        print("Het is nog niet goed ingevuld. Vul het formulier opnieuw in:")
    

