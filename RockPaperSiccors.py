while True:
    player_a = input("Player A : rock, paper or sciccors :")
    player_b = input("Player B : rock, paper or sciccors :")

    if player_a == "rock" and player_b == "scissors":
        print("player A wins!")
    if player_a == "rock" and player_b == "paper":
        print("Player B wins!")
    if player_a == "rock" and player_b == "rock":
        print("Tie!")
    if player_a == "scissors" and player_b == "scissors":
        print("Tie!")
    if player_a == "scissors" and player_b == "paper":
        print("Player A wins!")
    if player_a == "scissors" and player_b == "rock":
        print("Player B wins!")
    if player_a == "paper" and player_b == "scissors":
        print("Player B wins!")
    if player_a == "paper" and player_b == "paper":
        print("Tie!")
    if player_a == "paper" and player_b == "rock":
        print("Player A wins!")
