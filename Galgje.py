# Maak een programma waar je het woord moet raden net als in galgje
# Er is 1 input de vraagt om je naam
# 
# Gebruik (input, while, for, if, else, break, in, not in, ==, + en -)

naam_speler = input("Hey speler wat is je naam: ")
print("Hallo", naam_speler, "Welkom bij raad het woord.")
print("")
print("begin met het raden van het woord...")

woord = "trustgaming"
gokken = ""
beurten = 10

while beurten > 0:
    niet_goed_geraden = 0
    for char in woord:
        if char in gokken:
            print(char)
        else:
            print("_")
            niet_goed_geraden += 1
    if niet_goed_geraden == 0:
        print("Je hebt gewonnen")
        break
    print("")
    gok = input("Gok een letter van het woord: ")
    gokken += gok
    if gok not in woord:
        beurten -= 1
        print("De letter zit niet in het woord")
        print("Je hebt nog", beurten, "over om het woord te raden")
        if beurten == 0:
            print("Je beuten zijn op je hebt verloren. Volgende keer beter.")