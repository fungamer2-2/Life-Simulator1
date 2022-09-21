import random
from random import randint
from enum import Enum

def clamp(val, lo, hi):
	return max(lo, min(val, hi))

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
			continue
		if lo <= val <= hi:
			return val
			
def choice_input(*options):
	for i in range(len(options)):
		print(f"{i+1}. {options[i]}")
	return int_input_range(1, len(options))	
		
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
		
	#TODO: add is_male() and is_female() methods
		
	def change_relationship(self, amount):
		self.relationship = clamp(self.relationship + amount, 0, 100)
	
	def get_type(self):
		return "Unknown Relation"
		
	def name_accusative(self):
		return "relationship"
		
	def age_up(self):
		super().age_up()
		self.change_relationship(randint(-4, 4))
			
class Parent(Relationship):
	
	def __init__(self, lastname, age, gender):
		happiness = randint(40, 100)
		health = randint(30, 100)
		smarts = randint(0, 50) + randint(0, 50)
		looks = randint(0, 60) + randint(0, 40)
		super().__init__(random_name(gender), lastname, age, gender, happiness, health, smarts, looks, randint(90, 100))
	
	def name_accusative(self):
		return "mother" if self.gender == Gender.Female else "father"
	
	def get_type(self):
		return "Mother" if self.gender == Gender.Female else "Father"

MALE_NAMES = open("male_names.txt").read().splitlines()
FEMALE_NAMES = open("female_names.txt").read().splitlines()
LAST_NAMES = open("last_names.txt").read().splitlines()

def random_name(gender):
	if gender == Gender.Male:
		return random.choice(MALE_NAMES)
	else:
		return random.choice(FEMALE_NAMES)
		
