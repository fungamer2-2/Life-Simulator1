from enum import Enum
import math
import os
from random import choice, uniform, random
from sys import platform

from .const import CONST

_ = lambda s: s


def clamp(val, lo, hi):
    return max(lo, min(val, hi))


class Gender(Enum):
    Male = 0
    Female = 1

    @staticmethod
    def random():
        return Gender.Male if uniform(0, 100) < 51.2 else Gender.Female


def display_event(message):
    print(message)
    press_enter()
    clear_screen()


def press_enter():
    input(_("Press Enter to continue..."))


def clear_screen():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def random_name(gender):

    if gender == Gender.Male:
        return choice(CONST.MALE_NAMES)
    else:
        return choice(CONST.FEMALE_NAMES)


def display_bar(stat_name, val):
    print(stat_name + ": " + draw_bar(val, 100, 25))


def print_align_bars(*name_pairs, show_percent=False):
    l = 0
    for pair in name_pairs:
        name = pair[0]
        if len(name) > l:
            l = len(name)
    for pair in name_pairs:
        name, val = pair[:2]
        if len(pair) >= 3:
            extra = pair[2]
        else:
            extra = ""
        print(
            (name + ": ").ljust(l + 2)
            + draw_bar(val, 100, 25)
            + (f" {val}%" if show_percent else "")
            + extra
        )


def draw_bar(val, max_val, width):
    num = round(width * val / max_val)
    return "[" + "|" * num + " " * (width - num) + "]"


def round_stochastic(value):
    """Randomly rounds a number up or down, based on its decimal part
    For example, 5.3 has a 70% chance to be rounded to 5, 30% chance to be rounded to 6
    And 2.8 has a 80% chance to be rounded to 3, 20% chance to be rounded to 2"""
    low = math.floor(value)
    high = math.ceil(value)
    if value < 0:
        if random() < high - value:
            return low
        return high
    else:
        if random() < value - low:
            return high
        return low


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


def choice_input(*options, return_text=False):
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    val = int_input_range(1, len(options))
    if return_text:
        return options[val - 1]
    return val
