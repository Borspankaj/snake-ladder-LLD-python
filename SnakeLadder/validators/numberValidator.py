def is_valid_number(input_str):
    try:
        int_number = int(input_str)
        return True
    except ValueError:
        return False


def is_valid_player_number(value):
    if 2 <= value <= 10:
        return True
    return False


def is_valid_board_size(value):
    if 5 <= value <= 15:
        return True
    return False


def is_valid_choice(value):
    if 0 <= value <= 2:
        return True
    return False


def is_valid_turn(value):
    if value.lower() == "e" or value.lower() == "r":
        return True
    return False


def is_valid_dice(value):
    if 1 <= value <= 3:
        return True
    return False
