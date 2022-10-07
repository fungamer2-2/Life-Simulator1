from src.lifesim_lib.lifesim_lib import choice_input, Gender
from src.people.classes.player import Player
from src.people.classes.sibling import Sibling
from src.lifesim_lib.translation import _
from src.lifesim_lib.const import SAVE_PATH
import os
import random
from random import randint
from src.lifesim_lib.lifesim_lib import round_stochastic

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
	mother = player.parents["Mother"]
	father = player.parents["Father"]
	print(_("Your mother is {name}, age {age}.").format(name=mother.name, age=mother.age))
	print(_("Your father is {name}, age {age}.").format(name=father.name, age=father.age))
	if randint(1, 5) < 5:  # 80% chance of having a sibling
		whichlast = random.choice((player.parents["Mother"].lastname, player.parents["Father"].lastname))
		theirsmarts = round_stochastic((randint(0, 100) + player.smarts) / 2)
		theirlooks = round_stochastic((randint(0, 100) + player.looks) / 2)
		sibling = Sibling(whichlast, randint(2, 10), Gender.random(), theirsmarts, theirlooks)
		player.relations.append(sibling)
		print(_("You have a {siblingtype} named {name}, age {age}.").format(siblingtype=sibling.get_translated_type().lower(), name=sibling.name, age=sibling.age))
	return player