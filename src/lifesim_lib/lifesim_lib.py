from enum import Enum
import math
import os
import random
from sys import platform

from src.lifesim_lib.const import *
from src.lifesim_lib.translation import _

class PlayerDied(Exception):
	pass

def clamp(val, lo, hi):
	return max(lo, min(val, hi))
	
def randexpo(lo, avg):
	"Returns a random number exponentially distributed, with a minimum of 'lo', averaging around 'avg'."
	assert lo < avg, "lo must be less than avg"
	return lo + random.expovariate(1/(avg - lo))

def calculate_tax(salary):
	tax = 0
	prev = 0
	brackets = SALARY_TAX_BRACKETS
	for i in range(len(brackets) - 1):
		bound, perc = brackets[i]
		if salary <= bound:
			tax += (salary - prev)*perc
			break
		else:
			tax += (bound - prev)*perc
		prev = bound
	else:
		tax += (salary - prev)*brackets[-1]
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

class Gender(Enum):
	Male = 0
	Female = 1

	@staticmethod
	def random():
		return Gender.Male if random.uniform(0, 100) < 51.2 else Gender.Female

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

def press_enter():
	input(_("Press Enter to continue..."))

def display_event(message):
	print(message)
	press_enter()
	clear_screen()

def display_bar(stat_name, val):
	print(stat_name + ": " + draw_bar(val, 100, 25))

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
	num = round(width * val / max_val)
	return "[" + "|" * num + " " * (width - num) + "]"	

def clear_screen():
	os.system("cls" if platform == "win32" else "clear")