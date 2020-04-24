import time

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def freeSpace(pos):
    return board[pos] == ' '

def printBoard(board):
    print('\n     |     |     ')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |     \n')

def fullBoard(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def won(b, l):
    return  (b[1] == l and b[2] == l and b[3] == l) or \
            (b[4] == l and b[5] == l and b[6] == l) or \
            (b[7] == l and b[8] == l and b[9] == l) or \
            (b[1] == l and b[4] == l and b[7] == l) or \
            (b[2] == l and b[5] == l and b[8] == l) or \
            (b[3] == l and b[6] == l and b[9] == l) or \
            (b[1] == l and b[5] == l and b[9] == l) or \
            (b[7] == l and b[5] == l and b[3] == l)

def playerMove():
    run = True
    while run:
        move = input("Please select a position to insert X between 1 to 9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freeSpace(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("This position has already been selected")
            else:
                print("Type a number between 1 to 9")
        except:
            print("Please type a number")

def machineMove():
    time.sleep(0.3)
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if won(boardcopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random

    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def printTutor():
    print('\n     |     |     ')
    print('  \033[90m1\033[0m  |  \033[90m2\033[0m  |  \033[90m3\033[0m  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  \033[90m4\033[0m  |  \033[90m5\033[0m  |  \033[90m6\033[0m  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  \033[90m7\033[0m  |  \033[90m8\033[0m  |  \033[90m9\033[0m  ')
    print('     |     |     \n')

def main():
    print("================================")
    print("      Welcome to the game")
    print("================================")
    printTutor()

    while not(fullBoard(board)):
        if not(won(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Machine won!!!!\n")
            break
        if not(won(board, 'X')):
            move = machineMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O', move)
                print("Computer inserte O in position", move, ":")
                printBoard(board)
        else:
            print("You won!\n")
            break

    if fullBoard(board):
        print("Draw!")


while True:
    x = input("Do you want to play again? (y/n) ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("\n")
        main()
    else:
        break