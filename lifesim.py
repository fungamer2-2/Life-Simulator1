import gettext, os
	
from src.lifesim_lib.translation import _
from src.lifesim_lib.const import *
from src.menus.main import main_menu
from src.menus.start import start_menu
from src.lifesim_lib.lifesim_lib import PlayerDied, yes_no, choice_input, clear_screen

"""
TODO List:
- Move some activities into submenus
- Add social media
- Allow children to have traits
"""

def game_loop(player):
	try:
		while True:
			try:
				main_menu(player)
			except Exception as e:
				if type(e) == PlayerDied:
					raise
				clear_screen()
				print(_("An error has occured"))
				import traceback
				message = "".join(traceback.format_exception(type(e), e, e.__traceback__))
				print(message)
				with open("error.log", "w") as f:
					f.write(message)
				print(_("The above error message has been written to error.log"))
				print(_("Please report this bug on Github"))
				print("https://github.com/fungamer2-2/Life-Simulator1/issues/new?template=bug_report.md")
				exit(1)
			else:
				player.save_game()
	except PlayerDied:
		pass

while True:
	clear_screen()
	player = start_menu()
	player.print_traits()
	
	while True:
		print(_("Age {age}").format(age=player.age))
		game_loop(player)
		if player.children and yes_no(_("Would you like to continue as one of your children?")):
			names = [c.name for c in player.children]
			print(_("Which child would you like to continue as?"))
			choice = choice_input(*names)
			c = player.children[choice - 1]
			player.convert_child_to_player(c)
			player.save_game()
		elif yes_no(_("Would you like to start a new life?")):
			break
		else:
			print(_("Thanks for playing!"))
			exit()