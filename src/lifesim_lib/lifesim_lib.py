from enum import Enum
import math, os, random, pickle
from sys import platform

from src.lifesim_lib.const import *
from src.lifesim_lib.translation import lang, _


class PlayerDied(Exception):
    pass


class TranslateMarker:
    def __init__(self, string):
        if type(string) != str:
            raise TypeError("only strings are allowed")
        self.string = string

    def raw_str(self):
        return self.string

    def __hash__(self):
        return hash(self.string)

    def __str__(self):
        if lang:
            return lang.gettext(self.string)
        return self.string

    def __eq__(self, other):
        if isinstance(other, TranslateMarker):
            return self.string == other.string
        if isinstance(other, str):
            return self.string == other
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


def get_save_files():
    return os.listdir(SAVE_PATH)


def get_saves(saves=None):
    if saves is None:
        saves = get_save_files()
    players = []
    for filename in saves:
        p = SAVE_PATH + "/" + filename
        players.append(pickle.load(open(p, "rb")))
    return players


def clamp(val, lo, hi):
    return max(lo, min(val, hi))


def randexpo(lo, avg):
    "Returns a random number exponentially distributed, with a minimum of 'lo', averaging around 'avg'."
    assert lo < avg, "lo must be less than avg"
    return lo + random.expovariate(1 / (avg - lo))


def one_in(x):
    return x <= 1 or random.randint(1, x) == 1


def x_in_y(x, y):
    return random.uniform(0, y) < x


def calculate_tax(salary):
    tax = 0
    prev = 0
    brackets = SALARY_TAX_BRACKETS
    for i in range(len(brackets) - 1):
        bound, perc = brackets[i]
        if salary <= bound:
            tax += (salary - prev) * perc
            break
        else:
            tax += (bound - prev) * perc
        prev = bound
    else:
        tax += (salary - prev) * brackets[-1]
    return round(tax)


def round_stochastic(value):
    """Randomly rounds a number up or down, based on its decimal part
    For example, 5.3 has a 70% chance to be rounded to 5, 30% chance to be rounded to 6
    And 2.8 has a 80% chance to be rounded to 3, 20% chance to be rounded to 2"""
    low = math.floor(value)
    high = math.ceil(value)
    if value < 0:
        if random.random() < high - value:
            return low
        return high
    else:
        if random.random() < value - low:
            return high
        return low


COLORS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}


def get_colored(message, color):
    if color is None:
        return str(message)
    if color not in COLORS:
        raise ValueError(f"{color!r} is not a valid ANSI color")
    return f"\u001b[{COLORS[color]}m" + str(message) + "\033[0m"


def print_colored(message, color):
    print(get_colored(message, color))


class Gender(Enum):
    Male = 0
    Female = 1

    @staticmethod
    def random():
        return Gender.Male if random.uniform(0, 100) < 51.2 else Gender.Female


TRAITS_DICT = {
    "CHEERFUL": (
        _("Cheerful"),
        _("It is easier to increase your happiness by doing activities."),
        1,
        ["GRUMPY"],
    ),
    "BOOK_LOVER": (
        _("Book Lover"),
        _(
            "You enjoy reading a good book. You gain more happiness when going to the library."
        ),
        2,
    ),
    "NERD": (
        _("Nerd"),
        _("You gain more smarts by going to the library and doing other activities."),
        2,
    ),
    "GENIUS": (
        _("Genius"),
        _(
            "You tend to be very intelligent. Your Smarts increases over time, and you gain more Smarts when going to the library."
        ),
        4,
    ),
    "FAST_WORKER": (
        _("Fast Worker"),
        _("You tend to work faster, improving your performance over time."),
        1,
        ["SLOW_WORKER", "LAZY"],
    ),
    "WELL_KEPT": (
        _("Well-Kept"),
        _(
            "You tend to be good at taking care of your appearance. Your Looks increases slightly over time."
        ),
        1,
        ["BADLY_KEPT"],
    ),
    "MEDITATOR": (
        _("Meditator"),
        _(
            "You tend to be less stressed than most people. In addition, meditation helps you recover from stress more quickly."
        ),
        2,
    ),
    "GRUMPY": (
        _("Grumpy"),
        _("It is difficult for you to be in a good mood."),
        -1,
        ["CHEERFUL"],
    ),
    "SLOW_WORKER": (
        _("Slow Worker"),
        _("You tend to work slowly, lowering your performance."),
        -1,
        ["FAST_WORKER"],
    ),
    "LAZY": (
        _("Lazy"),
        _(
            "You are often lazy on the job. Your stress and performance decrease over time, and you gain more stress when working harder."
        ),
        -1,
        ["FAST_WORKER"],
    ),
    "SICKLY": (
        _("Sickly"),
        _("You tend to be in poor health, decreasing your Health over time."),
        -1,
    ),
    "BADLY_KEPT": (
        _("Badly-Kept"),
        _("You tend to neglect your appearance, decreasing your Looks over time."),
        -1,
        ["WELL_KEPT"],
    ),
    "THANATOPHOBIA": (
    	_("Thanatophobia"),
    	_("You are afraid of death. You often worry about your own death or the death of a relative, and you lose more Happiness when a relative dies."),
    	-3
    ),
    
    "MOODY": (
        _("Moody"),
        _(
            "Your mood can change more easily. All changes to your Happiness are more intense."
        ),
        0,
        ["NON_EMOTIONAL"]
    ),
    "NON_EMOTIONAL": (
        _("Non-Emotional"),
        _(
            "You don't react much to situations. Any changes to your Happiness are less intense."
        ),
        0,
        ["MOODY"]
    ),
	"FITNESS_ENTHUSIAST": (
        _("Fitness-Enthusiast"),
        _(
            "You really enjoy getting your blood pumping. Any changes to your Health are slightly more intense."
        ),
        +1,
    ),
	"GYM_JUNKIE": (
        _("Gym_Junkie"),
        _(
            "You love hitting the gym and pumping iron. Any changes to your Health are more intense."
        ),
        +2,
    ),
	"BORN_ATHLETE": (
        _("Born_Athlete"),
        _(
            "You love exercise and sport in all its forms. Any changes to your Health are significantly more intense."
        ),
        +3,
    ),
}

