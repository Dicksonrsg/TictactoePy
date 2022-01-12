#Two Player TicTacToe Game in Python
''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' Function to print updated board '''
def showBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    
def game():
    
    turn = 'X'
    count = 0
    
    for i in range(10):
        showBoard(theBoard)
        print("It's your turn, " + turn + ". Where to?")
        move = input()
        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\n Where to?")
            continue
        
        #Check if a player has won after 5 turns
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] !=' ': #Top across
                showBoard(theBoard)
                print("\nGame Over.\n")
                print("*** " + turn + " won. ***")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] !=' ': #Middle across
                showBoard(theBoard)
                print("\nGame Over.\n")
                print("*** " + turn + " won. ***")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] !=' ': #Bottom across
                showBoard(theBoard)
                print("\nGame Over.\n")
                print("*** " + turn + " won. ***")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] !=' ': #Left down
                showBoard(theBoard)
                print("\nGame Over.\n")
                print("*** " + turn + " won. ***")
                break 
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] !=' ': #Middle down
                showBoard(theBoard)
                print("\nGame Over.\n")
                print("*** " + turn + " won. ***")
                break   
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] !=' ': #Right down
                showBoard(theBoard)
                print("\nGame Over.\n")
                print("*** " + turn + " won. ***")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] !=' ': #Diagonal 1
                showBoard(theBoard)
                print("\nGame Over.\n")
                print("*** " + turn + " won. ***")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] !=' ': #Diagonal 2
                showBoard(theBoard)
                print("\nGame Over.\n")
                print("*** " + turn + " won. ***")
                break 
        
        #If neither X nor O has won and the board is full, it's a tie.    
        if count == 9:
            print("\nGame over.\n")
            print("It's a tie!!")    
        
        #Changing players
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    #Asking players whether they play again
    restart = input("Would you like to play again? (y/n)")
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key] = ' '
        
        game()
    elif restart == 'n' or restart == 'N':
        print("Thanks for playing.")
        SystemExit

#if __name__ == "_main_":
game()