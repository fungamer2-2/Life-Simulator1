from random import randint

from src.lifesim_lib.lifesim_lib import clamp, Gender
from src.people.classes.person import Person
from src.lifesim_lib.translation import _

class Child(Person):
	"""Class that represents any children the player has"""
	
	def __init__(self, first, last, gender, smarts, looks, mother=None, father=None):
		super().__init__(first, last, 0, gender, randint(50, 100), randint(80, 100), smarts, looks, randint(60, 100))
		self.mother = mother
		self.father = father