# Mariska de Vries
# 223751

# Het inlezen van getallen 
getal1 = int(input("Getal: ")) 
getal2 = int(input("Getal: ")) 
getal3 = int(input("Getal: "))


if (getal1 < getal2 < getal3):
    print("Het grootste getal is: " + str(getal3))
elif (getal2 < getal3 < getal1):
    print("Het grootste getal is: " + str(getal1))
elif (getal1 < getal3 < getal2):
    print("Het grootste getal is: " + str(getal2))
