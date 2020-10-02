# Mariska de Vries
# 223751

# het importeren van random
import random
# de code de gaat door
doorgaan = True

while doorgaan:
    # Hij kiets een random getal tussen de 0 en 7
    beurt_1 = random.randint(1,6)
    print("Beurt 1 = ", beurt_1)
 
    beurt_2 = random.randint(1,6)
    print("Beurt 2 =", beurt_2)

    beurt_3 = random.randint(1,6)
    print("Beurt 3 =", beurt_3)

    beurt_4 = random.randint(1,6)
    print("Beurt 4 =", beurt_4)

    beurt_5 = random.randint(1,6)
    print("Beurt 5 =", beurt_5)

    # Hier telt hij de random getallen bij elkaar op
    print("Totaal = ", beurt_1 + beurt_2 + beurt_3 + beurt_4 + beurt_5)

    # Input om te vragen als je door wilt gaan
    vraag = input("Nog een keer? (j/n): ")
    # Als je n invult dan stopt de code
    if (vraag == "n"):
        doorgaan = False 

 
    