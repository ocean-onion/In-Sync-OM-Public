import games.plaingame as plaingame
import games.styledgame as styledgame
import utils.utilities as utilities
from utils.utilities import clear, colourprint, color, wait
import os, sys


def test_start_game():
    clear()
    print("Function Testing Utility\n")

    modules = {"1": plaingame, "2": styledgame, "3": utilities}

    print("Available Modules:")
    print("1: games.plaingame")
    print("2: games.styledgame")
    print("3: utils.utilities")

    module_choice = input("\nSelect a module (1-3): ")
    if module_choice not in modules:
        print("Invalid choice!")
        return

    module = modules[module_choice]

    functions = {}
    function_list = []

    if module == plaingame:
        function_list = [
            "prepare_game_deck", "create_players", "deal_cards", "show_cards",
            "check_user_deck", "get_all_remaining_cards",
            "check_lowest_possible", "find_correct_player", "play_card",
            "get_valid_player", "get_valid_card", "play_turn", "game_loop",
            "restart_game", "plain_start_game"
        ]
    elif module == styledgame:
        function_list = [
            "prepare_game_deck", "create_players", "deal_cards", "show_cards",
            "check_user_deck", "get_all_remaining_cards",
            "check_lowest_possible", "find_correct_player", "play_card",
            "get_valid_player", "get_valid_card", "play_turn", "game_loop",
            "restart_game", "styled_start_game"
        ]
    elif module == utilities:
        function_list = [
            "clear", "wait", "typingprint", "colourprint", "typinginput",
            "instructions", "plain_instructions", "apply_colors", "countdown"
        ]

    for i, name in enumerate(function_list, 1):
        if hasattr(module, name):
            functions[str(i)] = (name, getattr(module, name))
            print(f"{i}: {name}")

    if module == utilities:
        print("\nAdditional Options:")
        print("C: Test color constants")

    function_choice = input("\nSelect a function or option: ")

    if module == utilities and function_choice.upper() == "C":
        test_colors()
        return

    if function_choice not in functions:
        print("Invalid choice!")
        return

    function_name, function = functions[function_choice]

    print(f"\nRunning {function_name}...")

    if function_name == "typingprint" or function_name == "colourprint":
        text = input("Enter text to display: ")
        color_option = input("Add color formatting? (y/n): ").lower()
        if color_option == "y":
            text = add_color_to_text(text)
        result = function(text)
    elif function_name == "typinginput":
        text = input("Enter prompt text: ")
        color_option = input("Add color formatting? (y/n): ").lower()
        if color_option == "y":
            text = add_color_to_text(text)
        result = function(text)
    elif function_name == "wait":
        seconds = float(input("Enter seconds to wait: "))
        result = function(seconds)
    elif function_name == "apply_colors":
        text = input("Enter text with color tags (e.g., {RED}text{END}): ")
        result = function(text)
        print(f"Result: {result}")
    elif function_name == "countdown":
        seconds = int(
            input("Enter seconds to count down (1-25 recommended): "))
        result = function(seconds)
    elif function_name == "check_user_deck":
        deck_str = input(
            "Enter a comma-separated list of cards (e.g., 1,5,10): ")
        player = {
            "name": "Test Player",
            "deck": [int(c.strip()) for c in deck_str.split(",") if c.strip()]
        }
        card = int(input("Enter the card to check: "))
        result = function(player, card)
        print(f"Result: {result}")
    elif function_name == "play_card":
        deck_str = input(
            "Enter a comma-separated list of cards (e.g., 1,5,10): ")
        player = {
            "name": "Test Player",
            "deck": [int(c.strip()) for c in deck_str.split(",") if c.strip()]
        }
        card = int(input("Enter the card to play: "))
        if card in player["deck"]:
            result = function(player, card)
            print(f"Remaining deck: {player['deck']}")
        else:
            print(f"Card {card} not in deck {player['deck']}")
    elif function_name == "get_all_remaining_cards":
        num_players = int(input("Enter number of players: "))
        players = []
        for i in range(num_players):
            deck_str = input(
                f"Enter a comma-separated list of cards for Player {i+1}: ")
            player = {
                "name": f"Player {i+1}",
                "deck":
                [int(c.strip()) for c in deck_str.split(",") if c.strip()]
            }
            players.append(player)
        result = function(players)
        print(f"Result: {result}")
    elif function_name == "check_lowest_possible":
        num_players = int(input("Enter number of players: "))
        players = []
        for i in range(num_players):
            deck_str = input(
                f"Enter a comma-separated list of cards for Player {i+1}: ")
            player = {
                "name": f"Player {i+1}",
                "deck":
                [int(c.strip()) for c in deck_str.split(",") if c.strip()]
            }
            players.append(player)
        played_card = int(input("Enter the card to check: "))
        result = function(players, played_card)
        print(f"Result: {result}")
    elif function_name == "find_correct_player":
        num_players = int(input("Enter number of players: "))
        players = []
        for i in range(num_players):
            deck_str = input(
                f"Enter a comma-separated list of cards for Player {i+1}: ")
            player = {
                "name": f"Player {i+1}",
                "deck":
                [int(c.strip()) for c in deck_str.split(",") if c.strip()]
            }
            players.append(player)
        card = int(input("Enter the card to find: "))
        result = function(players, card)
        print(f"Result: {result}")
    elif function_name == "prepare_game_deck":
        num_players = int(input("Enter number of players (2-4): "))
        game_deck, cards_per_player = function(num_players)
        print(f"Game deck created with {len(game_deck)} cards.")
        print(f"Each player will receive {cards_per_player} cards.")
        print(f"Sample of cards in deck: {game_deck[:5]}...")
    elif function_name == "create_players":
        print("This function requires user input for player names.")
        num_players = int(input("Enter number of players for testing (1-4): "))
        result = function(num_players)
        print(f"Created {len(result)} players:")
        for player in result:
            print(f"- {player['name']}")
    elif function_name == "deal_cards":
        print("Setting up test data for deal_cards...")
        num_players = int(input("Enter number of players (2-4): "))
        game_deck = list(range(1, 31))
        players = [{
            "name": f"Player {i+1}",
            "deck": []
        } for i in range(num_players)]
        cards_per_player = int(input("Enter cards per player (1-10): "))
        function(game_deck, players, cards_per_player)
        print("Cards dealt. Players now have:")
        for player in players:
            print(f"- {player['name']}: {player['deck']}")
    elif function_name == "show_cards":
        deck_str = input(
            "Enter a comma-separated list of cards (e.g., 1,5,10): ")
        player = {
            "name": "Test Player",
            "deck": [int(c.strip()) for c in deck_str.split(",") if c.strip()]
        }
        function(player)
    elif function_name == "get_valid_player":
        print("Setting up test players...")
        num_players = int(input("Enter number of players (2-4): "))
        players = []
        for i in range(num_players):
            name = input(f"Enter name for Player {i+1}: ")
            deck_str = input(
                f"Enter a comma-separated list of cards for {name}: ")
            player = {
                "name": name,
                "deck":
                [int(c.strip()) for c in deck_str.split(",") if c.strip()]
            }
            players.append(player)
        print("\nTesting get_valid_player function. Enter a player name:")
        result = function(players)
        print(f"Selected player: {result['name']}")
    elif function_name == "get_valid_card":
        deck_str = input(
            "Enter a comma-separated list of cards (e.g., 1,5,10): ")
        player = {
            "name": "Test Player",
            "deck": [int(c.strip()) for c in deck_str.split(",") if c.strip()]
        }
        print(
            f"\nTesting get_valid_card function for {player['name']} with deck {player['deck']}."
        )
        result = function(player)
        print(f"Selected card: {result}")
    elif function_name == "play_turn":
        print("Setting up a test game...")
        num_players = int(input("Enter number of players (2-4): "))
        players = []
        for i in range(num_players):
            name = input(f"Enter name for Player {i+1}: ")
            deck_str = input(
                f"Enter a comma-separated list of cards for {name}: ")
            player = {
                "name": name,
                "deck":
                [int(c.strip()) for c in deck_str.split(",") if c.strip()]
            }
            players.append(player)
        played_cards = []
        previous_card = None
        prev_card_str = input("Enter previous card (leave blank for none): ")
        if prev_card_str.strip() and prev_card_str.isdigit():
            previous_card = int(prev_card_str)
        print("\nTesting play_turn function. Play a card:")
        result = function(players, played_cards, previous_card)
        print(f"Result: {result}")
        print(f"Updated played cards: {played_cards}")
    elif function_name == "game_loop":
        print("Setting up a test game...")
        num_players = int(input("Enter number of players (2-4): "))
        players = []
        for i in range(num_players):
            deck_str = input(
                f"Enter a comma-separated list of cards for Player {i+1}: ")
            player = {
                "name": f"Player {i+1}",
                "deck":
                [int(c.strip()) for c in deck_str.split(",") if c.strip()]
            }
            players.append(player)
        print(
            "\nStarting game loop with these players. Play cards in order to win!"
        )
        function(players)
    elif function_name in [
            "restart_game", "plain_start_game", "styled_start_game",
            "instructions", "plain_instructions"
    ]:
        print(f"The function {function_name} is a full game flow function.")
        run_it = input(
            "Do you want to run this entire function? (y/n): ").lower()
        if run_it == 'y':
            result = function()
        else:
            print("Function execution skipped.")
    else:
        try:
            result = function()
        except TypeError as e:
            print(f"Error: {e}")
            print(
                "This function requires parameters that aren't handled by the test utility."
            )
            return

    print(f"{color.BLUE}Function completed.")

    test_function_q = input(
        f"{color.END}Do you want to test another function? (y/n): ").lower()
    if test_function_q.lower() == 'y':
        test_start_game()
    elif test_function_q.lower() == 'n':
        print("Returning to main menu...")
        wait(2)
        clear()

        os.execv(sys.executable, [sys.executable] + ['-m', 'main'])


