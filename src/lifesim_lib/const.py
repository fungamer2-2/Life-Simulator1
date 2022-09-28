import os


class CONST:
    """Base class for global constants."""

    MALE_NAMES = open("assets/male_names.txt").read().splitlines()
    FEMALE_NAMES = open("assets/female_names.txt").read().splitlines()
    LAST_NAMES = open("assets/last_names.txt").read().splitlines()

    # TODO: Add a way to select the language at the start of the game
    GAME_LANGUAGE = "en"

    LANGUAGES = [
        dir
        for dir in os.listdir("./locale")
        if os.path.isdir(os.path.abspath("./locale/" + dir))
    ]
