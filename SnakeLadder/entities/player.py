class Player:
    def __init__(self, name, position=0) -> None:
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
