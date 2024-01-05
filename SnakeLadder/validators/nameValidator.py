def is_valid_name(name, players):
    if not name.isalpha():
        return False

    if not 1 <= len(name) <= 10:
        return False

    if any(player.name == name for player in players):
        return False

    return True
