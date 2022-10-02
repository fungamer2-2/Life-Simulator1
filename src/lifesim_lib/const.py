import os as _os

DEBUG = False

MALE_NAMES = open("assets/male_names.txt").read().splitlines()
FEMALE_NAMES = open("assets/female_names.txt").read().splitlines()
LAST_NAMES = open("assets/last_names.txt").read().splitlines()

GAME_LANGUAGE = "en"

LANGUAGES = [
	dir
	for dir in _os.listdir("./locale")
	if _os.path.isdir(_os.path.abspath("./locale/" + dir))
]
