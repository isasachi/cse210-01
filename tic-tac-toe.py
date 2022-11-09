#CSE210 - Week 01
#Assignment: Tic-tac-toe game
#Author: Isaac Salirrosas

def main():
    board = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]
    x_player_win = False
    o_player_win = False
    
    draw_grid(board)

    while x_player_win == False or o_player_win == False:
        x_choice = input("x's turn to choose a square (1-9): ")
        mark_square("x", x_choice, board)
        draw_grid(board)

        o_choice = input("o's turn to choose a square (1-9):")
        mark_square("o", o_choice, board)
        draw_grid(board)

        x_player_win = has_player_won("x", board, False)
        o_player_win = has_player_won("o", board, False)

def draw_grid(board):
    for i in range(len(board)):
        print("|".join(board[i]))

def mark_square(player, choice, board):
    if player == "x":
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == str(choice):
                    board[i][j] = player
    elif player == "o":
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == str(choice):
                    board[i][j] = player

def has_player_won(player, board, win):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        win = True
        return win
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        win = True
        return win
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        win = True
        return win
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        win = True
        return win
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        win = True
        return win
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        win = True
        return win
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        win = True
        return win
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        win = True
        return win
    else:
        win = False
        return win

main()