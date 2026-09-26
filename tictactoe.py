import random
XOX=[" "]*9
print(XOX)
def disp_board():
    print()
    print(XOX[0], "|", XOX[1] ,"|", XOX[2] )
    print("----------")
    print(XOX[3], "|", XOX[4] ,"|", XOX[5] )
    print("---------")
    print(XOX[6], "|", XOX[7] ,"|", XOX[8] )
    print("---------")
    print()

def check_winner():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if XOX[a] == XOX[b] == XOX[c] and XOX[a] != " ":
            return XOX[a]

    if " " not in XOX:
        return "Draw"

    return None

while True:
    disp_board()

    # Human move
    move = int(input("Enter your move (1-9): ")) - 1

    if move < 0 or move > 8 or XOX[move] != " ":
        print("Invalid move!")
        continue

    XOX[move] = "X"

    winner = check_winner()
    if(winner==("Draw")):
        disp_board()
        print("Draw")
        break;
    if winner:
        disp_board()
        print("Winner is:", winner)
        break

    # Robot move
    empty = [i for i in range(9) if XOX[i] == " "]
    robot_move = random.choice(empty)
    XOX[robot_move] = "O"

    print("Robot chose:", robot_move + 1)

    winner = check_winner()
    if(winner=="Draw"):
        disp_board()
        print("Draw")
        break;
    if winner:
        disp_board()
        print("Winner is:", winner)
        break


            
