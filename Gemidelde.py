# Mariska de Vries
# 223751
# Gemaakt met Thomas en Menno

# getal Inlezen
doorgaan = True
aantal = 0
totaal = 0

# Een loop zodat de vraag medere keer word gevraagd
while (doorgaan == True):
    getal = int(input("Noem een getal: "))
    # Het optellen van de ingevulde getallen
    totaal = totaal + getal
    aantal = aantal + 1
    # De loop stoppen als er 0 word ingevuld
    if (getal == 0):
        doorgaan = False
        aantal = aantal - 1
    # Het (delete en) de waarschuwing voor een -getal
    elif (getal < 0):
        #del getal
        print("Alleen getallen boven de 0 invullen.")
    
    # Het printen van de uitkomst en het delen van het totaal
print("Je gemiddelde is: " + str(totaal/aantal))