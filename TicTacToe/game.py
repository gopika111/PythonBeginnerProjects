import random

import board
from player import Player


def play(turn, matrix):
    moves_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    center_piece = 5
    corner_pieces = [1, 3, 7, 9]
    while(turn < 5):
        move = int(input('Enter Your Move (Input any number from 1 to 9 to enter your move) :'))
        matrix = board.get_board(matrix, move, 'x')
        board.display_matrix(matrix)
        moves_available.remove(move)
        if move in corner_pieces:
            corner_pieces.remove(move)
        print("Computer's Turn")
        if center_piece in moves_available:
            matrix = board.get_board(matrix, center_piece, player2.sign)
            moves_available.remove(center_piece)
        elif len(corner_pieces)>0:
            choice = random.choice(corner_pieces)
            matrix = board.get_board(matrix, choice, player2.sign)
            moves_available.remove(choice)
            corner_pieces.remove(choice)
        else:
            choice = random.choice(moves_available)
            matrix = board.get_board(matrix, choice, player2.sign)
            moves_available.remove(choice)
        board.display_matrix(matrix)
        turn +=1

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
matrix = board.get_intial_matrix()
board.display_matrix(matrix)

turn = 0
play(turn, matrix)

