from ..entities.snake import Snake
from ..entities.ladder import Ladder
from ..services import diceService as ds
import random
import math


def generate_board(board):
    sl = generate_snakes_ladders(board.size)
    board.snakes = sl["snakes"]
    board.ladders = sl["ladders"]

    return board


def generate_snakes_ladders(size):
    pairs = []
    snakes = []
    ladders = []

    start = 2
    end = size - 1
    value = k = math.floor(math.sqrt(size))

    possible_pairs = (end - start + 1) * (end - start) // 2
    if value > possible_pairs:
        raise ValueError("Cannot Generate ")

    while len(pairs) < value:
        pair = (random.randint(start, end), random.randint(start, end))
        if pair[0] != pair[1] and abs(pair[0] - pair[1]) >= k:
            pairs.append(tuple(sorted(pair)))

    for i in range(len(pairs)):
        if i % 2 == 0:
            snakes.append(Snake(pairs[i][0], pairs[i][1]))

        else:
            ladders.append(Ladder(pairs[i][0], pairs[i][1]))

    return {"snakes": snakes, "ladders": ladders}


def roll_dice(dice_count):
    bonus = False
    rolls, total = ds.roll_dice(dice_count)

    if dice_count == 1 and total == 6:
        bonus = True

    if dice_count == 2 and len(rolls) == 1:
        bonus = True

    if dice_count == 3 and len(rolls) == 1:
        bonus = True

    return rolls, total, bonus
