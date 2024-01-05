from .entities.board import Board
from .validators import numberValidator as nv
from .utils import utils as ut
from .services import boardService as bs
from .services import diceService as ds


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.players = []
        self.winners = []
        self.exit = False
        self.ready = False
        self.dice = None

    def get_game_settings(self):
        while True:
            self.print_options()
            choice = input()

            if choice.lower() == "e":
                self.exit = True
                return

            if choice.lower() == "s" and self.ready == True:
                return
            if not nv.is_valid_number(choice) or not nv.is_valid_choice(int(choice)):
                print("Please Enter valid choice : ")
                continue

            if choice == "0":
                self.board.players = ut.get_player_input()

            elif choice == "1":
                self.board.size = ut.get_board_size()

            elif choice == "2":
                self.dice = ut.get_dice_count()

            if (
                self.board.players != None
                and self.board.size != None
                and self.dice != None
            ):
                self.ready = True

    def print_options(self, options=3):
        print_options = [
            "Set Players (2 - 10)",
            "Set Board Size (5 - 15)",
            "Set Number of Dice (1 - 3)",
        ]

        print("-" * 100)
        for option in range(options):
            print(str(option) + ". " + print_options[option])

        if self.ready:
            print("Start Game ? ( Press S )")
        print("Exit (E)")
        print("-" * 100)

    def generate_game(self):
        self.players = ut.set_players(self.board.players)
        self.board = bs.generate_board(self.board)

    def launch_game(self):
        self.board.print_board()
        while len(self.players) > 1:
            current_player = self.players.pop(0)

            choice = "F"
            while not nv.is_valid_turn(choice):
                self.print_turn_options(current_player.name)
                choice = input()

            if choice.lower() == "e":
                continue

            if choice.lower() == "r":
                self.make_move(current_player)
                if current_player.position >= self.board.size:
                    self.print_winner(current_player)
                    self.winners.append(current_player)
                    ch = input()
                    return

                else:
                    self.players.append(current_player)

            ch = input("Press ENTER to Continue ")
            self.print_positions()

        self.winners = self.players[:]
        self.print_winner(self.players[0])

    def make_move(self, player):
        initial_position = player.position
        current_position = player.position
        final_position = current_position
        chance = 0
        while True:
            rolls, move, bonus = bs.roll_dice(self.dice)
            ut.print_rolls(rolls)

            if chance == 2 and bonus == True:
                print(
                    "You got Double Three in a Row ... resetting to original position"
                )
                final_position = initial_position
                break

            final_position += move
            if final_position <= self.board.size:
                jump = self.board.get_snake_at_position(final_position)
                if jump:
                    print(" Bad Luck !! Snake bit you")
                    print(f"from {jump.end_position} to {jump.start_position}")
                    final_position = jump.start_position

                jump = self.board.get_ladder_at_position(final_position)
                if jump:
                    print("WOW !! climb the ladder to go above")
                    print(f"from {jump.start_position} to {jump.end_position}")
                    final_position = jump.end_position

            if bonus == False:
                break
            chance += 1
            ch = input("Wow !! You got a double .... Press ENTER to roll again")

        print("You are at ", end="")
        print(final_position)
        player.position = final_position

    def print_turn_options(self, name):
        print("-" * 100)
        print(f"{name} !! Its your Turn ")
        print("1. Press (R) to Roll Dice ")
        print("2. Press (E) Resign ")
        print("-" * 100)

    def print_message(self, string):
        width = 100
        print("*" * width)
        print(string.center(width, "-"))
        print("*" * width)

    def print_positions(self):
        print("-" * 100)
        for player in self.players:
            print(player.name + " is at " + str(player.position))
        print("-" * 100)

    def print_winner(self, player):
        text = player.name + " Won !! "
        width = 100
        print("*" * width)
        print(text.center(width, "-"))
        print("*" * width)
