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
			
def choice_input(*options, return_text=False):
	for i in range(len(options)):
		print(f"{i+1}. {options[i]}")
	val = int_input_range(1, len(options))	
	if return_text:
		return options[val - 1]
	
	return val

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
		
	#TODO: add is_male() and is_female() methods
		
	def change_relationship(self, amount):
		self.relationship = clamp(self.relationship + amount, 0, 100)
		
	def get_gender_word(self, wordmale, wordfemale):
		return wordmale if self.gender == Gender.Male else wordfemale
	
	def his_her(self):
		return self.get_gender_word("his", "her")
	
	def get_type(self):
		return "Unknown Relation"
		
	def name_accusative(self):
		return _("relationship")
		
	def age_up(self):
		super().age_up()
		self.change_relationship(randint(-4, 4))
		self.spent_time = False
		self.had_conversation = False
			
class Parent(Relationship):
	
	def __init__(self, lastname, age, gender):
		happiness = randint(40, 100)
		health = randint(30, 100)
		smarts = randint(0, 50) + randint(0, 50)
		looks = randint(0, 60) + randint(0, 40)
		super().__init__(random_name(gender), lastname, age, gender, happiness, health, smarts, looks, randint(90, 100))
		
	def name_accusative(self):
		return self.get_gender_word(_("father"), _("mother"))
		
	def get_type(self):
		return self.get_gender_word("Father", "Mother")
		
	def get_translated_type(self):
		return self.get_gender_word(_("Father"), _("Mother"))
		
MALE_NAMES = open("assets/male_names.txt").read().splitlines()
FEMALE_NAMES = open("assets/female_names.txt").read().splitlines()
LAST_NAMES = open("assets/last_names.txt").read().splitlines()

def random_name(gender):
	if gender == Gender.Male:
		return random.choice(MALE_NAMES)
	else:
		return random.choice(FEMALE_NAMES)

