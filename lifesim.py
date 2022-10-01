import gettext

from src.lifesim_lib.const import *
from src.menus.main import main_menu
from src.menus.start import start_menu

_ = lambda s: s

langs = {}

for lang in LANGUAGES:
	try:
		l = gettext.translation("lifesim", localedir="locale", languages=[lang])
	except:
		pass

if GAME_LANGUAGE in langs:
	langs[GAME_LANGUAGE].install()

player = start_menu()
while True:
	main_menu(player)