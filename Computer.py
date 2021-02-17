class Computer:
    def __init__(self, merk, model, besturingssysteem):
        self.__merk = merk
        self.__model = model
        self.__besturingssysteem = besturingssysteem 
        self._opgestart = False
        self._afsluiten = False

    def opstarten(self):
        print(f'Welkom {self.__merk} {self.__besturingssysteem} {self.__model}')
        self._opgestart = True
    
    def opnieuwopstarten(self):
        print(f'{self.__merk} {self.__besturingssysteem} {self.__model} word afgesloten')
        self._afsluiten = True
        print(f'{self.__besturingssysteem} afsluiten')
        print(f'{self.__merk} {self.__besturingssysteem} {self.__model} word opnieuw opgestart')
        self._opstarten = True
        print(f'Welkom {self.__merk} {self.__besturingssysteem} {self.__model}')
    
    def afsluiten(self):
        if (self._opgestart == False):
            print("ERROR")
        elif (self._opgestart == True):
            print(f'{self.__besturingssysteem} is afgesloten')

gamecomputer = Computer('Cool Master', 'Game Computer', 'windows 10')
laptop =  Computer('Lenovo', 'Laptop', 'windows 10')
werkcomputer =  Computer('acer', 'Werk Computer', 'windows 10')


gamecomputer.opstarten()
laptop.opstarten()
werkcomputer.opstarten()
print("")

gamecomputer.opnieuwopstarten()
print("")
laptop.opnieuwopstarten()
print("")
werkcomputer.opnieuwopstarten()
print("")

gamecomputer.afsluiten()
laptop.afsluiten()
werkcomputer.afsluiten()

