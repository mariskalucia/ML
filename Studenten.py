class Student:
    def __init__(self, naam, nummer):
        self.naam = naam
        self.nummer = nummer

mariska = Student('Mariska', '223751')
lucia = Student('Lucia', '224642')
jan = Student('Jan', '225754')
tom = Student('Tom', '228945')

klas = [mariska, lucia, jan, tom]
lengte = len(klas)

for x in range(lengte):
    print("Naam: " + klas[x].naam + "      " + "Studentennummer: " + klas[x].nummer)
