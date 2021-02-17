# Doosmaakmachine heeft een input nodig
# Snap de verhouding nog steeds niet helemaal??

# opdruk
# gewicht
# vorm -> alleen maar rechthoekige dozen!

# Gegeven lengte, breede, diepte en dikte
# specificaties
doosbreedte = float(input("Breedte(mm) van de doos: "))# mm
dooslengte = float(input("Lengte(mm) van de doos: "))  # mm
doosdiepte = float(input("Diepte(mm) van de doos: "))  # mm
doosdikte = float(input("Dikte(mm) van de doos: "))    # mm
kleur = input("Welke kleur(blauw, rood, groen): ")
materiaal = input("Welke materiaal(karton, hout, plastic): ")

# Het controleren van de afmetingen
def controleren_afmetingen():
    if (doosbreedte <= maxbreedte and doosbreedte >= minbreedte) and (dooslengte <= maxlengte and dooslengte >= minlengte) and (doosdiepte <= maxdiepte and doosdiepte >= doosdiepte) and (doosdikte <= maxdikte and doosdikte >= mindikte):
        return True
    else:
        return False

# Het controleren van de inhoud
def controleren_inhoud(dl, db, dd):
    inhoud = round((dl * db * dd)/1000000, 1) # liters
    if inhoud < 1:
        return False
    else:
        return True

# Verhouding controlen
def controleren_verhouding(afm1, afm2):
    verhouding = round(afm1/afm2)
    if verhouding < 1:
        return False
    else:
        return True
  
# Max lengte, breede, diepte en dikte
# Randvoorwaarden
maxbreedte = 1000  # mm
maxlengte = 1000   # mm
maxdiepte = 1000   # mm
maxdikte = 10      # mm

minbreedte = 10  # mm
minlengte = 10   # mm
mindiepte = 10   # mm
mindikte = 1     # mm

# Keuzes van kleuren en materialen
materialen = ["karton", "hout", "plastic"]
kleuren = ["blauw", "rood", "groen"]
# Gegeven kleur en materiaal
if kleur == "blauw":
    print("De kleur van de doos is", kleuren[0])
elif kleur == "rood":
     print("De kleur van de doos is", kleuren[1])
elif kleur == "groen":
     print("De kleur van de doos is", kleuren[2])
else:
    print("Vul een kleur in die bestaat!")

if materiaal == "karton":
    print("Het materiaal van de doos is", materialen[0])
elif materiaal == "hout":
    print("Het materiaal van de doos is", materialen[1])
elif materiaal == "plastic":
    print("Het materiaal van de doos is", materialen[2])
else:
    print("Vul een materiaal in die bestaat!")

# verstuur naar machine

print("")
if (controleren_afmetingen() == False):
    print("De afmetingen zijn onjuist")
else:
    print("Afmetingen zijn juist")
print("")
if (controleren_inhoud(dooslengte, doosbreedte, doosdiepte) == False):
    print("De inhoud is te klein het moet minstens 1 liter zijn")
    print("Vul het opnieuw in")
else:
    print("Inhoud is juist")
print("")
if (controleren_verhouding(dooslengte, doosbreedte) == False):
    print("Doos wordt te hoog!")
else:
    print("Dooshoogte is juist")
print("")
if (controleren_verhouding(doosdiepte, doosbreedte) == False):
    print("Doos wordt te breed!")
else:
    print("Doosbreedte is juist")
print("")
if (controleren_verhouding(doosdiepte, dooslengte) == False):
    print("Doos wordt te diep!")
else: 
    print("Doosdiepte is juist")