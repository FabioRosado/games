from random import randrange

the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

available_Plays = ["1. top-L", "2. top-M", "3. top-R",
                   "4. mid-L", "5. mid-M", "6. mid-R",
                   "7. low-L", "8. low-M", "9. low-R"]


def printBoard(board):
    """
    This is the layout of the game, it will change
    depending on the moves made by player/pc
    """
    print("\n")
    print(' '+ the_board['top-L'] +'  | '+ the_board['top-M']+' |  '+ the_board['top-R']+'  ')
    print('____|___|____')
    print(' '+ the_board['mid-L'] +'  | '+ the_board['mid-M']+' |  '+ the_board['mid-R']+'  ')
    print('____|___|____')
    print('    |   |    ')
    print(' '+ the_board['low-L'] +'  | '+ the_board['low-M']+' |  '+ the_board['low-R']+'  ')
    print("\n ")
    return ''


def menu(choice):
    pass


def startGame():
    """
    This will start the game by asking questions to the player
    the game will change depending on those questions
    """
    chosen = False

    print('Welcome to Tic-Tac-Toe!\n')

    while not chosen:
        player_symbol = input("Would you like to be X or O? ").lower()
        if player_symbol == "x":
            player_symbol = "X"
            pc_symbol = "O"
            chosen = True
        elif player_symbol == 'o' or player_symbol == "0":
            player_symbol = 'O'
            pc_symbol = "X"
            chosen = True
        else:
            print("Sorry, you can only choose these two symbols: X or O\n")
    return player_symbol


def playerTurn():
    """
    Will prompt user to choose one of the available plays
    :return:
    """
    print("Please choose one of the following spots on the board\n", available_Plays)
    player_choice = input().lower()

    if player_choice == "1" or player_choice == "top-l" and the_board["top-L"] == " " and the_board["top-L"] != pc_symbol:
        the_board["top-L"] = player_symbol
        available_Plays.remove("1. top-L")
    elif player_choice == "2" or player_choice == "top-m" and the_board["top-M"] == " " and the_board["top-M"] != pc_symbol:
        the_board["top-M"] = player_symbol
        available_Plays.remove("2. top-M")
    elif player_choice == "3" or player_choice == "top-r" and the_board["top-R"] == " "and the_board["top-R"] != pc_symbol:
        the_board["top-R"] = player_symbol
        available_Plays.remove("3. top-R")
    elif player_choice == "4" or player_choice == "mid-l" and the_board["mid-L"] == " " and the_board["mid-L"] != pc_symbol:
        the_board["mid-L"] = player_symbol
        available_Plays.remove("4. mid-L")
    elif player_choice == "5" or player_choice == "mid-m" and the_board["mid-M"] == " " and the_board["mid-M"] != pc_symbol:
        the_board["mid-M"] = player_symbol
        available_Plays.remove("5. mid-M")
    elif player_choice == "6" or player_choice == "mid-r" and the_board["mid-R"] == " " and the_board["mid-R"] != pc_symbol:
        the_board["mid-R"] = player_symbol
        available_Plays.remove("6. mid-R")
    elif player_choice == "7" or player_choice == "low-l" and the_board["low-L"] == " " and the_board["low-L"] != pc_symbol:
        the_board["low-L"] = player_symbol
        available_Plays.remove("7. low-L")
    elif player_choice == "8" or player_choice == "low-m" and the_board["low-M"] == " " and the_board["low-M"] != pc_symbol:
        the_board["low-M"] = player_symbol
        available_Plays.remove("8. low-M")
    elif player_choice == "9" or player_choice == "low-r" and the_board["low-R"] == " " and the_board["low-R"] != pc_symbol:
        the_board["low-R"] = player_symbol
        available_Plays.remove("9. low-R")
    else:
        print("Ooops! Either I didn't understand that or someone used that space before")


def pcTurn(pc_symbol):
    choice = randrange(len(available_Plays))

    the_board[available_Plays[choice][3:]] = pc_symbol
    available_Plays.remove(available_Plays[choice])


def isWon():
    """
    Returns True if a certain play will make the current player
    win the game
    :return: bool
    """
    if the_board['top-L'] == the_board["top-M"] and the_board["top-R"] == the_board["top-M"] and the_board["top-L"] != " ":
        return True
    elif the_board["mid-L"] == the_board["mid-M"] and the_board["mid-R"] == the_board["mid-M"] and the_board["mid-R"] != " ":
        return True
    elif the_board["low-L"] == the_board["low-M"] and the_board["low-R"] == the_board["low-M"] and the_board["low-R"] != " ":
        return True

    elif the_board["top-L"] == the_board["mid-L"] and the_board["low-L"] == the_board["mid-L"] and the_board["mid-L"] != " ":
        return True
    elif the_board["mid-M"] == the_board["top-M"] and the_board["low-M"] == the_board["top-M"] and the_board["mid-M"] != " ":
        return True
    elif the_board["top-R"] == the_board["mid-R"] and the_board["low-R"] == the_board["top-R"] and the_board["top-R"] != " ":
        return True

    elif the_board["mid-M"] == the_board["top-L"] and the_board["mid-M"] == the_board["low-R"] and the_board["mid-M"] != " ":
        return True
    elif the_board["mid-M"] == the_board["low-L"] and the_board["mid-M"] == the_board["top-R"] and the_board["mid-M"] != " ":
        return True

    else:
        return False

# Loop for the game

player_symbol = startGame()
if player_symbol == "X":
    pc_symbol = "O"
else:
    pc_symbol = "X"


while not isWon():

    printBoard(the_board)

    print('\n')
    playerTurn()
    pcTurn(pc_symbol)


print(printBoard(the_board))
