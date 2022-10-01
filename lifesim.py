import random, math, os
from random import randint
from enum import Enum
import gettext
from sys import platform

def clamp(val, lo, hi):
	return max(lo, min(val, hi))

_ = lambda s: s
	
LANGUAGES = [dir for dir in os.listdir("./locale") if os.path.isdir(os.path.abspath("./locale/" + dir))]

langs = {}
for lang in LANGUAGES:
	try:
		l = gettext.translation("lifesim", localedir="locale", languages=[lang])
	except:
		pass
		
GAME_LANGUAGE = "en" #TODO: Add a way to select the language at the start of the game
if GAME_LANGUAGE in langs:
	langs[GAME_LANGUAGE].install()

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

class Person:

	def __init__(self, firstname, lastname, age, gender, happiness, health, smarts, looks):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.gender = gender
		self.happiness = happiness
		self.health = health
		self.smarts = smarts
		self.looks = looks
		self.alive = True
		
	def age_up(self):
		self.age += 1
		self.change_happiness(randint(-3, 3))
		self.change_health(randint(-3, 3))
		self.change_smarts(randint(-3, 3))
		self.change_looks(randint(-3, 3))
		
	def death_check(self):
		return self.age > randint(98, 122) or (self.age > randint(80 + self.health//12, 90 + self.health//3) and randint(1, 100) <= 65)
		
	def change_happiness(self, amount):
		self.happiness = clamp(self.happiness + amount, 0, 100)
		
	def change_health(self, amount):
		self.health = clamp(self.health + amount, 0, 100)
	
	def change_smarts(self, amount):
		self.smarts = clamp(self.smarts + amount, 0, 100)

	def change_looks(self, amount):
		self.looks = clamp(self.looks + amount, 0, 100)
	
	@property
	def name(self):
		return self.firstname + " " + self.lastname
		
class Relationship(Person):
	
	def __init__(self, firstname, lastname, age, gender, happiness, health, smarts, looks, relationship):
		super().__init__(firstname, lastname, age, gender, happiness, health, smarts, looks)
		self.relationship = relationship
		self.spent_time = False
		self.had_conversation = False
		self.was_complimented = False
				
	#TODO: add is_male() and is_female() methods
		
	def change_relationship(self, amount):
		self.relationship = clamp(self.relationship + amount, 0, 100)
		
	def get_gender_word(self, wordmale, wordfemale):
		return wordmale if self.gender == Gender.Male else wordfemale
		
	def his_her(self):
		return self.get_gender_word(_("his"), _("her"))
	
	def him_her(self):
		return self.get_gender_word(_("him"), _("her"))
	
	def get_type(self):
		return "Unknown Relation"
		
	def name_accusative(self):
		return _("relationship")
		
	def age_up(self):
		super().age_up()
		self.change_relationship(randint(-4, 4))
		self.spent_time = False
		self.had_conversation = False
		self.was_complimented = False
			
class Parent(Relationship):
	
	def __init__(self, lastname, age, gender):
		happiness = randint(40, 100)
		health = randint(30, 100)
		smarts = randint(0, 50) + randint(0, 50)
		looks = randint(0, 60) + randint(0, 40)
		super().__init__(random_name(gender), lastname, age, gender, happiness, health, smarts, looks, randint(90, 100))
		self.generosity = randint(0, 100)
		
	def name_accusative(self):
		return self.get_gender_word(_("father"), _("mother"))
		
	def get_type(self):
		return self.get_gender_word("Father", "Mother")
		
	def get_translated_type(self):
		return self.get_gender_word(_("Father"), _("Mother"))

class Sibling(Relationship):
	
	def __init__(self, lastname, age, gender, smarts, looks):
		happiness = randint(40, 80)
		health = randint(60, 100)
		super().__init__(random_name(gender), lastname, age, gender, happiness, health, smarts, looks, randint(35, 80))
		self.petulance = randint(0, 100)
		
	def name_accusative(self):
		return self.get_gender_word(_("brother"), _("sister")) + ", " + self.firstname
		
	def get_type(self):
		return self.get_gender_word("Brother", "Sister")
		
	def get_translated_type(self):
		return self.get_gender_word(_("Brother"), _("Sister"))

MALE_NAMES = open("assets/male_names.txt").read().splitlines()
FEMALE_NAMES = open("assets/female_names.txt").read().splitlines()
LAST_NAMES = open("assets/last_names.txt").read().splitlines()

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
		
class Player(Person):
	
	def __init__(self, first=None, last=None, gender=None):
		gender = gender or Gender.random()
		first = first or random_name(gender)
		last = last or random.choice(LAST_NAMES)
		happiness = randint(50, 100)
		health = randint(75, 100)
		smarts = randint(0, 50) + randint(0, 50)
		looks = randint(0, 65) + randint(0, 35)
		super().__init__(first, last, 0, gender, happiness, health, smarts, looks)
		last1 = last2 = last
		if randint(1, 100) <= 40:
			newlast = random.choice(LAST_NAMES)
			if random.randint(1, 3) == 1:
				last2 = newlast #Makes it more common to be named after the father's last name
			else:
				last1 = newlast
		self.parents = { #Cache these for performance since we only have one of each
			"Mother": Parent(last1, min(randint(randint(18, 20), 50) for _ in range(3)), Gender.Female),
			"Father": Parent(last2, min(randint(randint(18, 24), 60) for _ in range(3)), Gender.Male),
		}
		diff = self.parents["Father"].generosity - self.parents["Mother"].generosity
		if randint(1, 2) == 1:
			if diff > 0:
				self.parents["Mother"].generosity += randint(0, diff//2)
			elif diff < 0:
				self.parents["Mother"].generosity -= randint(0, abs(diff//2))
		else:
			diff = -diff
			if diff > 0:
				self.parents["Father"].generosity += randint(0, diff//2)
			elif diff < 0:
				self.parents["Father"].generosity -= randint(0, abs(diff//2))
		
		self.relations = [
			self.parents["Mother"],
			self.parents["Father"]
		]
		
		self.karma = randint(0, 25) + randint(0, 25) + randint(0, 25) + randint(0, 25)
		self.total_happiness = 0
		self.meditated = False
		self.worked_out = False
		self.money = 0
		self.depressed = False
		self.student_loan = 0
		self.chose_student_loan = False
		self.uv_years = 0
		self.reset_already_did()
		self.grades = None
		self.dropped_out = False
		self.teen_looks_inc = 0
	
	def change_grades(self, amount):
		if self.grades is not None:
			self.grades = clamp(self.grades + amount, 0, 100)
		
	def change_karma(self, amount):
		self.karma = clamp(self.karma + amount, 0, 100)
		
	def reset_already_did(self):
		self.meditated = False
		self.worked_out = False
		self.visited_library = False
		self.studied = False
		self.tried_to_drop_out = False
		
	def age_up(self):
		self.total_happiness += self.happiness
		super().age_up()
		self.reset_already_did()
		self.change_karma(randint(-2, 2))
		
		for relation in self.relations:
			relation.age_up()
			if isinstance(relation, Parent):
				if self.age < 18:
					relation.change_relationship(1)
				else:
					relation.change_relationship(random.choice((-1, -1, 0)))
		
		print(_("Age {age}").format(age=self.age))
		if self.death_check():
			self.die(_("You died of old age."))
			return
		if self.age == 13:	
			if randint(1, 4) == 1:
				val = randint(0, 1)
			else:
				val = min(randint(0, 12) for _ in range(4))
			self.teen_looks_inc = val
		if self.age >= 13 and self.age < randint(18, 24):
			self.change_looks(self.teen_looks_inc)
		if self.age > 50 and self.looks > randint(20, 25):
			decay = min((self.age - 51) // 5 + 1, 4)
			self.change_looks(-randint(0, decay))
		if self.happiness < 10 and not self.depressed:
			display_event(_("You are suffering from depression."))
			self.depressed = True
			self.change_happiness(-50)
			self.change_health(-randint(4, 8))
		for relation in self.relations[:]:
			if relation.death_check():
				rel_str = relation.name_accusative()
				display_event(_("Your {relative} died at the age of {age} due to old age.").format(relative=rel_str, age=relation.age))
				if isinstance(relation, Parent):
					del self.parents[relation.get_type()]
				self.relations.remove(relation)	
				self.change_happiness(-randint(40, 55))
		self.random_events()
		
	def calc_grades(self, offset):
		self.grades = clamp(round(10 * math.sqrt(self.smarts + offset)), 0, 100)
	
	def get_gender_str(self):
		return _("Male") if self.gender == Gender.Male else _("Female")
		
	def die(self, message):
		print(message)
		avg_happy = round(p.total_happiness / p.age)
		score = p.happiness * 0.3 + avg_happy * 0.7
		print_align_bars(
			(_("Lifetime Happiness"), avg_happy),
			(_("Karma"), p.karma)
		)
		exit()
	
	def display_stats(self):
		if self.happiness >= 60:
			if self.happiness >= 85:
				symbol = ":D"
			else:
				symbol = ":)"
		elif self.happiness < 40:
			if self.happiness < 15:
				symbol = ":'("
			else:
				symbol = ":("
		else:
			symbol = ":|"
		print_align_bars(
			(_("Happiness"), self.happiness, " " + symbol),
			(_("Health"), self.health),
			(_("Smarts"), self.smarts),
			(_("Looks"), self.looks),
			show_percent=True
		)
		
	def random_events(self):
		if self.uv_years > 0:
			self.uv_years -= 1
			if self.uv_years == 0:
				self.grades = None
				display_event(_("You graduated from university."))
				self.change_happiness(randint(14, 20))
				self.change_smarts(randint(10, 15))
				if self.chose_student_loan:
					self.student_loan = randint(20000, 40000)
					print(_("You now have to start paying back your student loan"))
			else:
				if self.grades < randint(10, 45):
					display_event(_("You were expelled from university after earning bad grades."))
					self.change_happiness(-randint(30, 50))
		if self.student_loan > 0:
			amount = min(randint(1000, 3000) for _ in range(3))
			amount = min(amount, self.student_loan)
			self.money -= amount
			self.student_loan -= amount
			if self.student_loan == 0:
				print(_("You've fully paid off your student loan"))
		if self.depressed:
			if self.happiness >= randint(20, 35):
				display_event(_("You are no longer suffering from depression"))
				self.change_happiness((100 - self.happiness)//2)
				self.change_health(randint(4, 8))
				self.depressed = False
			else:
				self.change_happiness(-randint(1, 2))
				self.change_health(-randint(1, 4))
		if self.age == 2 and randint(1, 2) == 1:
			print(_("Your mother is taking to to the doctor's office to get vaccinated."))
			print(_("How will you behave?"))
			choices = [
				_("Cooperate"),
				_("Throw a tantrum"),
				_("Bite her")
			]
			choice = choice_input(*choices)
			clear_screen()
			if choice == 1:
				print(_("You remained calm"))
			elif choice == 2:
				self.change_happiness(-randint(25, 35))
				self.parents["Mother"].change_relationship(-randint(6, 10))
				print(_("You threw a tantrum"))
			elif choice == 3:
				self.change_happiness(-randint(6, 10))
				self.parents["Mother"].change_relationship(-randint(25, 35))
				print(_("You bit your mother"))
		if self.grades is not None:
			self.change_grades(randint(-3, 3))
			base = round(10 * math.sqrt(self.smarts))
			if self.grades < base - 2:
				self.change_grades(randint(1, 3))
			elif self.grades > base + 2:
				self.change_grades(-randint(1, 3))
			grade_delta = (self.happiness - 50)/10
			if grade_delta > 0:
				grade_delta /= 2
			self.change_grades(round_stochastic(grade_delta))
		if self.age == 6:
			print(_("You are starting elementary school"))
			self.change_smarts(randint(1, 2))
			self.calc_grades(randint(4, 8))
		if self.age == 12:
			print(_("You are starting middle school"))
			self.change_smarts(randint(1, 3))
			self.calc_grades(randint(0, 8))
		if self.age == 14:
			print(_("You are starting high school"))
			self.change_smarts(randint(1, 4))
			self.calc_grades(randint(-8, 8))
		if self.age == 17 and not p.dropped_out:
			self.grades = None
			print(_("You graduated from high school."))
			self.change_happiness(randint(15, 20))
			self.change_smarts(randint(6, 10))
			print()
			self.display_stats()
			print()
			print(_("Would you like to apply to university?"))
			choice = choice_input(_("Yes"), _("No"))
			clear_screen()
			if choice == 1:
				if self.smarts >= random.randint(28, 44):
					print(_("Your application to university was accepted!"))
					self.change_happiness(randint(7, 9))
					SCHOLARSHIP = _("Scholarship")
					LOAN = _("Student Loan")
					PARENTS = _("Ask parents to pay")
					choices = [
						SCHOLARSHIP,
						LOAN,
						PARENTS
					]
					chosen = False
					while not chosen:
						print(_("How would you like to pay for your college tuition?"))
						choice = choice_input(*choices, return_text=True)
						clear_screen()
						if choice == SCHOLARSHIP:
							if self.smarts >= randint(randint(75, 85), 95):
								display_event(_("Your scholarship application has been awarded!"))
								self.change_happiness(randint(10, 15))
								chosen = True
							else:
								display_event(_("Your scholarship application was rejected."))
								self.change_happiness(-randint(7, 9))
								choices.remove(SCHOLARSHIP)
						elif choice == PARENTS:
							total = sum(p.generosity for p in self.parents.values())
							avg = total / len(self.parents)
							chance = (avg/100)**4
							if random.random() < chance:
								display_event(_("Your parents agreed to pay for your university tuition!"))
								self.change_happiness(randint(7, 9))
								chosen = True
							else:
								display_event(_("Your parents refused to pay for your university tuition."))
								self.change_happiness(-randint(7, 9))
								choices.remove(PARENTS)
						else:
							display_event(_("You took out a student loan to pay for your university tuition."))
							chosen = True
							self.chose_student_loan = True
					print(_("You are now enrolled in university."))
					self.uv_years = 4
					self.calc_grades(randint(-8, 10))
				else:
					display_event(_("Your application to university was rejected."))
					self.change_happiness(-randint(7, 9))

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
			extra = pair[2]
		else:
			extra = ""
		print((name + ": ").ljust(l + 2) + draw_bar(val, 100, 25) + (f" {val}%" if show_percent else "") + extra)

def draw_bar(val, max_val, width):
	num = round(width * val / max_val)
	return "[" + "|"*num + " "*(width-num) + "]"
	
def clear_screen():
	if platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

DEBUG = False

choice = choice_input(_("Random Life"), _("Custom Life"))
if choice == 1:
	p = Player()
else:
	first = ""
	last = ""
	while not first:
		first = input(_("Enter your first name: ")).strip()
	while not last:
		last = input(_("Enter your last name: ")).strip()
	print()
	print(_("Choose your gender:"))
	choice = choice_input(_("Male"), _("Female"))
	print()
	p = Player(first, last, Gender.Male if choice == 1 else Gender.Female)

clear_screen()
print(_("Your mother's name is {name}").format(name=p.parents["Mother"].name))
print(_("Your father's name is {name}").format(name=p.parents["Father"].name))

if randint(1, 5) < 5: #80% chance of having a sibling
	whichlast = random.choice((p.parents["Mother"].lastname, p.parents["Father"].lastname))
	theirsmarts = round_stochastic((randint(0, 100) + p.smarts)/2)
	theirlooks = round_stochastic((randint(0, 100) + p.looks)/2)
	sibling = Sibling(whichlast, randint(2, 12), Gender.random(), theirsmarts, theirlooks)
	p.relations.append(sibling)
	print(_("You have a {siblingtype} named {name}").format(siblingtype=sibling.get_translated_type().lower(), name=sibling.name))

while True:
	print()
	print(_("Your name") + f": {p.name}")
	print(_("Gender") + f": {p.get_gender_str()}")
	print(_("Money") + f": ${p.money:,}")
	p.display_stats()
	print()
	if p.alive == False:
		print(_("You died."))
		avg_happy = round(p.total_happiness / p.age)
		score = p.happiness * 0.3 + avg_happy * 0.7
		print_align_bars(
			(_("Lifetime Happiness"), avg_happy),
			(_("Karma"), p.karma)
		)
		exit()
	choices = [ _("Age +1"), _("Relationships"), _("Activities") ] 
	if p.grades is not None:
		choices.append(_("School"))
	if DEBUG:
		choices.append(_("Debug Menu"))
	choice = choice_input(*choices, return_text=True)
	clear_screen()
	if choice == _("Age +1"):
		print()
		p.age_up()
	if choice == _("Relationships"):
		relations = p.relations
		print(_("Relationships: "))
		for num, relation in enumerate(relations):
			print(f"{num+1}. {relation.name} ({relation.get_translated_type()})")
		back = _("Back")
		print(f"{len(relations)+1}. {back}")
		choice = int_input_range(1, len(relations)+1)
		clear_screen()
		if choice <= len(p.relations):
			relation = relations[choice - 1]
			print(_("Name") + ": " + relation.name + f" ({relation.get_translated_type()})")
			print(_("Age") + f": {relation.age}")
			bars = [
				(_("Relationship"), relation.relationship)
			]
			if isinstance(relation, Parent):
				bars.append((_("Generosity"), relation.generosity))
			elif isinstance(relation, Sibling):
				bars.append((_("Smarts"), relation.smarts))
				bars.append((_("Looks"), relation.looks))
				bars.append((_("Petulance"), relation.petulance))
			print_align_bars(*bars)
			choices = [ _("Back") ]
			if relation.age >= 5:
				if p.age >= 5:
					choices.append(_("Spend time"))
					choices.append(_("Have a conversation"))
				if p.age >= 6:
					choices.append(_("Compliment"))
					choices.append(_("Insult"))
			choice = choice_input(*choices, return_text=True)
			clear_screen()
			if choice == _("Spend time"):
				if relation.relationship < 15:
					print(_("Your {relation} refused to see you."))
					p.change_happiness(-4)
				else:
					print(_("You spent time with your {relation}.").format(relation=relation.name_accusative()))
					enjoyment1 = max(randint(0, 70), randint(0, 70)) + randint(0, 30)
					enjoyment2 = round(random.triangular(0, 100, relation.relationship))
					print_align_bars(
						(_("Your Enjoyment"), enjoyment1),
						(_("{his_her} Enjoyment").format(his_her=relation.his_her().capitalize()), enjoyment2)
					)
					if not relation.spent_time:
						p.change_happiness(round_stochastic(enjoyment1 / 12))
						relation.change_relationship(round_stochastic(enjoyment2 / 12))
						relation.spent_time = True
			elif choice == _("Have a conversation"):
				if relation.relationship < 25:
					display_event(_("Your {relation} isn't interested in having a conversation with you.").format(relation=relation.name_accusative()))
					p.change_happiness(-4)
				else:
					agreement = random.triangular(0, 100, 65)
					agreement += randint(0, max(0, (relation.relationship - 50)//3))
					if isinstance(relation, Sibling) and randint(1, 2) == 1:
						agreement -= randint(0, relation.petulance//3)
					#agreement = 0
					agreement = clamp(round(agreement), randint(0, 10), randint(90, 100))
					print(_("You had a conversation with your {relation}.").format(relation=relation.name_accusative()))
					display_bar(_("Agreement"), agreement)
					if not relation.had_conversation:
						p.change_happiness(4)
						relation.change_relationship(round_stochastic(agreement / 12))
						relation.had_conversation = True
					if agreement < 15:
						relation.change_relationship(-randint(2, 8))
						print(_("You and your {relation} got into an argument. What will you do?").format(relation=relation.name_accusative()))
						choice = choice_input(_("Apologize"), _("Agree to disagree"), _("Insult {him_her}").format(him_her=relation.him_her()))
						if choice == 1:
							p.change_karma(randint(1, 3))
							print(_("You apologized to your {relation}").format(relation=relation.name_accusative()))
							relation.change_relationship(randint(2, 4))
						elif choice == 2:
							print(_("You agreed to disagree"))
						elif choice == 3:
							p.change_karma(-randint(2, 6))
							print(_("You insulted your {relation}").format(relation=relation.name_accusative()))
							relation.change_relationship(-randint(4, 7))
			elif choice == _("Compliment"):
				appreciation = randint(0, 60) + randint(0, 40)
				diff = p.smarts - relation.smarts + 50
				if randint(1, 100) <= diff:
					appreciation = max(appreciation, randint(0, 60) + randint(0, 40))
				print(_("You complimented your {relation}.").format(relation=relation.name_accusative()))
				display_bar(_("{his_her} Appreciation").format(his_her=relation.his_her().capitalize()), appreciation)
				press_enter()
				if not relation.was_complimented:
					p.change_karma(randint(0, 2))
					relation.change_relationship(round_stochastic(appreciation / 6))
					if randint(1, 300) <= round_stochastic(appreciation * relation.relationship/50):
						display_event(_("Your {relation} complimented you back!").format(relation=relation.name_accusative()))
						p.change_happiness(randint(6, 10))
					relation.was_complimented = True
			elif choice == _("Insult"):
				rel = relation.name_accusative()
				if yes_no(_("Are you sure you want to insult your {relation}?").format(relation=rel)):
					display_event(_("You insulted your {rel}.").format(rel=rel))
					relation.change_relationship(-randint(4, 8))
					p.change_karma(-randint(2, 4))
					if isinstance(relation, Sibling):
						chance = 50 * (relation.petulance/100)**1.5
					else:
						chance = (100-relation.relationship)/4
					if random.uniform(0, 100) < chance:
						display_event(_("Your {rel} insulted you back.").format(rel=rel))
						p.change_happiness(-randint(1, 5) if isinstance(relation, Sibling) else -randint(3, 8))
			print()
	if choice == _("Activities"):
		print(_("Activities Menu"))
		print()
		choices = [ _("Back") ]
		if p.age >= 13:
			choices.append(_("Meditate"))
			choices.append(_("Library"))
		if p.age >= 18:
			choices.append(_("Gym"))
		choice = choice_input(*choices, return_text=True)
		clear_screen()
		if choice == _("Meditate"):
			print(_("You practiced meditation."))
			if not p.meditated: #You can only get the bonus once per year
				p.change_health(randint(2, 5))
				p.change_happiness(randint(3, 6))
				p.change_karma(randint(0, 3))
				if random.randint(1, 12) == 1:
					p.change_happiness(2)
					print(_("You have achieved a deeper awareness of yourself."))
					print(_("Karma") + ": " + draw_bar(p.karma, 100, 25))
				p.meditated = True
		elif choice == _("Library"):
			print(_("You went to the library."))
			if not p.visited_library: #You can only get the bonus once per year
				p.change_happiness(randint(0, 4))
				p.change_smarts(randint(2, 5))
				p.visited_library = True
		elif choice == _("Gym"):
			if p.health < 10:
				print(_("Your health is too weak to visit the gym."))
			else:
				workout = randint(25, 75)
				if p.health > 50:
					workout += randint(0, (p.health - 50)//2)
				else:
					workout -= randint(0, (50 - p.health)//2)
				lo = -25
				hi = 25
				if workout < 25:
					lo = -workout
				elif workout > 75:
					hi = 100 - workout
				workout += randint(lo, hi)
				print(_("You worked out at the gym."))
				print(_("Workout") + ": " + draw_bar(workout, 100, 25))
				if not p.worked_out:
					p.change_happiness(round(workout / 12) + randint(0, 1))
					p.change_health(round(workout / 14) + randint(1, 2))
					if p.looks < workout:
						p.change_looks(randint(1, 3) + randint(0, round(workout / 33)))
					p.worked_out = True
				print()
	if choice == _("School"):
		print(_("School Menu"))
		print()
		display_bar(_("Grades"), p.grades)
		choice = choice_input(_("Back"), _("Study harder"), _("Drop out"))
		clear_screen()
		if choice == 2:
			print(_("You began studying harder"))
			if not p.studied:
				p.change_grades(randint(5, 7 + (100 - p.grades)//5))
				p.change_smarts(randint(0, 2))
				p.studied = True
		if choice == 3:
			can_drop_out = p.smarts < randint(8, 12) + randint(0, 13)
			can_drop_out &= not p.tried_to_drop_out
			if p.age >= 18 or p.uv_years > 0 or (p.age >= randint(15, 16) and can_drop_out):
				p.dropped_out = True
				p.grades = None
				print(_("You dropped out of school."))
				if p.uv_years > 0:
					p.uv_years = 0
			else:
				p.tried_to_drop_out = True
				print(_("Your parents won't let you drop out of school."))
	if choice == _("Debug Menu"):
		choice = choice_input(_("Back"), _("Stats"), _("Identity"))
		if choice == 2:
			while True:
				clear_screen()
				print(_("Your stats"))
				display_data(_("Happiness"), p.happiness)
				display_data(_("Health"), p.health)
				display_data(_("Smarts"), p.smarts)
				display_data(_("Looks"), p.looks) 	
				display_data(_("Karma"), p.karma) 
				choice = choice_input(
					_("Back"),
					_("Modify Happiness"),
					_("Modify Health"),
					_("Modify Smarts"),
					_("Modify Looks"),
					_("Modify Karma")
				)
				if choice == 1:
					break
				elif choice == 2:
					print(_("What would you like to set Happiness to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						p.happiness = val
				elif choice == 3:
					print(_("What would you like to set Health to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						p.health = val
				elif choice == 4:
					print(_("What would you like to set Smarts to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						p.smarts = val
				elif choice == 5:
					print(_("What would you like to set Looks to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						p.looks = val
				elif choice == 6:
					print(_("What would you like to set Karma to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						p.karma = val
		elif choice == 3:
			while True:
				clear_screen()
				display_data(_("First name"), p.firstname)
				display_data(_("Last name"), p.lastname)
				display_data(_("Gender"), p.get_gender_str())
				choice = choice_input(
					_("Back"),
					_("Change first name"),
					_("Change last name"),
					_("Change gender")
				)
				if choice == 1:
					break
				elif choice == 2:
					name = input(_("Enter first name: ")).strip()
					if name:
						p.firstname = firstname
				elif choice == 3:
					name = input(_("Enter last name: ")).strip()
					if name:
						p.lastname = firstname
				elif choice == 4:
					if p.gender == Gender.Male:
						p.gender = Gender.Female
					else:
						p.gender = Gender.Male	
