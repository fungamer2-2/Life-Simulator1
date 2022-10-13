import os as _os

DEBUG = False

MALE_NAMES = open("assets/male_names.txt").read().splitlines()
FEMALE_NAMES = open("assets/female_names.txt").read().splitlines()
LAST_NAMES = open("assets/last_names.txt").read().splitlines()

SAVE_PATH = filename = _os.getcwd() + "/game_saves"  # + "/gamedata.pickle"

LANGUAGES = [
    dir
    for dir in _os.listdir("./locale")
    if _os.path.isdir(_os.path.abspath("./locale/" + dir))
]

SALARY_TAX_BRACKETS = [
    [9950, 0.1],
    [40525, 0.12],
    [86375, 0.22],
    [164925, 0.24],
    [209425, 0.32],
    [523600, 0.35],
    0.37,
]
