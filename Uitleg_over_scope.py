# Mariska de Vries
# 223751
# 21-1-2021
# Uilteg over scope

# scope = waar kun je variabelen zien (tot hoever)

# global scope (overal bekend)
punten = 10

def scoren():
    # Local scope (allen op deze plek)
    punten = 50
    print(punten)

print("punten: ", punten)

scoren()

print("punten in scoren() ", punten)