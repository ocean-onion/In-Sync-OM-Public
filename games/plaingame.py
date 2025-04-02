import random
from utils.utilities import cards, plain_instructions, clear, wait


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
    for i in range(num_players):
        while True:
            name = input(f"Enter the name of Player {i + 1}: ")
            if name.strip():
                break
            print("Name cannot be empty. Please try again.")
        players.append({"name": name, "deck": []})
    return players


def deal_cards(game_deck, players, cards_per_player):
    clear()
    print("Now we have all players. Lets deal the cards.")
    print("Shuffling and dealing cards...")
    for i in range(cards_per_player):
        for player in players:
            if game_deck:
                card = game_deck.pop(0)
                player["deck"].append(card)

    for player in players:
        player["deck"].sort()
    print("Cards have been dealt!")


def show_cards(player):
    clear()
    print(f"{player['name']}, I will show your cards in 5 seconds.")
    print("Make sure all other players are looking away!")
    clear()
    print("5")
    wait(1)
    print("4")
    wait(1)
    print("3")
    wait(1)
    print("2")
    wait(1)
    print("1")
    wait(1)
    clear()

    print(
        f"{player['name']}, Please view your cards. It may be useful to write them down on some paper."
    )
    print(f"{player['name']}'s cards: {player['deck']}")
    input("Press Enter/Return when you have memorized your cards.")
    clear()


def check_user_deck(player, card):
    if card in player["deck"]:
        return True
    print("You do not have that card!")
    return False


def get_all_remaining_cards(players):
    return [card for player in players for card in player["deck"]]


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
    chosen_player = input("Enter your name: ")

    player_found = False
    for player in players:
        if player["name"].lower() == chosen_player.lower():
            player_found = True
            return player

    if not player_found:
        print("Player name not found. Please enter a valid name.")
        return get_valid_player(players, played_cards)


def get_valid_card(player, played_cards=None):
    chosen_card_input = input("Choose a card to play: ")


    if not chosen_card_input.isdigit():
        print("Please enter a valid card number!")
        return get_valid_card(player, played_cards)

    chosen_card = int(chosen_card_input)

    if not check_user_deck(player, chosen_card):
        return get_valid_card(player, played_cards)

    return chosen_card


def play_turn(players, played_cards, previous_card):
    clear()
    if previous_card is not None:
        print(f"Previous card played was: {previous_card}")
    else:
        print("No cards have been played yet.")

    print("Anyone can play a card at any time.")

    player = get_valid_player(players, played_cards)
    chosen_card = get_valid_card(player, played_cards)

    if check_lowest_possible(players, chosen_card):
        previous_card = play_card(player, chosen_card)
        played_cards.append(chosen_card)
        clear()
        print(f"{player['name']} played the card {chosen_card} successfully!")
        print("Cards left in the game: ",
              len(get_all_remaining_cards(players)))
        return previous_card
    else:
        remaining_cards = get_all_remaining_cards(players)
        lowest_card = min(remaining_cards)
        correct_player = find_correct_player(players, lowest_card)

        print(
            f"Wrong move! {player['name']} played an incorrect card. Game over."
        )
        if played_cards is not None:
            print(
                f"The correct card to play was {lowest_card}, and it should have been played by {correct_player}."
            )
            print(f"Cards played in order before the error: {played_cards}")
            return None
        elif played_cards is None:
            print(
                f"The correct card to play was {lowest_card}, and it should have been played by {correct_player}."
            )
            print("You lost on the first card. ˙◠˙")
            return None
        else:
            print("Something has gone very wrong!")


def game_loop(players):
    previous_card = None
    played_cards = []

    while True:
        if all(len(player["deck"]) == 0 for player in players):
            print("Congratulations! You've successfully completed the game!")
            print(f"Cards played in order: {played_cards}")
            break

        result = play_turn(players, played_cards, previous_card)
        if result is None:
            return
        previous_card = result


def restart_game():
    answer = input("Do you want to play again? (y/n): ").lower()
    if answer == "y":
        plain_start_game()
    else:
        print("Thanks for playing!")


def plain_start_game():
    clear()
    print("Welcome to the game!")
    print("In-Sync is a cooperative card game where timing is everything!")
    int_ask = input("Would you like the instructions? (y/n): ").lower()

    if int_ask == "y":
        plain_instructions()
        clear()
    elif int_ask == "n":
        clear()
    else:
        print("Invalid input!")
        return plain_start_game()

    clear()
    print("Okay, let's start the game!")

    while True:
        num_players_input = input(
            "Enter the number of players (between 2 and 4): ")
        clear()

        if not num_players_input.isdigit() or not (2 <= int(num_players_input)
                                                   <= 4):
            print(
                "Invalid input. Please enter a valid number of players between 2 and 4."
            )
        else:
            num_players = int(num_players_input)
            break

    game_deck, cards_per_player = prepare_game_deck(num_players)
    players = create_players(num_players)
    deal_cards(game_deck, players, cards_per_player)

    for player in players:
        show_cards(player)

    input("Are you ready to begin? Press Enter to start the game...")
    game_loop(players)
    restart_game()


if __name__ == '__main__':
    plain_start_game()
