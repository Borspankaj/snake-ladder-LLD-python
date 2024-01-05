import math


class Board:
    def __init__(self) -> None:
        self._players = None
        self._size = None
        self._snakes = []
        self._ladders = []

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        self._players = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value * value

    @property
    def snakes(self):
        return self._snakes

    @snakes.setter
    def snakes(self, snakes):
        self._snakes = snakes[::-1]

    @property
    def ladders(self):
        return self._ladders

    @ladders.setter
    def ladders(self, ladders):
        self._ladders = ladders[::-1]

    def get_snake_at_position(self, position):
        snake = next(
            (snake for snake in self._snakes if snake.end_position == position), None
        )
        return snake

    def get_ladder_at_position(self, position):
        ladder = next(
            (ladder for ladder in self._ladders if ladder.start_position == position),
            None,
        )
        return ladder

    def print_board(self):
        value = math.floor(math.sqrt(self.size))
        for row in range(value, 0, -1):
            if (value - row) % 2 == 0:
                start_col, end_col, step = 1, value + 1, 1
            else:
                start_col, end_col, step = value, 0, -1

            for col in range(start_col, end_col, step):
                position = (row - 1) * value + col
                snake = next(
                    (s for s in self.snakes if s.end_position == position), None
                )
                ladder = next(
                    (l for l in self.ladders if l.start_position == position), None
                )

                if snake:
                    print(f"S({snake.start_position})", end="\t")
                elif ladder:
                    print(f"L({ladder.end_position})", end="\t")
                else:
                    print(position, end="\t")
            print()
