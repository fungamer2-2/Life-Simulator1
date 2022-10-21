from random import randint

from src.people.classes.relationship import Relationship
from src.lifesim_lib.translation import _
from src.lifesim_lib.lifesim_lib import random_name, random_last_name

class Partner(Relationship):
	
	def __init__(self, age, gender, smarts, looks, relationship, status):
		happiness = randint(30, 100)
		health = randint(15, 60) + randint(randint(0, 40), 40)
		last = random_last_name(gender)
		super().__init__(random_name(gender), random_last_name(gender), age, gender, happiness, health, smarts, looks, relationship)
		self.status = status
		
	def get_translated_type(self):
		types = [
			(_("Boyfriend"), _("Girlfriend")),
			(_("Fiancé"), _("Fiancée")),
			(_("Husband"), _("Wife")),
		]
		return self.get_gender_word(*types[self.status])

		