# Conditionals
print("Conditionals")
print("Does 3 equal 3?")
if 3 == 3:
    print(True)

x = 3
y = 2
print("Is {} greater then {}?".format(x, y))
if x > y:
    print(True)
else:
    print(False)

print("Is {} greater then {}?".format(x, y))
x = 2
y = 3
if x > y:
    print(True)
else:
    print(False)

player_a = "rock"
player_b = "paper"

if player_a == "rock" and player_b == "rock":
    print("Someone chose rock!")

if player_a == "rock" and player_b == "scissors":
    print("player A wins!")
elif player_a == "rock" and player_b == "paper":
    print("Player B wins!")
else:
    print("Tie!")