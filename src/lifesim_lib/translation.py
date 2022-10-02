from src.lifesim_lib.const import *
import gettext
import os as _os

_ = lambda s: s

dir = _os.getcwd()
langs = {}

for lang in LANGUAGES:
	try:
		l = gettext.translation("lifesim", localedir=dir + "/locale", languages=[lang])
	except:
		pass
	else:
		langs[lang] = l

if GAME_LANGUAGE in langs:
	langs[GAME_LANGUAGE].install()
	_ = langs[GAME_LANGUAGE].gettext