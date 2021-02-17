class Student:
    def __init__(self, voornaam, achternaam, nummer, mail, gebdatum):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.nummer = nummer
        self.mail = mail
        self.gebdatum = gebdatum

    def gemiddelde():
        print()

peter = Student('Peter', ' de Boer', '876867', 'peter@hotmail.com', '21-1-1999') #instance/object van de class Student
roemer = Student('Roemer', ' de Vries', '786987', 'roemer@gmail.com', '22-1-1999') #instance/object van de class Student
siebe = Student('Siebe', ' Postma', '782347', 'siebe@hotmail.com', '23-1-1999') #instance/object van de class Student
lydia = Student('Lydia', ' van der Hoek', '782347', 'lydia@gmail.com', '24-1-1999') #instance/object van de class Student

klas = [peter, lydia, roemer, siebe]

for x in klas:
    print("Naam student: " + x.voornaam + x.achternaam + "\n" + "Studentennummer: " + x.nummer + "\n" + "Mail van student: " + x.mail + "\n" + "Geboortedatum van student: " + x.gebdatum + "\n")
