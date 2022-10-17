from random import randint

from src.lifesim_lib.lifesim_lib import clamp, Gender
from src.people.classes.person import Person

_ = lambda s: s


class Relationship(Person):
    """Base class for relationships."""

    def __init__(
        self,
        firstname,
        lastname,
        age,
        gender,
        happiness,
        health,
        smarts,
        looks,
        relationship,
    ):
        super().__init__(
            firstname, lastname, age, gender, happiness, health, smarts, looks
        )
        self.relationship = relationship
        self.spent_time = False
        self.had_conversation = False
        self.was_complimented = False

    # TODO: add is_male() and is_female() methods

    def change_relationship(self, amount):
        self.relationship = clamp(self.relationship + amount, 0, 100)

    def get_gender_word(self, wordmale, wordfemale):
        return wordmale if self.gender == Gender.Male else wordfemale

    def his_her(self):
        return self.get_gender_word(_("his"), _("her"))

    def him_her(self):
        return self.get_gender_word(_("him"), _("her"))

    def hes_shes(self):
        return self.get_gender_word(_("he's"), _("she's"))

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
