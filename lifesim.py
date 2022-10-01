import gettext

from src.lifesim_lib.const import CONST
from src.menus.main import main_menu
from src.menus.start import start_menu


_ = lambda s: s

langs = {}
for lang in CONST.LANGUAGES:
    try:
        l = gettext.translation("lifesim", localedir="locale", languages=[lang])
    except:
        pass

if CONST.GAME_LANGUAGE in langs:
    langs[CONST.GAME_LANGUAGE].install()

player = start_menu()
while True:
    main_menu(player)
