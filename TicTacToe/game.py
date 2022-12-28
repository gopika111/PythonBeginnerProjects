import random

import board
from player import Player

win_combo = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def analyze_board(player1_moves, player2_moves):
    flag = 0
    print("Player1 Moves")
    print(player1_moves)
    print("Player2 Moves")
    print(player2_moves)
    for combo in win_combo:
        if player1_moves == combo:
            print(f"{player1.name} Won !!!")
            flag = 1
        if player2_moves == combo:
            print(f"{player2.name} Won !!!")
            flag = 1
    return flag


def play(turn, matrix):
    moves_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1_moves = []
    player2_moves = []
    current_player = player1.name
    current_sign = player1.sign
    while (turn < 9):
        print(f"{current_player}'s Turn")
        move = int(input('Enter Your Move (Input any number from 1 to 9 to enter your move) :'))
        matrix = board.get_board(matrix, move, current_sign)
        board.display_matrix(matrix)
        moves_available.remove(move)
        if current_player == player1.name:
            player1_moves.append(move)
        else:
            player2_moves.append(move)
        flag = analyze_board(player1_moves, player2_moves)
        if flag == 1:
            break
        player = change_player(current_player)
        current_player = player.name
        current_sign = player.sign
        turn += 1


def change_player(name):
    if name == player1.name:
        current_player = player2
    else:
        current_player = player1
    return current_player


def get_player_details(sign=''):
    name = input('Enter Player Name : ')
    if sign == '':
        sign = input('Choose the sign x or 0 :')
    player = Player(name, sign)
    return player


print("Let's Start the Game!!!")
print("Provide Player1 Details")
player1 = get_player_details()
print("Provide Player2 Details")
if player1.sign == 'x':
    sign = '0'
else:
    sign = 'x'
player2 = get_player_details(sign)

print('Player1 Details:')
print('Player Name : {0} Sign Chosen : {1}'.format(player1.name, player1.sign))

print('Player2 Details')
print('Player Name : {0} Sign Chosen : {1}'.format(player2.name, player2.sign))

print("Let's Play !!!")
matrix = board.get_intial_matrix()
board.display_matrix(matrix)

turn = 0
play(turn, matrix)
