
from games.plaingame import plain_start_game
from games.styledgame import styled_start_game
from utils.utilities import clear

def start_game():
    print("Welcome to In Sync")
    print("By  Ocean Man (Ocean-Onion)")
    print("The options are 'S' for styled game or 'P' for plain game.")
    game_choose = input("Choose a game: ")
    if game_choose.lower() == "p":
        clear()
        plain_start_game()
    elif game_choose.lower() == "s":
        clear()
        styled_start_game()
    else:
        print("Invalid game choice.")
        clear()
        start_game()

if __name__ == "__main__":
    start_game()
