# Mariska de Vries
# 223751
# 12-2-2021
# Doosmaakmachine

# Doosmaakmachine heeft een input nodig

# opdruk
# gewicht
# vorm -> alleen maar rechthoekige dozen!

doosbreedte = float(input("Breedte(mm) van de doos: "))# mm
dooslengte = float(input("Lengte(mm) van de doos: "))  # mm
doosdiepte = float(input("Diepte(mm) van de doos: "))  # mm
doosdikte = float(input("Dikte(mm) van de doos: "))    # mm
kleurin = input("Welke kleur(blauw, rood, groen): ")
materiaalin = input("Welke materiaal(karton, hout, plastic): ")


class Doos:
    def __init__(self, lengte, breedte, diepte, dikte, kleur, materiaal):
        self._dooslengte = lengte
        self._doosbreedte = breedte
        self._doosdiepte = diepte
        self._doosdikte = dikte
        self._kleur = kleur
        self._materiaal = materiaal
        self._maxlengte = 1000  #mm
        self._maxbreedte = 1000 #mm
        self._maxdiepte = 1000  #mm
        self._maxdikte = 10     #mm
        self._minlengte = 100   #mm
        self._minbreedte = 100  #mm
        self._mindiepte = 100   #mm
        self._mindikte = 1      #mm

    # Het controleren van de verhouding
    def controleren_afmetingen(self):
        if (self._doosbreedte <= self._maxbreedte and self._doosbreedte >= self._minbreedte) and (self._dooslengte <= self._maxlengte and self._dooslengte >= self._minlengte) and (self._doosdiepte <= self._maxdiepte and self._doosdiepte >= self._doosdiepte) and (self._doosdikte <= self._maxdikte and self._doosdikte >= self._mindikte):
            return True
        else:
            return False

    # Het controleren van de inhoud
    def controleren_inhoud(self):
        inhoud = round((self._dooslengte * self._doosbreedte * self._doosdiepte)/1000000, 1) # liters
        if inhoud < 1:
            return False
        else:
            return True

    # Verhouding controlen van de lengte en breedte
    def controleren_verhouding1(self):
        verhouding = round(self._dooslengte/self._doosbreedte)
        if verhouding < 1:
            return False
        else:
            return True
    
    # Verhouding controlen van de diepte en breedte
    def controleren_verhouding2(self):
        verhouding = round(self._doosdiepte/self._doosbreedte)
        if verhouding < 1:
            return False
        else:
            return True
    
    # Verhouding controlen van de diepte en lengte
    def controleren_verhouding3(self):
        verhouding = round(self._doosdiepte/self._dooslengte)
        if verhouding < 1:
            return False
        else:
            return True

    # Het printen van de kleur en materiaal
    def kleur_materiaal(self):
        print(f'De kleur van de doos is {self._kleur}')
        print(f'Het materiaal van de doos is {self._materiaal}')



# De kleuren en materialen
# materialen = "karton", "hout", "plastic"
# kleuren = "blauw", "rood", "groen"

# De doos
doos = Doos(dooslengte, doosbreedte, doosdiepte, doosdikte, kleurin, materiaalin) 


# verstuur naar machine

doos.kleur_materiaal()

if (doos.controleren_afmetingen() == False):
    print("De afmetingen zijn onjuist")
else:
    print("Afmetingen zijn juist")

if (doos.controleren_inhoud() == False):
    print("De inhoud is te klein het moet minstens 1 liter zijn")
    print("Vul het opnieuw in")
else:
    print("Inhoud is juist")

if (doos.controleren_verhouding1() == False):
    print("Doos wordt te hoog!")
else:
    print("Dooshoogte is juist")

if (doos.controleren_verhouding2() == False):
    print("Doos wordt te breed!")
else:
    print("Doosbreedte is juist")

if (doos.controleren_verhouding3() == False):
    print("Doos wordt te diep!")
else: 
    print("Doosdiepte is juist")