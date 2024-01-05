class Snake:
    def __init__(self, start_position, end_position) -> None:
        self._start_position = start_position
        self._end_position = end_position

    @property
    def start_position(self):
        return self._start_position

    @start_position.setter
    def start_position(self, value):
        self._start_position = value

    @property
    def end_position(self):
        return self._end_position

    @end_position.setter
    def end_position(self, value):
        self._end_position = value
