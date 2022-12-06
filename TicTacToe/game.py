import board
from player import Player


def play():
    print('Enter')


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
board = board.get_board()
print(board)
