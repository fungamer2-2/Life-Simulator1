import random
from random import randint

from src.people.classes.relationship import Relationship
from src.lifesim_lib.translation import _
from src.lifesim_lib.lifesim_lib import *


class Partner(Relationship):
    def __init__(self, age, gender, smarts, looks, relationship, status):
        happiness = randint(30, 100)
        health = randint(15, 60) + randint(randint(0, 40), 40)
        last = random_last_name()
        super().__init__(
            random_name(gender),
            last,
            age,
            gender,
            happiness,
            health,
            smarts,
            looks,
            relationship,
        )
        self.status = status
        self.willpower = randint(0, 60) + randint(0, 40)
        if randint(1, 2) == 1:
            self.willpower = max(self.willpower, randint(40, 100))
        self.craziness = randint(0, 100)
        self.fertility = 0
        if self.gender == Gender.Female:
            self.fertility = randint(25, 100)
        self.years_together = 0
        self.was_proposed_to = False
        self.is_pregnant = False
        P_CONST = math.log(5, 4)  # Generate net worth using Pareto distribution
        net_worth = round_stochastic(13000 / ((1 - random.random()) ** (1 / P_CONST)))
        if randint(1, 100) <= 40:
            net_worth -= randint(0, 60000)
        self.net_worth = net_worth

    def age_up(self):
        super().age_up()
        self.years_together += 1
        self.was_proposed_to = False

    def print_info(self):
        display_data(_("Their Age"), self.age)
        print_align_bars(
            (_("Their Smarts"), self.smarts),
            (_("Their Looks"), self.looks),
            (_("Their Craziness"), self.craziness),
        )

    def compatibility_check(self, other):
        if randint(1, 6) == 1:
            k = other.karma if isinstance(other, Player) else 50
            return randint(1, 100) <= k
        c1 = other.looks - self.looks + 50
        c2 = other.smarts - self.smarts + 50
        return randint(1, 50) + randint(0, 50) <= round_stochastic(c1 + (c2 - c1) / 3)

    def get_translated_type(self):
        types = [
            (_("Boyfriend"), _("Girlfriend")),
            (_("Fiancé"), _("Fiancée")),
            (_("Husband"), _("Wife")),
        ]
        return self.get_gender_word(*types[self.status])

    def name_accusative(self):
        return self.get_translated_type().lower() + ", " + self.firstname


from src.people.classes.player import Player
