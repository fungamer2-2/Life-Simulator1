import gettext, os

from src.lifesim_lib.const import *
from src.menus.main import main_menu
from src.menus.start import start_menu
from src.lifesim_lib.translation import _

langs = {}

dir = os.getcwd()
for lang in LANGUAGES:
	try:
		l = gettext.translation("lifesim", localedir=dir + "/locale", languages=[lang])
	except:
		pass
	else:
		langs[lang] = l
		
player = start_menu()
while True:
	main_menu(player)