#The below is a list of traits that cannot be randomly selected 
NO_RAND_SELECT = {
	"MEDITATOR"
}


class Trait:
    def __init__(self, id, name, desc, val, conflicts=None):
        assert type(val) is int, "Trait value must be an integer"
        self.id = id
        self.name = name
        self.val = val
        self.conflicts = conflicts or []

    @property
    def desc(self):
        return TRAITS_DICT[self.id][1]

    def conflicts_with(self, other):
        return other in self.conflicts

    def roll_selection(self):
        if self.id in NO_RAND_SELECT:
        	return False
        if self.val == 0:
            return True
        return random.randint(1, abs(self.val)) == 1

    def get_color(self):
        if self.val > 0:
            return "green"
        if self.val < 0:
            return "red"
        return None

    @classmethod
    def from_name(cls, name):
        return cls(name, *TRAITS_DICT[name])


pairs = list(TRAITS_DICT.items())
names = [pair[0] for pair in pairs]
ALL_TRAITS = [Trait.from_name(n) for n in names]
ALL_TRAITS_DICT = {names[i]: ALL_TRAITS[i] for i in range(len(names))}


def int_input_range(lo, hi):
    while True:
        try:
            val = int(input())
        except ValueError:
            print(_("Invalid input; try again."))
            continue
        if lo <= val <= hi:
            return val
        else:
            print(_("Invalid input; try again."))


def int_input_range_optional(lo, hi):
    while True:
        try:
            val = input()
            if val is None:
                return None
            val = int(val)
        except ValueError:
            print(_("Invalid input; try again."))
            continue
        if lo <= val <= hi:
            return val
        else:
            print(_("Invalid input; try again."))


def choice_input(*options, return_text=False):
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    val = int_input_range(1, len(options))
    if return_text:
        return options[val - 1]
    return val


def yes_no(message):
    print(message)
    return choice_input(_("Yes"), _("No")) == 1


def random_name(gender):
    if gender == Gender.Male:
        return random.choice(MALE_NAMES)
    else:
        return random.choice(FEMALE_NAMES)


def random_last_name():
    return random.choice(LAST_NAMES)


def press_enter():
    input(_("Press Enter to continue..."))


def display_event(message, cls=True):
    print(message)
    press_enter()
    if cls:
        clear_screen()

def get_bar(val):
	return draw_bar(val, 100, 25)

def display_bar(stat_name, val):
    print(stat_name + ": " + get_bar(val))


def display_data(name, value):
    print(name + ": " + str(value))


def print_align_bars(*name_pairs, show_percent=False):
    l = 0
    for pair in name_pairs:
        name = pair[0]
        if len(name) > l:
            l = len(name)
    for pair in name_pairs:
        name, val = pair[:2]
        if len(pair) >= 3:
            extra = " " + pair[2]
        else:
            extra = ""
        print(
            (name + ": ").ljust(l + 2)
            + draw_bar(val, 100, 25)
            + (f" {val}%" if show_percent else "")
            + extra
        )


def draw_bar(val, max_val, width):
    val = clamp(val, 0, max_val)
    num = round(width * val / max_val)
    return "[" + "|" * num + " " * (width - num) + "]"


def clear_screen():
    os.system("cls" if platform == "win32" else "clear")
