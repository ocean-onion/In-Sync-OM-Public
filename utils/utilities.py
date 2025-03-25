import time, sys, os, re


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


_color_patterns = {}
_color_dict = {
    'RED': color.RED,
    'GREEN': color.GREEN,
    'YELLOW': color.YELLOW,
    'BLUE': color.BLUE,
    'CYAN': color.CYAN,
    'PURPLE': color.PURPLE,
    'DARKCYAN': color.DARKCYAN,
    'BOLD': color.BOLD,
    'UNDERLINE': color.UNDERLINE,
    'END': color.END
}


def apply_colors(text):
    for color_name, color_code in _color_dict.items():
        pattern = '{' + color_name + '}'
        if pattern in text:
            text = text.replace(pattern, color_code)
    return text + color.END


cards = list(range(1, 71))
lowest_card_playable = 1

_is_posix = os.name == 'posix'


def clear():
    os.system('clear' if _is_posix else 'cls')


def wait(seconds):
    time.sleep(seconds)


def typingprint(text):
    text = apply_colors(text)
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def colourprint(text):
    text = apply_colors(text)
    print(text)
    print()


def typingprint_nl(text):
    text = apply_colors(text)
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typinginput(text):
    text = apply_colors(text)
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    return input()

def colourinput(text):
    text = apply_colors(text)
    return input(text)

def typingintructions(text):
    text = apply_colors(text)
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print()


def countdown(seconds):
    ascii_numbers = {
        1:
        """░░███╗░░
░████║░░
██╔██║░░
╚═╝██║░░
███████╗
╚══════╝""",
        2:
        """██████╗░
╚════██╗
░░███╔═╝
██╔══╝░░
███████╗
╚══════╝""",
        3:
        """██████╗░
╚════██╗
░█████╔╝
░╚═══██╗
██████╔╝
╚═════╝░""",
        4:
        """░░██╗██╗
░██╔╝██║
██╔╝░██║
███████║
╚════██║
░░░░░╚═╝""",
        5:
        """███████╗
██╔════╝
██████╗░
╚════██╗
██████╔╝
╚═════╝░""",
        6:
        """░█████╗░
██╔═══╝░
██████╗░
██╔══██╗
╚█████╔╝
░╚════╝░""",
        7:
        """███████╗
╚════██║
░░░░██╔╝
░░░██╔╝░
░░██╔╝░░
░░╚═╝░░░""",
        8:
        """░█████╗░
██╔══██╗
╚█████╔╝
██╔══██╗
╚█████╔╝
░╚════╝░""",
        9:
        """░█████╗░
██╔══██╗
╚██████║
░╚═══██║
░█████╔╝
░╚════╝░""",
        10:
        """░░███╗░░░█████╗░
░████║░░██╔══██╗
██╔██║░░██║░░██║
╚═╝██║░░██║░░██║
███████╗╚█████╔╝
╚══════╝░╚════╝░""",
        11:
        """░░███╗░░░░███╗░░
░████║░░░████║░░
██╔██║░░██╔██║░░
╚═╝██║░░╚═╝██║░░
███████╗███████╗
╚══════╝╚══════╝""",
        12:
        """░░███╗░░██████╗░
░████║░░╚════██╗
██╔██║░░░░███╔═╝
╚═╝██║░░██╔══╝░░
███████╗███████╗
╚══════╝╚══════╝""",
        13:
        """░░███╗░░██████╗░
░████║░░╚════██╗
██╔██║░░░█████╔╝
╚═╝██║░░░╚═══██╗
███████╗██████╔╝
╚══════╝╚═════╝░""",
        14:
        """░░███╗░░░░██╗██╗
░████║░░░██╔╝██║
██╔██║░░██╔╝░██║
╚═╝██║░░███████║
███████╗╚════██║
╚══════╝░░░░░╚═╝""",
        15:
        """░░███╗░░███████╗
░████║░░██╔════╝
██╔██║░░██████╗░
╚═╝██║░░╚════██╗
███████╗██████╔╝
╚══════╝╚═════╝░""",
        16:
        """░░███╗░░░█████╗░
░████║░░██╔═══╝░
██╔██║░░██████╗░
╚═╝██║░░██╔══██╗
███████╗╚█████╔╝
╚══════╝░╚════╝░""",
        17:
        """░░███╗░░███████╗
░████║░░╚════██║
██╔██║░░░░░░██╔╝
╚═╝██║░░░░░██╔╝░
███████╗░░██╔╝░░
╚══════╝░░╚═╝░░░""",
        18:
        """░░███╗░░░█████╗░
░████║░░██╔══██╗
██╔██║░░╚█████╔╝
╚═╝██║░░██╔══██╗
███████╗╚█████╔╝
╚══════╝░╚════╝░""",
        19:
        """░░███╗░░░█████╗░
░████║░░██╔══██╗
██╔██║░░╚██████║
╚═╝██║░░░╚═══██║
███████╗░█████╔╝
╚══════╝░╚════╝░""",
        20:
        """██████╗░░█████╗░
╚════██╗██╔══██╗
░░███╔═╝██║░░██║
██╔══╝░░██║░░██║
███████╗╚█████╔╝
╚══════╝░╚════╝░""",
        21:
        """██████╗░░░███╗░░
╚════██╗░████║░░
░░███╔═╝██╔██║░░
██╔══╝░░╚═╝██║░░
███████╗███████╗
╚══════╝╚══════╝""",
        22:
        """██████╗░██████╗░
╚════██╗╚════██╗
░░███╔═╝░░███╔═╝
██╔══╝░░██╔══╝░░
███████╗███████╗
╚══════╝╚══════╝""",
        23:
        """██████╗░██████╗░
╚════██╗╚════██╗
░░███╔═╝░█████╔╝
██╔══╝░░░╚═══██╗
███████╗██████╔╝
╚══════╝╚═════╝░""",
        24:
        """██████╗░░░██╗██╗
╚════██╗░██╔╝██║
░░███╔═╝██╔╝░██║
██╔══╝░░███████║
███████╗╚════██║
╚══════╝░░░░░╚═╝""",
        25:
        """██████╗░███████╗
╚════██╗██╔════╝
░░███╔═╝██████╗░
██╔══╝░░╚════██╗
███████╗██████╔╝
╚══════╝╚═════╝░"""
    }

    for i in range(seconds, 0, -1):
        clear()
        if i <= 25 and i in ascii_numbers:
            colourprint(f"{color.RED}{ascii_numbers[i]}{color.END}")
        wait(1)
    clear()


