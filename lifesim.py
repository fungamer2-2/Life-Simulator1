import gettext, os

from src.lifesim_lib.const import *
from src.menus.main import main_menu
from src.menus.start import start_menu
from src.lifesim_lib.translation import _
from src.lifesim_lib.lifesim_lib import PlayerDied, yes_no, clear_screen

"""
TODO List:
- Add jobs
- Add a way to date people
- Add social media
"""

while True:
	try:
		player = start_menu()
		while True:
			main_menu(player)
	except PlayerDied:
		if yes_no(_("Would you like to start a new life?")):
			clear_screen()
		else:
			break