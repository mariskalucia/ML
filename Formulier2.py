# Mariska de Vries
# 223751

# Hier laat hij de code zolang opnieuw doen tot dat de input goed is ingevuld. 
doorgaan = True

while (doorgaan):
    # Hier word de input gevraagd
    voornaam = input("Voornaam: ")
    achternaam = input("Achternaam: ")
    nummer = input("Voer een vaste of mobiele nummer in: ")
    betaling = input("Betaling met Creditcard of Paypal: ")
    
    # Hier word gecheckt of de input klopt.
                #T                          #T
    if (voornaam == "Mariska" and achternaam == "de Vries") + (nummer == "0621359959" or nummer == "0512352603") + (betaling == "Creditcard" ^ betaling == "Paypal"):
        # Als het klopt word het geprint.
        print("Het word gecheckt ogenblik geduld a.u.b...")
        print(voornaam, achternaam)
        print(nummer)
        print(betaling)

    # Deze code checkt dat wat je ingevuld hebt ook correct(True) is.
    if ((voornaam == "Mariska") and (achternaam == "de Vries") and (nummer == "0621359959" or "0512352603") and (betaling == "Creditcard" ^ "Paypal")):
        # Als de code goed is dan stopt de loop.
        doorgaan = False
        print("Het is goed ingevuld. U kunt nu verder met bestellen.")
    else: 
        #Dit word geprint als het formulier niet goed is ingevuld
        print("Het is nog niet goed ingevuld.")
        print("Let op als u uw voor en achternaam met hoofdletterss heeft geschreven.")
        print("Let op dat u een mobiele of een vaste nummer heeft ingevuld.")
        print("Let op dat u 1 van de betalingen heeft uitgekozen.")
        print("Vul het formulier opnieuw in:")
    
