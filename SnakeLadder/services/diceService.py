from ..entities.dice import Dice


def roll_dice(dice_count):
    rolls = [Dice.roll() for _ in range(dice_count)]
    total = sum(rolls)

    return set(rolls), total
