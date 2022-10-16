import gettext, os

from src.lifesim_lib.const import *
from src.menus.main import main_menu
from src.menus.start import start_menu
from src.lifesim_lib.translation import _
from src.lifesim_lib.lifesim_lib import PlayerDied, yes_no, clear_screen

"""
TODO List:
- Add plastic surgery
- Add a way to date people
- Add social media
"""

while True:
	clear_screen()
	try:
		player = start_menu()
		player.print_traits()
		print(_("Age {age}").format(age=player.age))
		while True:
			main_menu(player)
			player.save_game()
	except PlayerDied:
		if not yes_no(_("Would you like to start a new life?")):
			break