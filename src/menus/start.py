from src.lifesim_lib.lifesim_lib import choice_input, Gender
from src.people.classes.player import Player

_ = lambda s: s

def start_menu():
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