def instructions():
    wait(0.05)
    clear()
    typingprint(f"{color.BLUE}{color.BOLD}Game Instructions:")
    typingintructions(
        f"{color.BLUE} 1. {color.END}{color.PURPLE}Each player receives a set of numbered cards.{color.END}"
    )
    typingintructions(
        f"{color.BLUE} 2. {color.END}{color.PURPLE}The goal is to play the cards in ascending order without speaking."
    )
    typingintructions(
        f"{color.BLUE} 3. {color.END}{color.PURPLE}Players must rely on intuition and teamwork to decide when to play.{color.END}"
    )
    typingintructions(
        f"{color.BLUE} 4. {color.END}{color.PURPLE}If a player plays a card out of order, the game ends.{color.END}"
    )
    typingintructions(
        f"{color.BLUE} 5. {color.END}{color.PURPLE}If all cards are played in the correct order, you win!{color.END}"
    )
    typingprint(f"{color.BLUE}{color.BOLD}\n Tips:{color.END}")
    typingintructions(
        f"{color.BLUE}  - {color.END}{color.PURPLE}{color.UNDERLINE}Stay focused and try to sense the right timing.{color.END}"
    )
    typingintructions(
        f"{color.BLUE}  - {color.END}{color.PURPLE}{color.UNDERLINE}If unsure, wait a moment before playing a card.{color.END}"
    )
    typinginput(f"{color.BLUE}\nPress Enter to continue...{color.END}")
    clear()
    return


def plain_instructions():
    print("Game Instructions:")
    print("1. Each player receives a set of numbered cards.")
    print(
        "2. The goal is to play the cards in ascending order without speaking."
    )
    print(
        "3. Players must rely on intuition and teamwork to decide when to play."
    )
    print("4. If a player plays a card out of order, the game ends.")
    print("5. If all cards are played in the correct order, you win!")
    print("\nTips:")
    print("- Stay focused and try to sense the right timing.")
    print("- If unsure, wait a moment before playing a card.")
    input("\nPress Enter to continue...")
    return
