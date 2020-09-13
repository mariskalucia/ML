# Mariska de Vries
# 223751
# Gemaakt met Thomas en Menno

# Vragen om de lengte
lengte = float(input("Je lengte meters: "))
# Warning 
if (lengte > 3.00):
    print("Waarschuwing vul u lengte in meters. bijv: 1.85")
    lengte
else: 
# Vragen om het gewicht
    gewicht = float(input("Je gewicht in kilogram: "))

# Berekenen van de BMI
    uitkomst = round(gewicht / (lengte * lengte), 2)

# Het printen van het antwoord
    print("Je BMI is: " + str(uitkomst))

# De fases
    if (uitkomst < 18.51):
        print("U heeft ondergwicht.")
    elif (uitkomst < 26):
        print("U bent gezond.")
    elif (uitkomst > 25):
        print("U heeft overgewicht.")

        
