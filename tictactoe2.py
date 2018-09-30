#Tic Tac Toe
import random

def space_check(board, position):

    return board[position] == ' '

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

Board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(Board)
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, please pick 'X' or 'O'.").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Please choose your next position from 1 - 9: "))
    return position

def place_marker(board, marker, position):
    board[position] = marker

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or #down the right
    (board[7] == mark and board[5] == mark and board[3] == mark) or #diagonal bottom right
    (board[1] == mark and board[5] == mark and board[9] == mark)) #diagonal top right

def play_again():
    return input('Do you want to play again? Type Y for yes and N for No.').lower().startswith('y')

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
game_on = True
print('Welcome to Tic Tac Toe!')
player1_marker, player2_marker = player_input()
turn = choose_first()
while game_on == True:
    if turn == 'Player 1':
            print('\n'*100)
            display_board(Board)
            print("Player 1's turn!")
            position = player_choice(Board)
            place_marker(Board, player1_marker , position)
            if win_check(Board, player1_marker):
                display_board(Board)
                print("Player 1 wins!")
                game_on = False
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 2'
    else:
        print('\n'*100)
        display_board(Board)
        print("Player 2's turn!")
        position = player_choice(Board)
        place_marker(Board, player2_marker , position)
        if win_check(Board, player2_marker):
            display_board(Board)
            print("Player 2 wins!")
            game_on = False
        else:
            if full_board_check(Board):
                display_board(Board)
                print("Tie game!")
                game_on = False
            else:
                turn = 'Player 1'
