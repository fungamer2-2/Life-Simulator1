import gettext

from src.lifesim_lib.const import CONST
from src.menus.main import MainMenu


langs = {}
for lang in CONST.LANGUAGES:
    try:
        l = gettext.translation("lifesim", localedir="locale", languages=[lang])
    except:
        pass

if CONST.GAME_LANGUAGE in langs:
    langs[CONST.GAME_LANGUAGE].install()


MainMenu()
