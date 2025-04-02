from games.plaingame import plain_start_game
from games.styledgame import BLUE, BOLD, DARKCYAN, END, GREEN, PURPLE, RED, YELLOW, styled_start_game
from utils.logo import display_logo
from utils.utilities import clear, colourprint, colourprint_nl, loading_screen, typinginput, typingprint, wait, loading_files_screen


def welcome():
    colourprint_nl(
        f"{BLUE}░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░{END}"
    )
    colourprint_nl(
        f"{BLUE}░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗{END}"
    )
    colourprint_nl(
        f"{BLUE}░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║{END}"
    )
    colourprint_nl(
        f"{BLUE}░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║{END}"
    )
    colourprint_nl(
        f"{BLUE}░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝{END}"
    )
    colourprint_nl(
        f"{BLUE}░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░{END}"
    )
    colourprint_nl(
        f"{BLUE}              ██╗███╗░░██╗░░░░░░░██████╗██╗░░░██╗███╗░░██╗░█████╗░{END}"
    )
    colourprint_nl(
        f"{BLUE}              ██║████╗░██║░░░░░░██╔════╝╚██╗░██╔╝████╗░██║██╔══██╗{END}"
    )
    colourprint_nl(
        f"{BLUE}              ██║██╔██╗██║█████╗╚█████╗░░╚████╔╝░██╔██╗██║██║░░╚═╝{END}"
    )
    colourprint_nl(
        f"{BLUE}              ██║██║╚████║╚════╝░╚═══██╗░░╚██╔╝░░██║╚████║██║░░██╗{END}"
    )
    colourprint_nl(
        f"{BLUE}              ██║██║░╚███║░░░░░░██████╔╝░░░██║░░░██║░╚███║╚█████╔╝{END}"
    )
    colourprint(
        f"{BLUE}              ╚═╝╚═╝░░╚══╝░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░╚════╝░{END}"
    )
    wait(0.4)
    print()
    print()
    typingprint(f"{DARKCYAN}By  Ocean Man (Ocean-Onion){END}")
    wait(3)
    clear()
    loading_screen()
    start_game()


def start_game():
    clear()
    colourprint(
        f"The options are {PURPLE}'{BOLD}S{END}{PURPLE}' for styled game{END} {GREEN}(Recommended){END}, {BLUE}'{BOLD}P{END}{BLUE}' for plain game,{END} {RED}(Maybe outdated){END} or {YELLOW}'{BOLD}T{END}{YELLOW}' for test functions{END} {RED}(Boring unless dev){END}."
    )
    game_choose = typinginput(
        f"{BOLD}{BLUE}Choose a game: {END}").lower().strip().replace(" ", "")
    if game_choose == "p":
        clear()
        plain_start_game()
    elif game_choose == "s":
        clear()
        styled_start_game()
    else:
        print("Invalid game choice.")
        wait(2)
        clear()
        start_game()


def introduction():
    clear()
    display_logo()
    loading_files_screen()
    wait(2)
    clear()
    welcome()


def hello():
    print("Hello, would you like the introduction (y/n)")
    skip_intro = input().lower()
    if skip_intro == 'y':
        introduction()
    elif skip_intro == 'n':
        start_game()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        hello()


if __name__ == "__main__":
    hello()
