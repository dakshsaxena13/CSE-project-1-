
board = ["1","2","3","4","5","6","7","8","9"]

def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])


def check_win():
    # all the winning combinations
    if board[0]==board[1]==board[2]:
        return True
    elif board[3]==board[4]==board[5]:
        return True
    elif board[6]==board[7]==board[8]:
        return True
    elif board[0]==board[3]==board[6]:
        return True
    elif board[1]==board[4]==board[7]:
        return True
    elif board[2]==board[5]==board[8]:
        return True
    elif board[0]==board[4]==board[8]:
        return True
    elif board[2]==board[4]==board[6]:
        return True
    else:
        return False


print("Welcome to Tic Tac Toe")
print("Player 1 = X , Player 2 = O")
show_board()

player = "X"
count = 0

while count < 9:
    print("\nPlayer " + player + " turn")
    pos = input("Enter position (1-9): ")
    pos = int(pos)

    # check if position already filled
    if board[pos-1] == "X" or board[pos-1] == "O":
        print("Position already filled! try again")
        continue

    board[pos-1] = player
    show_board()
    count = count + 1

    if check_win() == True:
        print("\nPlayer " + player + " wins the game!!")
        break

    # change turn
    if player == "X":
        player = "O"
    else:
        player = "X"

if count == 9 and check_win() == False:
    print("\nGame Draw!! no one wins")

print("Thanks for playing")