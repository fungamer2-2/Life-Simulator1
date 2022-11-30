from random import randint

from src.lifesim_lib.lifesim_lib import *
from src.people.classes.relationship import Relationship
from src.lifesim_lib.translation import _


class Child(Relationship):
    """Class that represents any children the player has"""

    def __init__(
        self,
        first,
        last,
        gender,
        smarts,
        looks,
        mother=None,
        father=None,
        adopted=False,
    ):
        super().__init__(
            first,
            last,
            0,
            gender,
            randint(50, 100),
            randint(80, 100),
            smarts,
            looks,
            randint(60, 100),
        )
        self.mother = mother
        self.father = father
        self.total_happiness = 0
        self.salary = 0
        self.money = 0
        self.is_in_uv = 0
        self.student_loan = 0
        self.student_loan_total = 0
        self.has_student_loan = False
        self.years_worked = 0
        self.partner = None
        self.partner_desire = randint(0, 100)
        self.may_divorce = False
        self.adopted = adopted
        self.player = None
        
    def set_parent(self, player):
    	if player.gender == Gender.Male:
    		self.father = player
    	else:
    		self.mother = player

    def name_accusative(self):
        if self.adopted:
            typ = self.get_gender_word(_("adopted son"), _("adopted daughter"))
        else:
            typ = self.get_gender_word(_("son"), _("daughter"))
        return typ + ", " + self.firstname

    def get_translated_type(self):
        if self.adopted:
            return self.get_gender_word(_("Adopted Son"), _("Adopted Daughter"))
        else:
            return self.get_gender_word(_("Son"), _("Daughter"))

    def age_up(self):
        self.total_happiness += self.happiness
        super().age_up()
        if randint(1, 2) == 1:
            if self.happiness < randint(46, 50):
                self.change_happiness(randint(0, 4))
            elif self.happiness > randint(50, 54):
                self.change_happiness(-randint(0, 3))
        if self.is_in_uv > 0:
            self.is_in_uv -= 1
            if self.is_in_uv == 0:
                print(
                    _("Your {child} graduated from university.").format(
                        child=self.name_accusative()
                    )
                )
                self.change_smarts(randint(6, 12))
                self.change_happiness(randint(8, 14))
        if self.age == 6:
            print(
                _("Your {child} is starting elementary school").format(
                    child=self.name_accusative()
                )
            )
            self.change_smarts(randint(0, 2))
        if self.age == 12:
            print(
                _("Your {child} is starting middle school").format(
                    child=self.name_accusative()
                )
            )
            self.change_smarts(randint(0, 3))
        if self.age == 14:
            print(
                _("Your {child} is starting high school").format(
                    child=self.name_accusative()
                )
            )
            self.change_smarts(randint(0, 4))
        if self.age == 17:
            print(
                _("Your {child} graduated from high school").format(
                    child=self.name_accusative()
                )
            )
            self.change_smarts(randint(5, 10))
            self.change_happiness(randint(5, 10))
            if self.smarts >= randint(35, 45) and randint(1, 4) < 4:
                print(
                    _("Your {child} started going to university.").format(
                        child=self.name_accusative()
                    )
                )
                self.is_in_uv = 4
        if self.salary > 0:
            self.years_worked += 1
            tax = calculate_tax(self.salary)
            income = self.salary - tax
            income *= random.uniform(0.4, 0.8)
            self.money += round_stochastic(self.salary)
        can_get_job = self.salary == 0 and self.age >= 18 and self.is_in_uv == 0
        if can_get_job and randint(1, 3) == 1:
            attempts = randint(2, 7)
            for i in range(attempts):
                salary = round_stochastic(randexpo(30000, 65000))
                if self.salary < randint(30000, 40000) and randint(1, 3) < 3:
                    continue
                m = 100 + round_stochastic((salary - 40000) / 300)
                mod = 50 - self.smarts
                roll = randint(1, m)
                if mod > 0:
                    roll += randint(0, mod)
                elif mod < 0:
                    roll -= randint(0, abs(mod))
                if roll <= 100:
                    self.years_worked = 0
                    self.salary = salary
                    break
        if self.partner:
            self.partner.age_up()
            if self.partner.death_check():
                self.partner = None
            else:
                breakup_chance = 45 if self.partner.status == 2 else 15
                if (self.may_divorce or self.partner.status != 2) and randint(
                    1, breakup_chance
                ) == 1:
                    self.change_happiness(-randint(5, 20))
                    if self.partner.status == 2:
                        print(
                            _("Your {child}, and {partner} divorced.").format(
                                child=self.name_accusative(), partner=self.partner.name
                            )
                        )
                        if self.partner_desire > (cap := randint(5, 12)):
                            self.partner_desire -= randint(3, 10)
                            if self.partner_desire < cap:
                                self.partner_desire = cap
                    else:
                        print(
                            _("Your {child}, and {partner} broke up.").format(
                                child=self.name_accusative(), partner=self.partner.name
                            )
                        )
                        if self.partner_desire > (cap := randint(10, 15)):
                            self.partner_desire -= randint(1, 6)
                            if self.partner_desire < cap:
                                self.partner_desire = cap
                    self.partner = None
                elif (
                    self.partner.status < 2
                    and self.partner.years_together >= randint(3, 7)
                    and one_in(5)
                ):
                    print(
                        _("Your {child} is now married to {partner}.").format(
                            child=self.name_accusative(), partner=self.partner.name
                        )
                    )
                    self.partner.change_relationship(randint(10, 45))
                    self.partner.status = 2
                    self.may_divorce = one_in(2)
        else:
            if self.age >= 18 and randint(1, 700) <= self.partner_desire:
                attempts = min(
                    randint(9, 11), round_stochastic(self.partner_desire / 8)
                )
                for i in range(attempts):
                    p = self.generate_partner()
                    if p.compatibility_check(self):
                        self.partner = p
                        self.change_happiness(randint(5, 20))
                        print(
                            _(
                                "Your {child} is now in a relationship with {partner}, age {age}."
                            ).format(
                                child=self.name_accusative(), partner=p.name, age=p.age
                            )
                        )
                        break
