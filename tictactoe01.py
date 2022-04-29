# we indicate the location of our moves by the numbers on the numeric keypad:
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

# we update our game board after each move
# create functions
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# the main function with the game will look like this:
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Your turn, " + turn + ". Where to move?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("This cell is filled.\nWhere to move?")
            continue

        # checking the winner after 5 moves in the game:
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # first line filled
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # second line filled
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # filled third line
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # first column filled
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # filled second column
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # third column filled
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # the first diagonal is filled
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # the second diagonal is filled
                printBoard(theBoard)
                print("\nGame over.\n")
                print(" **** " + turn + " won. ****")
                break

                # If the winner is still not revealed after the ninth move, then we declare a draw:
        if count == 9:
            print("\nGame over.\n")
            print("Draw in game!!")

        # we use the instruction to change players after each move:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # game restart question:
    restart = input("Do you want to repeat the game??(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()

# when the python interpreter reads the source file,
# it executes all the code found in it. Before you start executing commands,
# it defines a few special variables. For example,
# if the interpreter runs some module (source file) as the main program,
# it assigns to the special variable __name__ value "__main__".
# If this file is imported from another module, the variable __name__ will be assigned the name of this module.
# speaking in simple words: the variable __name__ is equal to __main__ only at the entry point to the program - in the script passed to the interpreter at startup:
if __name__ == "__main__":
    game()
