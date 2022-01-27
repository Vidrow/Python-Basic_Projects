tictac = {
    'top_left': '', 'top_mid': '', 'top_right': '',
    'mid_left': '', 'mid_mid': '', 'mid_right': '',
    'bottom_left': '', 'bottom_mid': '', 'bottom_right': ''
}


def main():

    print(
        f" {tictac['top_left']}  | {tictac['top_mid']}  | {tictac['top_right']} ")
    print(f"---+---+---  ")
    print(
        f" {tictac['mid_left']}  | {tictac['mid_mid']}  | {tictac['mid_right']} ")
    print(f"---+---+---  ")
    print(
        f" {tictac['bottom_left']}  | {tictac['bottom_mid']}  | {tictac['bottom_right']}")


def adjust_for_result():
    '''This function takes the values from the tictac dictionary and stores it in a list.
       We will constantly call this function in the main loop to get the updates for tictac dict values.
       Here we are refrencing the dictionary value in the list. We will use this list to compare the possible
       win situations.'''
    list = []
    for v in tictac.values():
        list.append(v)
    return list


'''There are total 8 possible cases for a player to win this game. We will use the list which we created 
   to check if player satisfies the possible case to win.
   If you draw tictac board and number the possible case you will get,
   012 , 258 , 678 , 036 , 048 , 246 , 147 , 345
'''


def result_X(list):
    if list[0] == 'X' and list[1] == 'X' and list[2] == "X":
        print("X turn player wins")
        return True
    elif list[2] == 'X' and list[5] == 'X' and list[8] == "X":
        print("X turn player wins")
        return True
    elif list[6] == 'X' and list[7] == 'X' and list[8] == "X":
        print("X turn player wins")
        return True
    elif list[0] == 'X' and list[3] == 'X' and list[6] == "X":
        print("X turn player wins")
        return True
    elif list[0] == 'X' and list[4] == 'X' and list[8] == "X":
        print("X turn player wins")
        return True
    elif list[2] == 'X' and list[4] == 'X' and list[6] == "X":
        print("X turn player wins")
        return True
    elif list[1] == 'X' and list[4] == 'X' and list[7] == "X":
        print("X turn player wins")
        return True
    elif list[3] == 'X' and list[4] == 'X' and list[5] == "X":
        print("X turn player wins")
        return True


def result_O(list):
    if list[0] == 'O' and list[1] == 'O' and list[2] == "O":
        print("O player turn wins")
        return True
    elif list[2] == 'O' and list[5] == 'O' and list[8] == "O":
        print("O player turn wins")
        return True
    elif list[6] == 'O' and list[7] == 'O' and list[8] == "O":
        print("O player turn wins")
        return True
    elif list[0] == 'O' and list[3] == 'O' and list[6] == "O":
        print("O player turn wins")
        return True
    elif list[0] == 'O' and list[4] == 'O' and list[8] == "O":
        print("O player turn wins")
        return True
    elif list[2] == 'O' and list[4] == 'O' and list[6] == "O":
        print("O player turn wins")
        return True
    elif list[1] == 'O' and list[4] == 'O' and list[7] == "O":
        print("O player turn wins")
        return True
    elif list[3] == 'O' and list[4] == 'O' and list[5] == "O":
        print("O player turn wins")
        return True


'''At first, list=['','','','','','','','','']
   Let take a possible case for example i.e 258
   So, X player to win, list=['','','X','','','X','','','X']
'''

turn = 'X'
while True:
    main()
    adjust_for_result()
    a = result_X(adjust_for_result())
    b = result_O(adjust_for_result())
    if a == True or b == True:
        break
    choice = input("Enter your choice : ")
    if choice == 'quit':
        break
    tictac[choice] = turn
    if turn == 'X':
        turn = 'O'
    elif turn == "O":
        turn = 'X'
