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
        self.money = randint(0, 50) + randint(0, 50)
        self.asked_for_money = 0  # Increases by 1 after the player asks for money. The player will be given money if this value == 0. If this value >= 3, they will tell the player "to stop asking for money"
        self.ask_money_cd = 0  # This value is set to 3 when the parent gives the player money and is decremented every year. Once this value reaches 0, asked_for_money is reset to 0

    def age_up(self):
        super().age_up()
        if self.ask_money_cd > 0:
            self.ask_money_cd -= 1
            if self.ask_money_cd == 0:
                self.asked_for_money = 0

    def name_accusative(self):
        return self.get_gender_word(_("father"), _("mother"))

    def get_type(self):
        return self.get_gender_word("Father", "Mother")

    def get_translated_type(self):
        return self.get_gender_word(_("Father"), _("Mother"))
