import os as _os

DEBUG = False

MALE_NAMES = open("assets/male_names.txt").read().splitlines()
FEMALE_NAMES = open("assets/female_names.txt").read().splitlines()
LAST_NAMES = open("assets/last_names.txt").read().splitlines()

SAVE_PATH = filename = _os.getcwd() + "/game_saves"  # + "/gamedata.pickle"

LANGUAGES = [
    dir
    for dir in _os.listdir("./locale")
    if _os.path.isdir(_os.path.abspath("./locale/" + dir))
]

SALARY_TAX_BRACKETS = [
    [9950, 0.1],
    [40525, 0.12],
    [86375, 0.22],
    [164925, 0.24],
    [209425, 0.32],
    [523600, 0.35],
    0.37,
]

from src.lifesim_lib.translation import _

ILLNESSES_TRANSLATIONS = {
	"Depression": _("Depression"),
	"High Blood Pressure": _("High Blood Pressure"),
}

COMPLIMENTS = [
	_("a bubbly personality"),
	_("a champion"),
	_("a gem"),
	_("a genius"),
	_("a jewel"),
	_("a legend"),
	_("a player"),
	_("a revolutionary"),
	_("a smart cookie"),
	_("a treasure"),
	_("a winner"),
	_("a wizard"),
	_("a visionary"),
	_("adorable"),
	_("admirable"),
	_("an OG"),
	_("brave"),
	_("bright"),
	_("brilliant"),
	_("charming"),
	_("clever"),
	_("cool"),
	_("courageous"),
	_("delightful"),
	_("dope"),
	_("elite"),
	_("fascinating"),
	_("fearless"),
	_("fresh"),
	_("gorgeous"),
	_("golden"),
	_("groovy"),
	_("inspiring"),
	_("intelligent"),
	_("magnificent"),
	_("motivating"),
	_("neat"),
	_("nifty"),
	_("one-of-a-kind"),
	_("a perfect 10"),
	_("phenomenal"),
	_("rad"),
	_("smart"),
	_("spectatular"),
	_("stellar"),
	_("strong"),
	_("stunning"),
	_("stylish"),
	_("swell"),
	_("the best"),
	_("the greatest"),
	_("the life of the party"),
	_("unparalled"),
	_("wise"),
	_("wonderful")
]