import math
from random import choice, randint

from src.lifesim_lib.const import CONST
from src.lifesim_lib.lifesim_lib import (
    choice_input,
    clamp,
    clear_screen,
    display_event,
    Gender,
    print_align_bars,
    random_name,
    round_stochastic,
)
from .parent import Parent
from .person import Person

_ = lambda s: s


class Player(Person):
    def __init__(self, first=None, last=None, gender=None):

        gender = gender or Gender.random()
        first = first or random_name(gender)
        last = last or choice(CONST.LAST_NAMES)
        happiness = randint(50, 100)
        health = randint(75, 100)
        smarts = randint(0, 50) + randint(0, 50)
        looks = randint(0, 65) + randint(0, 35)
        super().__init__(first, last, 0, gender, happiness, health, smarts, looks)
        last1 = last2 = last
        if randint(1, 100) <= 40:
            newlast = choice(CONST.LAST_NAMES)
            if randint(1, 3) == 1:
                last2 = newlast  # Makes it more common to be named after the father's last name
            else:
                last1 = newlast
        self.parents = {
            "Mother": Parent(
                last1, min(randint(18, 50) for _ in range(3)), Gender.Female
            ),
            "Father": Parent(
                last2, min(randint(18, 60) for _ in range(3)), Gender.Male
            ),
        }
        self.karma = randint(0, 25) + randint(0, 25) + randint(0, 25) + randint(0, 25)
        self.total_happiness = 0
        self.meditated = False
        self.worked_out = False
        self.money = 0
        self.depressed = False
        self.student_loan = 0
        self.chose_student_loan = False
        self.uv_years = 0
        self.reset_already_did()
        self.grades = None
        self.dropped_out = False

    @property
    def relations(self):
        return list(self.parents.values())

    def change_grades(self, amount):
        if self.grades is not None:
            self.grades = clamp(self.grades + amount, 0, 100)

    def change_karma(self, amount):
        self.karma = clamp(self.karma + amount, 0, 100)

    def reset_already_did(self):
        self.meditated = False
        self.worked_out = False
        self.visited_library = False
        self.studied = False
        self.tried_to_drop_out = False

    def age_up(self):
        self.total_happiness += self.happiness
        super().age_up()
        self.reset_already_did()

        self.change_karma(randint(-2, 2))
        for parent in self.parents.values():
            parent.age_up()
            if self.age < 18:
                parent.change_relationship(1)
            else:
                parent.change_relationship(choice((-1, -1, 0)))
        print(_("Age {age}").format(age=self.age))
        if self.age > randint(98, 122) or (
            self.age > randint(80 + self.health // 12, 90 + self.health // 3)
            and randint(1, 100) <= 65
        ):
            self.die(_("You died of old age."))
            return
        if self.age > 50 and self.looks > randint(20, 25):
            decay = min((self.age - 51) // 5 + 1, 4)
            self.change_looks(-randint(0, decay))
        if self.happiness < 10 and not self.depressed:
            display_event(_("You are suffering from depression."))
            self.depressed = True
            self.change_happiness(-50)
            self.change_health(-randint(4, 8))
        for parent in list(self.parents.values()):
            if parent.age >= randint(110, 120) or (
                randint(1, 100) <= 50
                and parent.age
                >= max(
                    (randint(72, 90) + randint(0, parent.health // 4)) for _ in range(2)
                )
            ):
                rel_str = parent.name_accusative()
                display_event(
                    _("Your {relative} died at the age of {age}").format(
                        relative=rel_str, age=parent.age
                    )
                )
                del self.parents[parent.get_type()]
                self.change_happiness(-randint(40, 55))
        self.random_events()

    def calc_grades(self, offset):
        self.grades = clamp(round(10 * math.sqrt(self.smarts + offset)), 0, 100)

    def die(self, message):
        print(message)
        avg_happy = round(self.total_happiness / self.age)
        score = self.happiness * 0.3 + avg_happy * 0.7
        print_align_bars((_("Lifetime Happiness"), avg_happy), (_("Karma"), self.karma))
        exit()

    def display_stats(self):
        if self.happiness >= 60:
            if self.happiness >= 85:
                symbol = ":D"
            else:
                symbol = ":)"
        elif self.happiness < 40:
            if self.happiness < 15:
                symbol = ":'("
            else:
                symbol = ":("
        else:
            symbol = ":|"
        print_align_bars(
            (_("Happiness"), self.happiness, " " + symbol),
            (_("Health"), self.health),
            (_("Smarts"), self.smarts),
            (_("Looks"), self.looks),
            show_percent=True,
        )

    def random_events(self):
        if self.uv_years > 0:
            self.uv_years -= 1
            if self.uv_years == 0:
                self.grades = None
                display_event(_("You graduated from university."))
                self.change_happiness(randint(14, 20))
                self.change_smarts(randint(10, 15))
                if self.chose_student_loan:
                    self.student_loan = randint(20000, 40000)
                    print(_("You now have to start paying back your student loan"))
            else:
                if self.grades < randint(10, 35):
                    display_event(
                        _("You were expelled from university after earning bad grades.")
                    )
                    self.change_happiness(-randint(30, 50))
        if self.student_loan > 0:
            amount = min(randint(1000, 3000) for _ in range(3))
            amount = min(amount, self.student_loan)
            self.money -= amount
            self.student_loan -= amount
            if self.student_loan == 0:
                print(_("You've fully paid off your student loan"))
        if self.depressed:
            if self.happiness >= randint(20, 35):
                display_event(_("You are no longer suffering from depression"))
                self.change_happiness((100 - self.happiness) // 2)
                self.change_health(randint(4, 8))
                self.depressed = False
            else:
                self.change_happiness(-randint(1, 2))
                self.change_health(-randint(1, 4))
        if self.age == 2 and randint(1, 2) == 1:
            print(
                _("Your mother is taking to to the doctor's office to get vaccinated.")
            )
            print(_("How will you behave?"))
            choices = [_("Cooperate"), _("Throw a tantrum"), _("Bite her")]
            choice = choice_input(*choices)
            clear_screen()
            if choice == 1:
                print(_("You remained calm"))
            elif choice == 2:
                self.change_happiness(-randint(25, 35))
                self.parents["Mother"].change_relationship(-randint(6, 10))
                print(_("You threw a tantrum"))
            elif choice == 3:
                self.change_happiness(-randint(6, 10))
                self.parents["Mother"].change_relationship(-randint(25, 35))
                print(_("You bit your mother"))
        if self.grades is not None:
            self.change_grades(randint(-3, 3))
            base = round(10 * math.sqrt(self.smarts))
            if self.grades < base:
                self.change_grades(randint(1, 2))
            elif self.grades > base:
                self.change_grades(-randint(1, 2))
            grade_delta = (self.happiness - 50) / 30
            if grade_delta > 0:
                grade_delta /= 2
            self.change_grades(round_stochastic(grade_delta))
        if self.age == 6:
            print(_("You are starting elementary school"))
            self.change_smarts(randint(1, 2))
            self.calc_grades(randint(4, 8))
        if self.age == 12:
            print(_("You are starting middle school"))
            self.change_smarts(randint(1, 3))
            self.calc_grades(randint(0, 8))
        if self.age == 14:
            print(_("You are starting high school"))
            self.change_smarts(randint(1, 4))
            self.calc_grades(randint(-8, 8))
        if self.age == 17 and not self.dropped_out:
            self.grades = None
            print(_("You graduated from high school."))
            self.change_happiness(randint(15, 20))
            self.change_smarts(randint(6, 10))
            print()
            self.display_stats()
            print()
            print(_("Would you like to apply to university?"))
            choice = choice_input(_("Yes"), _("No"))
            clear_screen()
            if choice == 1:
                if self.smarts >= randint(28, 44):
                    print(_("Your application to university was accepted!"))
                    self.change_happiness(randint(7, 9))
                    SCHOLARSHIP = _("Scholarship")
                    LOAN = _("Student Loan")
                    PARENTS = _("Ask parents to pay")
                    choices = [SCHOLARSHIP, LOAN, PARENTS]
                    chosen = False
                    while not chosen:
                        print(_("How would you like to pay for your college tuition?"))
                        choice = choice_input(*choices, return_text=True)
                        clear_screen()
                        if choice == SCHOLARSHIP:
                            if self.smarts >= randint(randint(75, 85), 95):
                                display_event(
                                    _("Your scholarship application has been awarded!")
                                )
                                self.change_happiness(randint(10, 15))
                                chosen = True
                            else:
                                display_event(
                                    _("Your scholarship application was rejected.")
                                )
                                self.change_happiness(-randint(7, 9))
                                choices.remove(SCHOLARSHIP)
                        elif choice == PARENTS:
                            if randint(1, 6) == 1:
                                display_event(
                                    _(
                                        "Your parents agreed to pay for your university tuition!"
                                    )
                                )
                                self.change_happiness(randint(7, 9))
                                chosen = True
                            else:
                                display_event(
                                    _(
                                        "Your parents refused to pay for your university tuition."
                                    )
                                )
                                self.change_happiness(-randint(7, 9))
                                choices.remove(PARENTS)
                        else:
                            display_event(
                                _(
                                    "You took out a student loan to pay for your university tuition."
                                )
                            )
                            chosen = True
                            self.chose_student_loan = True
                    print(_("You are now enrolled in university."))
                    self.uv_years = 4
                    self.calc_grades(randint(-8, 10))
                else:
                    display_event(_("Your application to university was rejected."))
                    self.change_happiness(-randint(7, 9))
