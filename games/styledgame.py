'''Import all nessarcy functions from libaries.'''
import random
from utils.utilities import colourprint, colourprint_nl, typingprint, typinginput, cards, clear, wait, instructions, color, countdown, colourinput, typingprint_nl, shuffle_screen

# Makes the colours more acessable and easier to use.
RED = color.RED
GREEN = color.GREEN
BLUE = color.BLUE
YELLOW = color.YELLOW
PURPLE = color.PURPLE
CYAN = color.CYAN
BOLD = color.BOLD
UNDERLINE = color.UNDERLINE
DARKCYAN = color.DARKCYAN
END = color.END


def prepare_game_deck(num_players):
    total_cards = len(cards)
    cards_to_remove = random.randint(25, 55)
    available_cards = total_cards - cards_to_remove

    cards_per_player = max(1, available_cards // num_players)

    deck = cards.copy()
    random.shuffle(deck)

    removed_cards = random.sample(deck, cards_to_remove)
    for card in removed_cards:
        deck.remove(card)

    game_deck = deck[:available_cards]
    return game_deck, cards_per_player


def create_players(num_players):
    players = []
    typingprint(f"{PURPLE}Let's get to know the players!{END}")
    for i in range(num_players):
        while True:
            name = typinginput(
                f"{BLUE}Enter the name of Player {i + 1}: {END}")
            if name.strip():
                break
            typingprint(f"{RED}Name cannot be empty. Please try again.{END}")
        typingprint(f"{GREEN}Welcome to the game, {name}!{END}")
        players.append({"name": name, "deck": []})
        wait(0.3)
    return players

'''This function is used to deal the cards to the players. It checks the game deck and then deals the cards to the players. and also make sures that they're are not cards left in the game deck.'''

def deal_cards(game_deck, players, cards_per_player):
    clear()
    typingprint(
        f"{CYAN}Now we have all {len(players)} players. Lets deal the cards.{END}"
    )
    clear()
    shuffle_screen()            
    for i in range(cards_per_player):
        for player in players:
            if game_deck:
                card = game_deck.pop(0)
                player["deck"].append(card)

    for player in players:
        player["deck"].sort()
    typingprint(f"{GREEN}Cards have been dealt!{END}")


def show_cards(player):
    typingprint(
        f"{CYAN}{player['name']}, I will show your cards in 5 seconds.{END}")
    typingprint(
        f"{RED}{BOLD}Make sure all other players are looking away!{END}")
    countdown(5)

    typingprint(
        f"{PURPLE}{player['name']}, Please view your cards. It may be useful to write them down on some paper.{END}"
    )
    card_list = ", ".join([f"{YELLOW}{card}{END}" for card in player["deck"]])
    colourprint(f"{BLUE}{player['name']}'s cards:{END} {card_list}")
    typinginput(
        f"{DARKCYAN}Press Enter/Return when you have memorized your cards.{END}"
    )
    clear()


def check_user_deck(player, card):
    if card in player["deck"]:
        return True
    typingprint(f"{RED}{BOLD}You do not have that card!{END}")
    return False

'''This function gets all the cards in a user deck and then just reutrns that value it is then used to check if the user has the card they want to use.'''
def get_all_remaining_cards(players):
    return [card for player in players for card in player["deck"]]

'''This function is used to check if the card that is played is the lowest possible card in the game. With this function the game could be played out of order and will crash the game.''' 
def check_lowest_possible(players, played_card):
    remaining_cards = get_all_remaining_cards(players)
    if not remaining_cards:
        return True
    lowest_remaining = min(remaining_cards)
    return played_card == lowest_remaining


def find_correct_player(players, card):
    for player in players:
        if card in player["deck"]:
            return player["name"]
    return "Unknown"


def play_card(player, card):
    player["deck"].remove(card)
    return card


def get_valid_player(players, played_cards=None):
    wait(0.3)
    chosen_player = colourinput(f"{PURPLE}Enter your name: {END}")

    player_found = False
    for player in players:
        if player["name"].lower() == chosen_player.lower():
            player_found = True
            return player

    if not player_found:
        typingprint(
            f"{RED}{BOLD}Player name not found. Please enter a valid name.{END}"
        )
        return get_valid_player(players, played_cards)


def get_valid_card(player, played_cards=None):
    wait(0.3)
    chosen_card_input = colourinput(f"{CYAN}Choose a card to play: {END}")

    if not chosen_card_input.isdigit():
        typingprint(f"{RED}{BOLD}Please enter a valid card number!{END}")
        return get_valid_card(player, played_cards)

    chosen_card = int(chosen_card_input)

    if not check_user_deck(player, chosen_card):
        return get_valid_card(player, played_cards)

    return chosen_card


def play_turn(players, played_cards, previous_card):
    clear()
    if previous_card is not None:
        typingprint(
            f"{BLUE}Previous card played was:{END} {YELLOW}{previous_card}{END}"
        )
    else:
        typingprint(f"{YELLOW}{BOLD}No cards have been played yet.{END}")

    typingprint(f"{BLUE}{UNDERLINE}Anyone can play a card at any time.{END}")

    player = get_valid_player(players, played_cards)
    chosen_card = get_valid_card(player, played_cards)

    if check_lowest_possible(players, chosen_card):
        previous_card = play_card(player, chosen_card)
        played_cards.append(chosen_card)
        clear()
        typingprint(
            f"{GREEN}{BOLD}{player['name']} played {chosen_card} successfully!{END}"
        )
        typingprint(
            f"{CYAN}Remaining cards for the game:{END} {BLUE}{len(get_all_remaining_cards(players))}{END}"
        )
        return previous_card
    else:
        remaining_cards = get_all_remaining_cards(players)
        lowest_card = min(remaining_cards)
        correct_player = find_correct_player(players, lowest_card)

        typingprint(
            f"{RED}{BOLD}Wrong move! {player['name']} played an incorrect card. Game over.{END}"
        )
        typingprint(
            f"{YELLOW}The correct card to play was {BOLD}{lowest_card}{END}{YELLOW}, and it should have been played by {BOLD}{correct_player}{END}{YELLOW}.{END}"
        )
        cards_corretly_played = ", " .join([f'{YELLOW}{card}{END}' for card in played_cards])
        typingprint_nl(
            f"{PURPLE}Cards played in order before the error:{END} "
        )
        colourprint(f"{cards_corretly_played}")
        return None


def game_loop(players):
    previous_card = None
    played_cards = []

    while True:
        if all(len(player["deck"]) == 0 for player in players):
            typingprint(
                f"{GREEN}{BOLD}Congratulations! You've successfully completed the game!{END}"
            )
            cards_display = ", ".join(
                [f"{YELLOW}{card}{END}" for card in played_cards])
            typingprint_nl(f"{CYAN}Cards played in order:{END} ") 
            colourprint(f"{cards_display}")
            break

        result = play_turn(players, played_cards, previous_card)
        if result is None:
            return
        previous_card = result


def restart_game():
    answer = typinginput(
        "{PURPLE}Do you want to play again? (y/n): {END}").lower()
    if answer == "y":
        styled_start_game()
    else:
        typingprint(f"{GREEN}{BOLD}Thanks for playing!{END}")


def styled_start_game():
    clear()
    typingprint(f"{YELLOW}{BOLD}Welcome to the game{END}")
    typingprint(
        f"{CYAN}In-Sync is a cooperative card game where timing is everything!{END}")
    int_ask = typinginput(
        f"{PURPLE}Would you like the instructions? (y/n): {END}").lower()

    if int_ask == "y":
        instructions()
        clear()
    elif int_ask == "n":
        clear()
    else:
        typingprint(f"{RED}{BOLD}Invalid input!{END}")
        return styled_start_game()

    typingprint(f"{GREEN}Okay, let's start the game!{END}")
    wait(0.5)

    while True:
        num_players_input = typinginput(
            f"{BLUE}Enter the number of players (between 2 and 4): {END}")
        if num_players_input.startswith("!?"):
            command = num_players_input[2:]
            execute_dev_command(command, [], [])
            continue

        if not num_players_input.isdigit() or not (2 <= int(num_players_input)
                                                   <= 4):
            typingprint(
                f"{RED}{BOLD}Invalid input. Please enter a valid number of players between 2 and 4.{END}"
            )
        else:
            num_players = int(num_players_input)
            break

    game_deck, cards_per_player = prepare_game_deck(num_players)
    players = create_players(num_players)
    deal_cards(game_deck, players, cards_per_player)

    for player in players:
        show_cards(player)

    typinginput(
        f"{GREEN}{BOLD}Are you ready to begin? Press Enter to start the game...{END}"
    )
    game_loop(players)
    restart_game()


if __name__ == '__main__':
    styled_start_game()
