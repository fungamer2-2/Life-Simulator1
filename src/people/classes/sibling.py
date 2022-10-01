from random import randint

from src.lifesim_lib.lifesim_lib import random_name
from src.people.classes.relationship import Relationship

_ = lambda s: s


class Sibling(Relationship):
    """Base class for siblings."""

    def __init__(self, lastname, age, gender, smarts, looks):
        happiness = randint(40, 80)
        health = randint(60, 100)
        super().__init__(
            random_name(gender),
            lastname,
            age,
            gender,
            happiness,
            health,
            smarts,
            looks,
            randint(35, 80),
        )
        self.petulance = randint(0, 100)

    def name_accusative(self):
        return self.get_gender_word(_("brother"), _("sister")) + ", " + self.firstname

    def get_type(self):
        return self.get_gender_word("Brother", "Sister")

    def get_translated_type(self):
        return self.get_gender_word(_("Brother"), _("Sister"))
