from random import randint

from src.lifesim_lib.lifesim_lib import random_name
from src.lifesim_lib.translation import _
from src.people.classes.relationship import Relationship

class Parent(Relationship):
	"""Base class for relationships."""

	def __init__(self, lastname, age, gender):
		happiness = randint(40, 100)
		health = randint(30, 100)
		smarts = randint(0, 50) + randint(0, 50)
		looks = randint(0, 60) + randint(0, 40)
		super().__init__(
			random_name(gender),
			lastname,
			age,
			gender,
			happiness,
			health,
			smarts,
			looks,
			randint(90, 100),
		)
		self.generosity = randint(0, 100)

	def name_accusative(self):
		return self.get_gender_word(_("father"), _("mother"))

	def get_type(self):
		return self.get_gender_word("Father", "Mother")

	def get_translated_type(self):
		return self.get_gender_word(_("Father"), _("Mother"))