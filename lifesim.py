import gettext, os

from src.lifesim_lib.const import *
from src.menus.main import main_menu
from src.menus.start import start_menu
from src.lifesim_lib.translation import _

"""
TODO List:
- Add jobs
- Add a way to date people
- Add social media
"""

player = start_menu()
while True:
	main_menu(player)