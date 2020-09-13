# Ditctionaries
print("Ditctionaries")
capitals = {"Japan":"Tokyo", "South Korea":"Seoul"}

print(capitals)

print(len(capitals))

capital = capitals["Japan"]
print(capital)

capitals["China"] = "Beijing"
capitals["Australia"] = "canberra"
print(capitals)

for country in capitals:
    capital = capitals[country]
    print("The capital of {} is {}.".format(country, capital))