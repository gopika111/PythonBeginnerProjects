import random


def play():
    print("Let's Play Rock Paper Scissor!!!")
    comp_points = 0
    player_name = input("Enter Player Name : ")
    player_points = 0
    no_of_tries = 5
    current_try = 1
    options = ['r', 'p', 's']
    while current_try <= no_of_tries:
        player_inp = input("Enter r for rock, p for paper and s for scissor : ")
        comp_inp = random.choice(options)
        if player_inp == comp_inp:
            player_points+=1
            comp_points+=1
        elif (player_inp == 'p' and comp_inp == 'r') or (player_inp == 'r' and comp_inp == 's')\
                or (player_inp == 's' and comp_inp == 'p'):
                player_points += 1
        else:
                comp_points +=1

        current_try+=1
        print(f"Comp Chose : {comp_inp}")
    print("Points ")
    print(f"{player_name}'s Points : {player_points}")
    print(f"Comp's Points : {comp_points}")
    if player_points == comp_points:
        print("It is a tie!!!")
    elif player_points > comp_points:
        print(f"{player_name} won!!!")
    else:
        print("Comp Won!!!")


play()
