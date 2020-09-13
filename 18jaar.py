leeftijd = int(input("Wat is je leeftijd: "))
if (leeftijd < 18):
    print("Je bent minderjarig.")
elif (leeftijd < 66):
    print("Je bent meerderjarig.")
elif (leeftijd > 65):
    print("Je bent meerderjarig en je hebt recht op pensioen.")
