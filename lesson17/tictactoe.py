import random 
from colorama import Fore, init, Style 
init (autoreset = True)

def display_board(board) :
    print ()
    def colored(cell) :
        if cell == "X" :
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O" or cell == "0" :
            return Fore.BLUE + cell + Style.RESET_ALL
        else :
            return Fore.YELLOW + cell + Style.RESET_ALL
    print (' ' + colored(board[0]) + ' | ' + colored (board[1]) + ' | ' + colored(board[2]))   
    print (Fore.CYAN + "----------"+ Style.RESET_ALL) 
    print (' ' + colored(board[3]) + ' | ' + colored (board[4]) + ' | ' + colored(board[5]))   
    print (Fore.CYAN + "----------"+ Style.RESET_ALL) 
    print (' ' + colored(board[6]) + ' | ' + colored (board[7]) + ' | ' + colored(board[8]))
    print () 

def player_choice () :
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input (Fore.GREEN + "Do you want to be X or O? "+ Style.RESET_ALL).upper()
    if symbol == "X" :
        return ("X", "O")
    else :
        return ("O", "X")
    
def player_move (board, symbol) :
    move = -1
    while move not in range (1, 10) or not board [move - 1] .isdigit() :
        try :
            move = int (input("Enter your move (1-9) : "))
            if move not in range (1, 10) or not board [move - 1].isdigit() :
                print ("Invalid move. Please try again.")
        except ValueError :
            print ("Please enter a value between 1 and 9 ")
    board [move - 1]= symbol 

def ai_move (board, ai_symbol) : 
    for i in range (9) :
        if board [i].isdigit() :
            board_copy = board.copy() 
            board_copy [i]= ai_symbol
            if check_win (board_copy, ai_symbol): 
                board[i] = ai_symbol 
                return
    possible_move = [i for i in range (9) if board[i].isdigit()]
    move = random.choice (possible_move)
    board[move] = ai_symbol 

def check_win (board, symbol) :
    win_condition = [ #tuples
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]                     
    for condition in win_condition :
        if board [condition [0]]== board[condition[1]]== board[condition[2]]== symbol :
            return True 
    return False 

def check_full (board) :
    return all (not spot.isdigit() for spot in board)

def tic_tac_toe () :
    print ("Welcome to tictactoe !") 
    player_name = input (Fore.GREEN +"Enter your name : " + Style.RESET_ALL)
    while True :
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, ai_symbol = player_choice() 
        turn = "player"
        game_on = True 
        while game_on :
            display_board (board)
            if turn == "player" :
                player_move (board, player_symbol)
                if check_win (board, player_symbol) :
                    display_board (board)
                    print ("Congratulations "+ player_name +"! You win")  
                    game_on = False
                else:
                    if check_full (board):
                        display_board(board)
                        print ("It's a tie.") 
                        break 
                    else:
                        turn = "AI"
            else: 
                ai_move (board, ai_symbol)
                if check_win (board, ai_symbol):
                    display_board(board)
                    print ("AI has won the game!")
                    game_on = False
                else :
                    if check_full (board) :
                        display_board (board)
                        print("It's a tie.")
                        break
                    else :
                        turn = "player" 
        play_again = input ("Do you want to play again ? (y, n) : ").lower()
        if play_again != "y":
            print ("Thanks for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()                        