class Player(Person):
	
	def __init__(self):
		gender = Gender.random()
		first = random_name(gender)
		last = random.choice(LAST_NAMES)
		happiness = randint(50, 100)
		health = randint(75, 100)
		smarts = randint(0, 50) + randint(0, 50)
		looks = randint(0, 65) + randint(0, 35)
		super().__init__(first, last, 0, gender, happiness, health, smarts, looks)
		last1 = last2 = last
		if randint(1, 100) <= 40:
			newlast = random.choice(LAST_NAMES)
			if random.randint(1, 2) == 1:
				last1 = newlast
			else:
				last2 = newlast
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
		
	@property
	def relations(self):
		return list(self.parents.values())
		
	def change_karma(self, amount):
		self.karma = clamp(self.karma + amount, 0, 100)
		
	def age_up(self):
		self.total_happiness += self.happiness
		super().age_up()
		
		self.meditated = False
		self.worked_out = False
		
		self.change_karma(randint(-2, 2))
		for parent in self.parents.values():
			parent.age_up()
			if self.age < 18:
				parent.change_relationship(1)
			else:
				parent.change_relationship(-randint(0, 1))
		print(f"Age {self.age}")
		if self.age > randint(111, 121) or (self.age > randint(85, 100) and randint(1, 2) == 1):
			self.alive = False
			return
		if self.age > 50 and self.looks > randint(20, 25):
			decay = min((self.age - 51) // 5 + 1, 4)
			self.change_looks(-randint(0, decay))
		if self.happiness < 10 and not self.depressed:
			print("You are suffering from depression.")
			self.depressed = True
			self.change_happiness(-50)
			self.change_health(-randint(4, 8))
		for parent in list(self.parents.values()):
			if parent.age >= randint(110, 120) or (randint(1, 100) <= 50 and parent.age >= max((randint(72, 90) + randint(0, parent.health//4)) for _ in range(2))):
				rel_str = parent.name_accusative()
				print(f"Your {rel_str} died at the age of {parent.age}")
				print("Press enter to continue")
				input()
				del self.parents[parent.get_type()]
				self.change_happiness(-randint(40, 55))
		self.random_events()
		
	def random_events(self):
		if self.depressed:
			if self.happiness >= randint(20, 35):
				print("You are no longer suffering from depression")
				self.change_happiness((100 - self.happiness)//2)
				self.depressed = False
			else:
				self.change_happiness(-randint(1, 2))
				self.change_health(-randint(1, 4))
		if self.age == 2 and randint(1, 2) == 1:
			print("Your mother is taking to to the doctor's office to get vaccinated.")
			print("How will you behave?")
			choices = [
				"Cooperate",
				"Throw a " + ("conniption fit" if randint(1, 4) == 1 else "tantrum"),
				"Bite her"
			]
			choice = choice_input(*choices)
			if choice == 1:
				print("You remained calm")
			elif choice == 2:
				self.change_happiness(-randint(25, 35))
				self.parents["Mother"].change_relationship(-randint(6, 10))
				print("You threw a tantrum")
			elif choice == 3:
				self.change_happiness(-randint(6, 10))
				self.parents["Mother"].change_relationship(-randint(25, 35))
				print("You bit your mother")
		if self.age == 6:
			print("You are starting elementary school")
			self.change_smarts(randint(1, 2))
		if self.age == 12:
			print("You are starting middle school")
			self.change_smarts(randint(1, 3))
		if self.age == 14:
			print("You are starting high school")
			self.change_smarts(randint(1, 4))
		if self.age == 17:
			print("You graduated from high school.")
			self.change_happiness(randint(15, 20))
			self.change_smarts(randint(6, 10))
			print("Would you like to apply to university?")
			choice = choice_input("Yes", "No")
			if choice == 1:
				if self.smarts >= random.randint(28, 44):
					print("Your application to university was accepted!")
					self.change_happiness(randint(7, 9))
				else:
					print("Your application to university was rejected.")
					self.change_happiness(-randint(7, 9))
			
def draw_bar(val, max_val, width):
	num = round(width * val / max_val)
	return "[" + "|"*num + " "*(width-num) + "]"
		
p = Player()
print(f"Your name: {p.name}")
print(f"Gender: {'Male' if p.gender == Gender.Male else 'Female'}")
while True:
	print(f"Happiness: {draw_bar(p.happiness, 100, 25)} {p.happiness}%")
	print(f"Health:    {draw_bar(p.health, 100, 25)} {p.health}%")
	print(f"Smarts:    {draw_bar(p.smarts, 100, 25)} {p.smarts}%")
	print(f"Looks:     {draw_bar(p.looks, 100, 25)} {p.looks}%")
	print()
	if p.alive == False:
		print("You died.")
		avg_happy = round(p.total_happiness / p.age)
		score = p.happiness * 0.3 + avg_happy * 0.7
		print(f"Lifetime Happiness: {draw_bar(score, 100, 25)}")
		print(f"Karma:              {draw_bar(p.karma, 100, 25)}")
		exit()
	choice = choice_input("Age", "Relationships", "Activities")
	if choice == 1:
		print()
		p.age_up()
	if choice == 2:
		relations = p.relations
		print("Relationships: ")
		for num, relation in enumerate(relations):
			print(f"{num+1}. {relation.name} ({relation.get_type()})")
		print(f"{len(relations)+1}. Back")
		choice = int_input_range(1, len(relations)+1)
		if choice <= len(p.relations):
			relation = relations[choice - 1]
			print(f"Name: {relation.name}")
			print(f"Age: {relation.age}")
			print(f"Relation: {relation.get_type()}")
			print(f"Relationship: {draw_bar(relation.relationship, 100, 25)}")
			print()
	if choice == 3:
		choices = [ "Back" ]
		if p.age >= 13:
			choices.append("Meditate")
		if p.age >= 18:
			choices.append("Gym")
		choice = choices[choice_input(*choices) - 1]
		if choice == "Meditate":
			print("You practiced meditation.")
			if not p.meditated:
				p.change_health(randint(2, 5))
				p.change_happiness(randint(3, 6))
				p.change_karma(randint(0, 3))
				if random.randint(1, 12) == 1:
					p.change_happiness(2)
					print("You have achieved a deeper awareness of yourself.")
					print("Karma: " + draw_bar(p.karma, 100, 25))
				p.meditated = True
		elif choice == "Gym":
			if p.health < 10:
				print("Your health is too weak to visit the gym.")
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
				print("You worked out at the gym.")
				print("Workout: " + draw_bar(workout, 100, 25))
				if not p.worked_out:
					p.change_happiness(round(workout / 8) + randint(0, 2))
					p.change_health(round(workout / 12) + randint(1, 3))
					if p.looks < workout:
						p.change_looks(randint(1, 3) + randint(0, round(workout / 33)))
					p.worked_out = True
				print()
