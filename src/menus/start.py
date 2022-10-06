from src.lifesim_lib.lifesim_lib import choice_input, Gender
from src.people.classes.player import Player
from src.lifesim_lib.translation import _
from src.lifesim_lib.const import SAVE_PATH
import os

def start_menu():
	if os.path.exists(SAVE_PATH):
		choice = choice_input(_("Continue existing game"), _("Start new game"))
		if choice == 1:
			import pickle
			return pickle.load(open(SAVE_PATH, "rb"))
		else:
			os.remove(SAVE_PATH)
	choice = choice_input(_("Random Life"), _("Custom Life"))
		
	if choice == 2:
		first = ""
		last = ""
		while not first:
			first = input(_("Enter your first name: ")).strip()
		while not last:
			last = input(_("Enter your last name: ")).strip()
		print()
		print(_("Choose your gender:"))
		choice = choice_input(_("Male"), _("Female"))
		print()
		player = Player(first, last, Gender.Male if choice == 1 else Gender.Female)
	else:
		 player = Player()
	return player