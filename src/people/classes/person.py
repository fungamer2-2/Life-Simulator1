from random import randint

from src.lifesim_lib.lifesim_lib import *


class Person:
    """Base class for any character in the game."""

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
        self.teen_looks_inc = 0
        self.update_name()

    def update_name(self):
        self.name = self.firstname + " " + self.lastname

    def age_up(self):
        self.age += 1
        self.change_happiness(randint(-3, 3))
        self.change_health(randint(-3, 3))
        self.change_smarts(randint(-3, 3))
        self.change_looks(randint(-3, 3))
        if self.age == 13:
            self.gen_teen_looks_inc()
        if self.age >= 13 and self.age < randint(24, 27):
            self.change_looks(self.teen_looks_inc)
        if self.age > 50 and self.looks > randint(20, 25) and randint(1, 4) < 4:
            decay = min((self.age - 51) // 5 + 1, 4)
            self.change_looks(-randint(0, decay))

    def gen_teen_looks_inc(self):
        val = 0
        if randint(1, 4) == 1:
            val = randint(0, 1)
        else:
            val = min(randint(0, 12) for _ in range(4))
        self.teen_looks_inc = val

    def generate_partner(self):
        from src.people.classes.partner import Partner

        m = self.age // 6
        age = 0
        while age < 18:
            age = self.age + randint(-m, m)
        gender = Gender.Female if self.gender == Gender.Male else Gender.Male
        p = Partner(
            age,
            gender,
            randint(0, 50) + randint(0, 50),
            randint(0, 50) + randint(0, 50),
            50,
            0,
        )
        while p.death_check():
            p.age -= randint(1, 5)
        return p

    def death_check(self):
        k1 = self.karma if self.__class__.__name__ == "Player" else 50
        h = self.happiness + int((self.health - self.happiness) / 3)
        return (self.age >= randint(98, 122) and randint(1, 100) <= 65) or (
            self.age > randint(70 + h // 11, 90 + h // 3) + int((k1 - 50) / 5)
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
