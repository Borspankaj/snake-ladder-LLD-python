from ..entities.player import Player
from ..validators import nameValidator as mv
from ..validators import numberValidator as nv


def get_player_input():
    while True:
        n_players = input("Set Players ( 2 - 10 ) : ")

        if not nv.is_valid_number(n_players) or not nv.is_valid_player_number(
            int(n_players)
        ):
            chr = input(
                ("Either Enter a number between ( 2 - 10 ) or Exit ( Enter E )")
            )
            if chr.lower() == "e":
                return None
        else:
            return int(n_players)


def get_board_size():
    while True:
        board_size = input("Set Board Size ( 5 - 15 ) : ")

        if not nv.is_valid_number(board_size) or not nv.is_valid_board_size(
            int(board_size)
        ):
            chr = input(
                ("Either Enter a number between ( 5 - 15 ) or Exit ( Enter E )")
            )
            if chr.lower() == "e":
                return None
        else:
            return int(board_size)


def set_players(n_players):
    players = []
    idx = 1
    while n_players > 0:
        name = input("Enter Name for Player" + str(idx) + ": ")
        if not mv.is_valid_name(name, players):
            print("Invalid Name !! ")
            continue
        idx += 1
        n_players -= 1
        players.append(Player(name))

    return players


def get_dice_count():
    while True:
        dice_count = input("Set Number of Dice ( 1 - 3 ) : ")

        if not nv.is_valid_number(dice_count) or not nv.is_valid_dice(int(dice_count)):
            chr = input(("Either Enter a number between ( 1 - 3 ) or Exit ( Enter E )"))
            if chr.lower() == "e":
                return None
        else:
            return int(dice_count)


def print_rolls(rolls):
    print("You got ", end="")
    for roll in rolls:
        print(str(roll), end=" ")
    print()