def test_colors():
    clear()
    print("Color Constants Testing\n")

    color_options = {
        "1": ("RED", color.RED),
        "2": ("GREEN", color.GREEN),
        "3": ("BLUE", color.BLUE),
        "4": ("YELLOW", color.YELLOW),
        "5": ("PURPLE", color.PURPLE),
        "6": ("CYAN", color.CYAN),
        "7": ("DARKCYAN", color.DARKCYAN),
        "8": ("BOLD", color.BOLD),
        "9": ("UNDERLINE", color.UNDERLINE),
        "10": ("END", color.END)
    }

    print("Available Colors:")
    for key, (name, _) in color_options.items():
        print(f"{key}: {name}")

    print("\nDisplay Options:")
    print("A: Show all colors")
    print("S: Select specific color")
    print("C: Combine multiple colors")
    print("M: Return to Main Menu")

    option = input("\nChoose an option: ").upper()

    if option == "A":
        for name, code in color_options.values():
            print(f"{code}This text is in {name}{color.END}")

    elif option == "S":
        color_choice = input("\nSelect a color (1-10): ")
        if color_choice in color_options:
            name, code = color_options[color_choice]
            text = input(f"Enter text to display in {name}: ")
            print(f"{code}{text}{color.END}")
        else:
            print("Invalid color choice!")

    elif option == "C":
        print(
            "Enter comma-separated color numbers to combine (e.g., 1,8 for RED and BOLD):"
        )
        selections = input().split(",")
        text = input("Enter text to display: ")

        combined_code = ""
        for selection in selections:
            if selection.strip() in color_options:
                _, code = color_options[selection.strip()]
                combined_code += code

        print(f"{combined_code}{text}{color.END}")

    elif option == "M":
        clear()
        print("Returning to main menu...")
        wait(2)
        clear()
        os.execv(sys.executable, [sys.executable] + ['-m', 'main'])
        return

    else:
        print("Invalid option!")

    if input("\nTest colors again? (y/n): ").lower() == 'y':
        test_colors()
    else:
        test_start_game()


def add_color_to_text(text):
    print("\nAvailable Color Tags:")
    print("1: {RED}")
    print("2: {GREEN}")
    print("3: {BLUE}")
    print("4: {YELLOW}")
    print("5: {PURPLE}")
    print("6: {CYAN}")
    print("7: {DARKCYAN}")
    print("8: {BOLD}")
    print("9: {UNDERLINE}")
    print("10: {END}")

    print("\nExample: {RED}This is red{END} and this is normal")

    choice = input(
        "\nDo you want to modify your text with color tags? (y/n): ").lower()
    if choice == 'y':
        return input("Enter your formatted text with color tags: ")
    return text


if __name__ == "__main__":
    test_start_game()
