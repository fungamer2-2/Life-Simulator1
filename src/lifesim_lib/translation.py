from src.lifesim_lib.const import *
import gettext
import os as _os

_ = lambda s: s

from src.lifesim_lib.lifesim_lib import choice_input

dir = _os.getcwd()
langs = {"en": None}

for lang in LANGUAGES:
	try:
		l = gettext.translation("lifesim", localedir=dir + "/locale", languages=[lang])
	except:
		pass
	else:
		langs[lang] = l

lang_map = {
	"en": "English",
	"es": "Español",
	"ko": "한국인",
	"ja": "日本",
	"ro": "Română",
	"he": "עִברִית"
}

names = []
codes = []
for lang in langs:
	codes.append(lang)
	names.append(lang_map.get(lang, lang))

language = codes[choice_input(*names) - 1]

if language != "en":
	langs[language].install()
	_ = langs[language].gettext