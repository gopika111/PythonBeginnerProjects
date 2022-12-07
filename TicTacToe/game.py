import random

import board
from player import Player

moves_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def play():
    move = input('Enter Your Move (Input any number from 1 to 9 to enter your move) :')
    matrix = board.get_board(move, 'x')
    board.display_matrix(matrix)
    moves_available.remove(int(move))
    print("Computer's Turn")
    matrix = board.get_board(random.choice(moves_available), player2.sign)
    board.display_matrix(matrix)
def get_current_player():
    pass


def get_player_details():
    name = input('Enter Player Name : ')
    sign = input('Choose the sign x or 0 :')
    player1 = Player(name, 'H', sign)
    return player1


comp_sign = ''
player1 = get_player_details()
if player1.sign == 'x':
    comp_sign = '0'
else:
    comp_sign = 'x'
print('Player Details:')
print('Player Name : {0} Sign Chosen : {1}'.format(player1.name, player1.sign))

player2 = Player('Comp', 'C', comp_sign)
print('Player Name : {0} Sign Chosen : {1}'.format(player2.name, player2.sign))

print("Let's Play !!!")
current_board = board.matrix
board.display_matrix(current_board)

play()
