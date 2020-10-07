# Mariska de Vries
# 223751

# Vragen om de leeftijd
leeftijd = int(input("Wat is uw leeftijd: "))

# De vakantiedagen is standaard 25
vankantiedagen = 25

# Als de leeftijd kleiner is dan 45 dan print hij 25 dagen
if (leeftijd < 45):
    print("U hebt recht op", vankantiedagen, "Vakantiedagen.")
elif (leeftijd < 56):
    # Als de leeftijd tussen de 44 en 56 dan telt hij bij de 25 vd 1 der bij op
    vankantiedagen+=1        
    print("U hebt recht op", vankantiedagen, "Vakantiedagen.")
elif (leeftijd < 68):
     # Als de leeftijd tussen de 55 en 68 dan telt hij bij de 25 vd 2 der bij op
    vankantiedagen+=2
    print("U hebt recht op", vankantiedagen, "Vakantiedagen.")

# Vragen om de aantal dienstjaren
aantaldienstjaren = int(input("Hoeveel dienstjaren heeft u gewerkt: "))

# Als de aantal dienstjaren kleiner is dan 26 dan krijg je geen extra vakantie dagen
if (aantaldienstjaren < 26):
    print("U krijgt geen extra vakantiedagen u hebt recht op", vankantiedagen, "vakantiedagen.") 
elif (aantaldienstjaren < 40):
    # Als je tussen de 25 en 40 zit dan krijg je 2 extra vakantiedagen
    vankantiedagen+=2
    print("U hebt recht op 2 extra vakantiedagen u hebt nu", vankantiedagen, "Vakantiedagen.")
elif (aantaldienstjaren < 68):
     # Als je tussen de 39 en 68 zit dan krijg je 5 extra vakantiedagen
    vankantiedagen+=5 
    print("U hebt recht op 5 extra vakantiedagen u hebt nu", vankantiedagen, "Vakantiedagen.")

# =<