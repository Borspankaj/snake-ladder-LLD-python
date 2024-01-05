import sys

from .game import Game

if __name__ == "__main__":
    game = Game()
    game.print_message("Starting The Game")
    game.get_game_settings()

    if game.exit == True:
        sys.exit()

    game.generate_game()
    game.launch_game()
