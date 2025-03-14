import sys
from utils.utilities import color, colourprint, typingprint, clear


def execute_dev_command(command, players, played_cards):
    if command == "players":
        players_list(players)
    elif command == "cards":
        show_cards(players)
    elif command == "played":
        show_played_cards(played_cards)
    elif command == "all":
        show_all_info(players, played_cards)
    elif command == "clear":
        clear()
    elif command == "exit":
        sys.exit(0)
    elif command == "help":
        show_help()
    else:
        typingprint(f"{color.RED}Unknown dev command: {command}{color.END}")
        typingprint(
            f"{color.RED}Type '!?help' for a list of available commands.{color.END}"
        )


def players_list(players):
    colourprint(f"{color.CYAN}Players:{color.END}")
    for player in players:
        colourprint(
            f"{color.BLUE}{player['name']} - {len(player['deck'])} cards{color.END}"
        )


def show_cards(players):
    colourprint(f"{color.CYAN}Cards per player:{color.END}")
    for player in players:
        card_list = ", ".join(
            [f"{color.YELLOW}{card}{color.END}" for card in player["deck"]])
        colourprint(f"{color.BLUE}{player['name']}: {color.END}{card_list}")


def show_played_cards(played_cards):
    if not played_cards:
        colourprint(f"{color.YELLOW}No cards have been played yet.{color.END}")
        return

    cards_display = ", ".join(
        [f"{color.YELLOW}{card}{color.END}" for card in played_cards])
    colourprint(f"{color.CYAN}Cards played so far:{color.END} {cards_display}")


def show_all_info(players, played_cards):
    players_list(players)
    show_cards(players)
    show_played_cards(played_cards)


def show_help():
    colourprint(f"{color.GREEN}Available Dev Commands:{color.END}")
    colourprint(
        f"{color.BLUE}!?players{color.END} - Show list of players and their card count"
    )
    colourprint(f"{color.BLUE}!?cards{color.END} - Show all players' cards")
    colourprint(
        f"{color.BLUE}!?played{color.END} - Show cards that have been played")
    colourprint(f"{color.BLUE}!?all{color.END} - Show all game information")
    colourprint(f"{color.BLUE}!?clear{color.END} - Clear the screen")
    colourprint(f"{color.BLUE}!?exit{color.END} - Exit the game")
    colourprint(f"{color.BLUE}!?help{color.END} - Show this help information")
