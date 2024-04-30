import json



def printBoard():
    print("\n_______\n|F|F|F|\n-------")
    print("|F|F|F|\n-------")
    print("|F|F|F|\n-------\n\n")

def Winner(board):
    if board[0][0]==board[0][1]and board[0][0]==board[0][2]and board[0][0]==1:
        return 1
    elif board[1][0]==board[1][1]and board[1][0]==board[1][2]and board[1][0]==1:
        return 1
    elif board[2][0]==board[2][1]and board[2][0]==board[2][2]and board[2][0]==1:
        return 1
    elif board[0][0]==board[1][0] and board[0][0]==board[2][0] and board[0][0]==1:
        return 1
    elif board[0][1]==board[1][1] and board[0][1]==board[2][1] and board[0][1]==1:
        return 1
    elif board[0][2]==board[1][2] and board[0][2]==board[2][2] and board[0][2]==1:
        return 1
    elif board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]==1:
        return 1
    elif board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]==1:
        return 1
    if board[0][0]==board[0][1]and board[0][0]==board[0][2]and board[0][0]==2:
        return 2
    elif board[1][0]==board[1][1]and board[1][0]==board[1][2]and board[1][0]==2:
        return 2
    elif board[2][0]==board[2][1]and board[2][0]==board[2][2]and board[2][0]==2:
        return 2
    elif board[0][0]==board[1][0] and board[0][0]==board[2][0] and board[0][0]==2:
        return 2
    elif board[0][1]==board[1][1] and board[0][1]==board[2][1] and board[0][1]==2:
        return 2
    elif board[0][2]==board[1][2] and board[0][2]==board[2][2] and board[0][2]==2:
        return 2
    elif board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]==2:
        return 2
    elif board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]==2:
        return 2
    return 0

name1 = input("Enter Player1 Name: ")
name2 = input("Enter Player2 Name: ")

try:
    ### Check The PLayers Name
    if name1 == "" or name2 == "":
        raise Exception("Players Names Can't Be empty")
    elif name1 == name2:
        raise Exception("Players Name Cant' Be Duplicated")
    ### Cpitalize The Names
    name1 = name1.capitalize()
    name2 = name2.capitalize()
    ### Players Infos
    player1, player2 = dict(name=name1), dict(name=name2)
    player1["Positions"] = []
    player2["Positions"] = []
    ### Welcoming
    print(f"Welcome {name1}.")
    print(f"Welcome {name2}.")
    print("This Is `X O` Game (:D)")
    ### Parameters Of The Game
    name1symbole = input(f"{name1}: Please Choose `X` Or `O`: ")
    if name1symbole.upper() != "X" and name1symbole.upper() != "O":
        raise Exception("Bad Choose For The `X O` Game.")
    elif name1symbole.upper() == "X":
        print(f"{name1}: You'r The `X`.\n{name2}: You'r The `O`.")
        player1["symbol"] = "X"
        player2["symbol"] = "O"
    else:
        print(f"{name1}: You'r The `O`.\n{name2}: You'r The `X`.")
        player1["symbol"] = "O"
        player2["symbol"] = "X"
    ### Instructions To Follow
    print("This Is The Board!")
    printBoard()
    print("On Your Turn Enter The Place That You Want To Put Your Symbol On.")
    print("Place Starts From 1 To 9 From The Left Top Into The Right Buttom.")
    print("The Game Start...\n\n")
    ### GamePlay
    board = [[0,0,0], [0,0,0], [0,0,0]]
    i = 0
    while i < 9:
        symbol = 0
        turn = f"{name1} Turn"
        if i % 2 != 0:
            turn = f"{name2} Turn"
        place = input(f"{turn}, Enter Place To Put You Symbol On It: ")
        if place=="" or len(place)>1 or ord(place)<ord("1") or ord(place)>ord("9"):
            raise Exception("Invalid Syntax.")
        elif i % 2 == 0:
            symbol = 1
            print(f"{name1}: Choose Position {place}.")
            if int(place) in player1["Positions"] or int(place) in player2["Positions"]:
                raise Exception("Can't Use Position Two Times")
            player1["Positions"].append(int(place))
        else:
            symbol = 2
            print(f"{name2}: Choose Position {place}.")
            if int(place) in player1["Positions"] or int(place) in player2["Positions"]:
                raise Exception("Can't Use Position Two Times")
            player2["Positions"].append(int(place))
        if int(place) >= 1 and int(place) <= 3:
            board[0][int(place) - 1] = symbol
        elif int(place) >= 1 and int(place) <= 6:
            board[1][int(place) - 4] = symbol
        else:
            board[2][int(place) - 7] = symbol
        res = Winner(board)
        if res == 1:
            print(f"\n\nThe Winner Is: `{name1}`\n\n")
            break
        elif res == 2:
            print(f"\n\nThe Winner Is: `{name2}`\n\n")
            break
        i += 1
    if i == 9:
        print("\n\nThe Game End With DRAW!\n")
    ### Game Status
    print("Status:")
    print(f"Player1: {player1}")
    print(f"Player2: {player2}")
    print("The Board:")
    for j in board:
        print(j)
    save1 = json.dumps(player1, indent=1, sort_keys=True)
    save2 = json.dumps(player2, indent=1, sort_keys=True)
    # print(save1)
    # print("____________________________________________________")
    # print(save2)
except Exception as err:
    print(f"{err}")
finally:
    print("Process Done, BYE!")