# Mariska de Vries
# 223751
# 6-1-2021
# Kilometer

class Kilometer:
    def __init__(self, afstand=0):
        self.__afstand = afstand

    
    def naar_mijlen(self):
        mijlen = self.__afstand * 0.621371
        return mijlen

    @property
    def afstand(self):
        print("Waarde ophalen...")
        return self.__afstand

    @afstand.setter
    def afstand(self, waarde):
        print("Waarde instellen...")
        self.__afstand = waarde

kilometers = Kilometer(10)
print(kilometers.afstand, "KM")
print(kilometers.naar_mijlen(), "MI")
kilometers.afstand = 12
print(kilometers.afstand, "KM")
print(kilometers.naar_mijlen(), "MI")