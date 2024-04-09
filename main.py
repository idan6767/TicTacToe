from player import Player
from random import randint

game_over = False
player_1 = Player("X", 0, 0)
player_2 = Player("O", 0, 0)

players = [player_1, player_2]
win = None
choice_tuple = (1, 2, 3)

def reset_game_board():
    whos_playing()
    global game_board
    game_board = []
    for row in range(3):
        row = ['_','_','_']
        game_board.append(row)
    return game_board

def reset_players_moves():
    for player in players:
        player.moves = 0

def reset_players_score():
    for player in players:
        player.score = 0

def whos_playing():
    player_or_computer = input("Do You Want To Play With The Computer? (Y / N):  ").upper()
    if player_or_computer == 'Y':
        player_selection = player_2.is_a_computer = True
    else:
        if player_2.is_a_computer == True:
            reset_players_score()
            reset_players_score()
        player_selection = player_2.is_a_computer = False
        return player_selection

def play(row, column, player):
    game_board[row-1][column-1] = player.symbol

def draw_game_board():
    board = (f"{game_board[0]}\n{game_board[1]}\n{game_board[2]}\n")
    print("=+=+ TIC TAC TOE =+=+")
    print(board)

def get_player_move():
    row = int(input("Isert Row (1-3): "))
    column = int(input("Isert Colomn (1-3): "))

    return column, row

def get_computer_move():
    col = []
    num = 0
    ## computer move selection ##
    # Check for computer block opportunitys ##

    # Slant Block
    left_slent = []
    right_slent = []

    right_slent_tuple = game_board[0][2], game_board[1][1], game_board[2][0]
    right_slent.append(right_slent_tuple)

    for segment in range(3):
        left_slent.append(game_board[segment][segment])

    if right_slent[0].count('X') == 2 and '_' in right_slent[0]:
        print("Right Slent Block!")
        row = right_slent[0].index('_')
        if row == 2:
            column = 0
        if row == 1:
            column = 1
        if row == 0:
            column = 2
        return column + 1 , row + 1

    if left_slent.count('X') == 2 and '_' in left_slent:
        print("Left Slent Block!")
        row = left_slent.index('_')
        if row == 0:
            column = 0
        if row == 1:
            column = 1
        if row == 2:
            column = 2
        return column + 1, row + 1

    # Horizontal Block
    for row in range(3):
        horizontal_x_elements = game_board[row]

        if horizontal_x_elements.count('X') == 2 and '_' in horizontal_x_elements:
            print("Horizontal Block!")
            row = row + 1
            column = horizontal_x_elements.index("_") + 1
            return column, row

        # Vertical Block
        for column in range(3):
            col.append(game_board[column][row])

        if col.count('X') == 2 and '_' in col:
            print("Verticl Block!")
            row = col.index("_") + 1
            column = game_board[row-2].index('X') + 1
            return column, row

        col = []

    row = randint(1, 3)
    column = randint(1, 3)

    return column, row

def add_space():
    print("\n")

def game_over_mode(winner):
    global win
    add_space()

    if winner == "draw":
        print(f'        -|:|-        Its A Draw!        -|:|-     ')
    for player in players:
        if player.symbol == winner:
            player.score += 1
            print(f'     -|:|-        The Winner is {winner}!        -|:|-     ')
    print("||||||||||||||||||||   -SCORE-   ||||||||||||||||||||")
    print(f'||| player 1-"X" |||  {player_1.score}  |:|  {player_2.score}  ||| player 2-"O" |||\n')
    draw_game_board()
    play_again = input("Do You Want To Play Again? (Y / N):  ").upper()

    if play_again == 'N':
        game_over = True
        quit()
        reset_players_score()
    else:
        reset_game_board()
        draw_game_board()
        reset_players_moves()
        add_space()
        game_play()
        win = winner

def check_game_status():
    global game_over
    global rows
    col = []
    elements = []

    # Check for slant win
    slant_row_a = [game_board[0][0],game_board[0][2]]
    slant_row_b = str([game_board[1][1]])
    slant_row_c = [game_board[2][0],game_board[2][2]]

    for player in players:
        # left to right slant
        if player.symbol in slant_row_a[0] and  player.symbol in slant_row_b and player.symbol in slant_row_c[1]:
            winner_symbol = slant_row_b
            game_over_mode(winner_symbol[2])
        # right to left slant
        if player.symbol in slant_row_a[1] and player.symbol in slant_row_b and player.symbol in slant_row_c[0]:
            winner_symbol = slant_row_b
            game_over_mode(winner_symbol[2])

    for row in range(3):
        unique_horizontal_elements = set(game_board[row])
        unique_vertical_elements = set(game_board[row])

        for column in range(3):
            col.append(game_board[column][row])

        # Check for vertical win
        if '_' not in set(col) and len(set(col)) == 1:
            game_over_mode(*set(col))
        col = []

        # Cheak for horizontal win
        if '_' not in unique_horizontal_elements and len(unique_horizontal_elements) == 1:
            game_over_mode(*unique_horizontal_elements)

    # Cheak for draw
    for list in game_board:
        for element in list:
            elements.append(element)
    if "_" not in elements:
        game_over_mode("draw")

    return game_over


def game_play():
    while not game_over:
        for player in players:
            turn = True
            while turn and not game_over:
                draw_game_board()

                if player.is_a_computer == False:
                    print(f"Player ({players.index(player) + 1})-{player.symbol} Turn || moves: {player.moves}")
                    user_choice = get_player_move()

                    while not any(element in choice_tuple for element in user_choice):
                        add_space()
                        print("|| Incorrect choice, Please Choose Between (1-3) ||\n")
                        draw_game_board()
                        print(f"Player ({players.index(player) + 1})-{player.symbol} Turn || moves: {player.moves}")
                        user_choice = get_player_move()

                    add_space()
                else:
                    user_choice = get_computer_move()
                    print(f"Computer Choose: Row: {user_choice[1]} | Column: {user_choice[0]}")
                row = int(user_choice[1])
                column = int(user_choice[0])

                if game_board[row - 1][column - 1] == "_":
                    play(row, column, player)
                    player.moves += 1
                    check_game_status()
                    turn = False
                    add_space()

                else:
                    add_space()
                    print("|| Whhoops! This Spot Already Taken, Plaese Choose another ||\n")


reset_game_board()
game_play()