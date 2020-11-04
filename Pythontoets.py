# Mariska de vries
# 223751

doorgaan = True
print("Als u het programme wilt sluiten typ in 0")
while (doorgaan) :
    getal = int(input("Vul een getal in: "))
    kwadraad = int(input("Door hoeveel wil je het kwadrateren(Kies een getal tussen de 2 t/m 10): "))
    if kwadraad == 2:
        print(getal, kwadraad, "is het kwadraad: " + str(getal * 2)) 
    elif kwadraad == 3:
        print(getal, kwadraad, "is het kwadraad: " + str(getal * 3))
    elif kwadraad == 4:
        print(getal, kwadraad, "is het kwadraad: " + str(getal * 4))
    elif kwadraad == 5:
        print(getal, kwadraad, "is het kwadraad: " + str(getal * 5))
    elif kwadraad == 6:
        print(getal, kwadraad, "is het kwadraad: " + str(getal * 6))
    elif kwadraad == 7:
        print(getal, kwadraad, "is het kwadraad: " + str(getal * 7))
    elif kwadraad == 8:
        print(getal, kwadraad, "is het kwadraad: " + str(getal * 8))
    elif kwadraad == 9:
        print(getal, kwadraad, "is het kwadraad: " + str(getal * 9))
    elif kwadraad == 10:
        print(getal, kwadraad, "is het kwadraad: " + str(getal * 10))
    else:
        print("Programma word gesloten...")
        doorgaan = False


    