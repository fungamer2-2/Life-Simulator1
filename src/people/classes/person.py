from random import randint

from src.lifesim_lib.lifesim_lib import clamp


class Person:
    """Base class for persons."""

    def __init__(
        self, firstname, lastname, age, gender, happiness, health, smarts, looks
    ):
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
        return self.age > randint(98, 122) or (
            self.age > randint(80 + self.health // 12, 90 + self.health // 3)
            and randint(1, 100) <= 65
        )

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
