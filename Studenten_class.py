class Student:
    def __init__(self, vnaam, anaam, nr, gebdatum):
        self.voornaam = vnaam
        self.achternaam = anaam
        self.nummer = nr
        self.mail = self.nummer + "@rocfriesepoort.nl"
        self.gebdatum = gebdatum
        self.cijfers = []


    def cijfersVullen(self, num):
        self.cijfers.extend(num)
        #print(self.cijfers)

    
    def berekenGemiddelde(self):
        if len(self.cijfers) > 0:
            return round(sum(self.cijfers)/len(self.cijfers), 1)
        else:
            return "Heeft geen cijfers"


peter = Student("Peter ", "de Boer", "0876867", "24-09-1995")
petra = Student("Petra ", "Zuurstra", "0786987", "16-04-2001")

klas = [peter, petra]

for x in klas:
    print("Naam student: " + x.voornaam + x.achternaam + "\n" + "Studentennummer: " + x.nummer + "\n" + "Mail van student: " + x.mail + "\n" + "Geboortedatum van student: " + x.gebdatum + "\n")

cijfers = [6.4, 7.2, 8.7]
peter.cijfersVullen(cijfers)
print("Het gemiddelde cijfer van Peter: ", peter.berekenGemiddelde())

cijfers = [5.6, 9.1, 7.4]
petra.cijfersVullen(cijfers)
print("Het gemiddelde cijfer van Petra: ", petra.berekenGemiddelde())