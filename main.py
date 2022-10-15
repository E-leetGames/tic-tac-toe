# This will be a basic tic-tac-toe exercise.
import os


def clear_board():
    """Creates an empty board"""
    row_a = ["a1", "a2", "a3"]
    row_b = ["b1", "b2", "b3"]
    row_c = ["c1", "c2", "c3"]
    fresh_rows = [row_a, row_b, row_c]
    return fresh_rows


def print_board(current_rows):
    """Displays current board to terminal"""
    os.system('cls')
    print(f" {current_rows[0][0]} | {current_rows[0][1]} | {current_rows[0][2]} ")
    print(f"--------------")
    print(f" {current_rows[1][0]} | {current_rows[1][1]} | {current_rows[1][2]} ")
    print(f"--------------")
    print(f" {current_rows[2][0]} | {current_rows[2][1]} | {current_rows[2][2]} ")


def check_win(current_rows):
    """Checks for all possible win conditions and returns True if any exist"""
    column = 0
    for row in current_rows:
        if row[0] == row[1] == row[2]:
            return True
    while column <= 2:
        if current_rows[0][column] == current_rows[1][column] == current_rows[2][column]:
            return True
        else:
            column += 1
    if current_rows[0][0] == current_rows[1][1] == current_rows[2][2]:
        return True
    if current_rows[0][2] == current_rows[1][1] == current_rows[2][0]:
        return True


def winner(turn, players):
    """Tells the players that the game is won and lets them play again if desired."""
    turn = not turn
    print(f"{players[turn].title()} WON!!!")
    input(f"Press ENTER to play again, or close the window to quit.")
    return True


def get_move(turn, players, current_rows):
    """Makes a list of currently available moves and then requests the user choose one of them."""
    possible_moves = []
    row = 0
    while row <= 2:
        item = 0
        while item <= 2:
            possible_moves.append(current_rows[row][item])
            item += 1
        row += 1

    chosen_move = input(f"{players[turn].title()}, please enter your move: ")

    while chosen_move.lower() not in possible_moves != "X" != "O":
        chosen_move = input(f"{players[turn].title()}, please enter your move in a coordinate format (Ex. b3): ")
    else:
        return chosen_move


def move(turn, current_rows, chosen_move):
    """Places the valid move into the lists and returns them"""
    markers = ["X ", "O "]
    row = 0
    while row <= 2:
        item = 0
        while item <= 2:
            if current_rows[row][item] == chosen_move.lower():
                current_rows[row][item] = markers[turn]

            else:
                item += 1
        row += 1

    return current_rows


def change_turn(turn):
    turn = not turn
    return turn


def introduction():
    """States that a game of tic-tac-toe is about to start and gets player names."""
    print(f"Time to play some Tic-Tac-Toe!")


def get_names(turn):
    """Retrieves player-names from the users. Will limit users to 25 characters."""
    players = ["player_one", "player_two"]

    players[turn] = input(f"Please enter a name for {players[turn]}: ")
    while len(players[turn]) >> 25:
        players[turn] = "player_one"
        players[turn] = input(f"Please enter a name for {players[turn]} that is less than 25 characters: ")

    turn = change_turn(turn)

    players[turn] = input(f"Please enter a name for {players[turn]}: ")
    while len(players[turn]) >> 25:
        players[turn] = "player_two"
        players[turn] = input(f"Please enter a name for {players[turn]} that is less than 25 characters: ")

    change_turn(turn)

    return players


def draw_game():
    """Tells the users that the game has come to a draw and offers them to play again."""
    print(f"The game is a DRAW!")
    input(f"Press ENTER to play again, or close the window to quit.")


while True:
    moves = 0
    victory = False
    rows = clear_board()
    game_state = False
    introduction()
    player_names = get_names(game_state)
    while not victory and moves < 9:
        print_board(rows)
        move(game_state, rows, get_move(game_state, player_names, rows))
        victory = check_win(rows)
        game_state = change_turn(game_state)
        moves += 1
    print_board(rows)
    if victory:
        winner(game_state, player_names)
    else:
        draw_game()