def display_event(message):
	print(message)
	input(_("Press Enter to continue..."))
	clearScreen()	
		
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
		self.parents = {
			"Mother": Parent(last1, min(randint(18, 50) for _ in range(3)), Gender.Female),
			"Father": Parent(last2, min(randint(18, 65) for _ in range(3)), Gender.Male),
		}
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
		
	@property
	def relations(self):
		return list(self.parents.values())
		
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
		for parent in self.parents.values():
			parent.age_up()
			if self.age < 18:
				parent.change_relationship(1)
			else:
				parent.change_relationship(random.choice((-1, -1, 0)))
		print(_("Age {age}").format(age=self.age))
		if self.age > randint(112, 123) or (self.age > randint(80 + self.health // 10, 90 + self.health//3) and randint(1, 100) <= 65):
			self.alive = False
			return
		if self.age > 50 and self.looks > randint(20, 25):
			decay = min((self.age - 51) // 5 + 1, 4)
			self.change_looks(-randint(0, decay))
		if self.happiness < 10 and not self.depressed:
			display_event(_("You are suffering from depression."))
			self.depressed = True
			self.change_happiness(-50)
			self.change_health(-randint(4, 8))
		for parent in list(self.parents.values()):
			if parent.age >= randint(110, 120) or (randint(1, 100) <= 50 and parent.age >= max((randint(72, 90) + randint(0, parent.health//4)) for _ in range(2))):
				rel_str = parent.name_accusative()
				display_event(_("Your {relative} died at the age of {age}").format(relative=rel_str, age=self.age))
				del self.parents[parent.get_type()]
				self.change_happiness(-randint(40, 55))
		self.random_events()
		
	def calc_grades(self, offset):
		self.grades = clamp(round(10 * math.sqrt(self.smarts + offset)), 0, 100)
	
	def display_stats(self):
		print_align_bars(
			(_("Happiness"), self.happiness),
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
			clearScreen()
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
			clearScreen()
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
						clearScreen()
						if choice == SCHOLARSHIP:
							if self.smarts >= randint(randint(75, 85), 95):
								display_event(_("Your scholarship application has been awarded!"))
								self.change_happiness(randint(10, 15))
								chosen = True
							else:
								display_event(_("Your scholarship application was rejected."))
								self.change_happiness(-randint(7, 9))
								choices.remove(SCHOLARSHIP)
						elif choice == LOAN:
							if randint(1, 6) == 1:
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
					self.calc_grades(randint(-4, 10))
				else:
					display_event(_("Your application to university was rejected."))
					self.change_happiness(-randint(7, 9))

def display_bar(stat_name, val):
	print(stat_name + ": " + val)
	
def print_align_bars(*name_pairs, show_percent=False):
	l = 0
	for name, val in name_pairs:
		if len(name) > l:
			l = len(name)
	for name, val in name_pairs:
		print((name + ": ").ljust(l + 2) + draw_bar(val, 100, 25) + (f" {val}%" if show_percent else ""))

def draw_bar(val, max_val, width):
	num = round(width * val / max_val)
	return "[" + "|"*num + " "*(width-num) + "]"
	
def clearScreen():
	if platform == "linux" or platform == "linux2":
		os.system('clear')
	elif platform == "darwin":
		os.system('clear')
	elif platform == "win32":
		os.system('cls')

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
	choice = choice_input("Male", "Female")
	print()
	p = Player(first, last, Gender.Male if choice == 1 else Gender.Female)
print(f"Your name: {p.name}")
gender = _("Male") if p.gender == Gender.Male else _("Female")
print(_("Gender") + f": {gender}")
while True:
	print()
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
	choice = choice_input(*choices, return_text=True)
	clearScreen()
	if choice == _("Age +1"):
		print()
		p.age_up()
	if choice == _("Relationships"):
		relations = p.relations
		print(_("Relationships: "))
		for num, relation in enumerate(relations):
			print(f"{num+1}. {relation.name} ({relation.get_translated_type()})")
		back = pgettext("to main menu", "Back")
		print(f"{len(relations)+1}. {back}")
		choice = int_input_range(1, len(relations)+1)
		clearScreen()
		if choice <= len(p.relations):
			relation = relations[choice - 1]
			print(_("Name") + ": " + relation.name + f"({relation.get_translated_type()})")
			print(_("Age") + f": {relation.age}")
			display_bar(_("Relationship"), relation.relationship)
			choices = [ _("Back") ]
			if p.age >= 4:
				choices.append(_("Spend time"))
				choices.append(_("Have a conversation"))
			choice = choice_input(*choices, return_text=True)
			clearScreen()
			if choice == _("Spend time"):
				print(_("You spent time with your {relation}.").format(relation.name_accusative()))
				enjoyment1 = max(randint(0, 70), randint(0, 70)) + randint(0, 30)
				enjoyment2 = round(random.triangular(0, 100, relation.relationship))
				print_align_bars(
					(_("Your Enjoyment"), enjoyment1),
					(_("{his_her} Enjoyment").format(his_her=relation.his_her().capitalize()), enjoyment2)
				)
				#print(_("Your Enjoyment") + ": " + draw_bar(enjoyment1, 100, 25))
#				print(_(f"{relation.his_her().capitalize()} Enjoyment:  {draw_bar(enjoyment2, 100, 25)}"))
				if not relation.spent_time:
					p.change_happiness(enjoyment1 // 12 + randint(0, 1))
					relation.change_relationship(enjoyment2 // 12 + randint(0, 1))
					relation.spent_time = True
			elif choice == _("Have a conversation"):
				if relation.relationship < 24:
					display_event(_("Your {relation} isn't interested in having a conversation with you.").format(relation=relation.name_accusative()))
					p.change_happiness(-4)
				else:
					agreement = random.triangular(0, 100, 65)
					agreement += randint(0, max(0, (relation.relationship - 50)//3))
					agreement = min(round(agreement), randint(90, 100))
					print(_("You had a conversation with your {relation}.").format(relation.name_accusative()))
					display_event(_("Agreement") + ": " + draw_bar(agreement, 100, 25))
					if not relation.had_conversation:
						p.change_happiness(4)
						relation.change_relationship(agreement // 16)
						relation.had_conversation = True
			print()
	if choice == _("Activities"):
		choices = [ _("Back") ]
		if p.age >= 13:
			choices.append(_("Meditate"))
			choices.append(_("Library"))
		if p.age >= 18:
			choices.append(_("Gym"))
		choice = choice_input(*choices, return_text=True)
		clearScreen()
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
					p.change_happiness(round(workout / 8) + randint(0, 1))
					p.change_health(round(workout / 12) + randint(1, 2))
					if p.looks < workout:
						p.change_looks(randint(1, 3) + randint(0, round(workout / 33)))
					p.worked_out = True
				print()
	if choice == _("School"):
		display_bar(_("Grades"), p.grades)
		choice = choice_input(_("Back"), _("Study harder"), _("Drop out"))
		clearScreen()
		if choice == 2:
			print(_("You began studying harder"))
			if not p.studied:
				p.change_grades(randint(2, 3 + (100 - p.grades)//5))
				p.change_smarts(randint(0, 2))
				p.studied = True
		if choice == 3:
			can_drop_out = p.smarts < randint(8, 12) + randint(0, 13)
			can_drop_out &= not p.tried_to_drop_out
			if p.age >= 18 or (p.age >= randint(15, 16) and can_drop_out):
				p.dropped_out = True
				p.grades = None
				print(_("You dropped out of school."))
				if p.uv_years > 0:
					p.uv_years = 0
			else:
				p.tried_to_drop_out = True
				print(_("Your parents won't let you drop out of school."))