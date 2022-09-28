from random import randint, triangular

from src.lifesim_lib.const import CONST
from src.lifesim_lib.lifesim_lib import (
    choice_input,
    clear_screen,
    display_bar,
    display_data,
    display_event,
    draw_bar,
    Gender,
    int_input_range,
    int_input_range_optional,
    press_enter,
    print_align_bars,
    round_stochastic,
    yes_no,
)
from src.people.classes.player import Player

_ = lambda s: s


def MainMenu():
    choice = choice_input(_("Random Life"), _("Custom Life"))
    if choice == 1:
        p = Player()
    else:
        first = ""
        last = ""
        while not first:
            first = input(_("Enter your first name: ")).strip()
        while not last:
            last = input(_("Enter your last name: ")).strip()
        print()
        print(_("Choose your gender:"))
        choice = choice_input(_("Male"), _("Female"))
        print()
        p = Player(first, last, Gender.Male if choice == 1 else Gender.Female)

    while True:
        print()
        print(_("Your name") + f": {p.name}")
        print(_("Gender") + f": {p.get_gender_str()}")
        print(_("Money") + f": ${p.money:,}")
        p.display_stats()
        print()
        if p.alive == False:
            print(_("You died."))
            avg_happy = round(p.total_happiness / p.age)
            score = p.happiness * 0.3 + avg_happy * 0.7
            print_align_bars(
                (_("Lifetime Happiness"), avg_happy), (_("Karma"), p.karma)
            )
            exit()
        choices = [_("Age +1"), _("Relationships"), _("Activities")]
        if p.grades is not None:
            choices.append(_("School"))
        if CONST.DEBUG:
            choices.append(_("Debug Menu"))
        choice = choice_input(*choices, return_text=True)
        clear_screen()
        if choice == _("Age +1"):
            print()
            p.age_up()
        if choice == _("Relationships"):
            relations = p.relations
            print(_("Relationships: "))
            for num, relation in enumerate(relations):
                print(f"{num+1}. {relation.name} ({relation.get_translated_type()})")
            back = _("Back")
            print(f"{len(relations)+1}. {back}")
            choice = int_input_range(1, len(relations) + 1)
            clear_screen()
            if choice <= len(p.relations):
                relation = relations[choice - 1]
                print(
                    _("Name")
                    + ": "
                    + relation.name
                    + f" ({relation.get_translated_type()})"
                )
                print(_("Age") + f": {relation.age}")
                display_bar(_("Relationship"), relation.relationship)
                choices = [_("Back")]
                if p.age >= 5:
                    choices.append(_("Spend time"))
                    choices.append(_("Have a conversation"))
                if p.age >= 6:
                    choices.append(_("Compliment"))
                    choices.append(_("Insult"))
                choice = choice_input(*choices, return_text=True)
                clear_screen()
                if choice == _("Spend time"):
                    print(
                        _("You spent time with your {relation}.").format(
                            relation=relation.name_accusative()
                        )
                    )
                    enjoyment1 = max(randint(0, 70), randint(0, 70)) + randint(0, 30)
                    enjoyment2 = round(triangular(0, 100, relation.relationship))
                    print_align_bars(
                        (_("Your Enjoyment"), enjoyment1),
                        (
                            _("{his_her} Enjoyment").format(
                                his_her=relation.his_her().capitalize()
                            ),
                            enjoyment2,
                        ),
                    )
                    if not relation.spent_time:
                        p.change_happiness(round_stochastic(enjoyment1 / 12))
                        relation.change_relationship(round_stochastic(enjoyment2 / 12))
                        relation.spent_time = True
                elif choice == _("Have a conversation"):
                    if relation.relationship < 24:
                        display_event(
                            _(
                                "Your {relation} isn't interested in having a conversation with you."
                            ).format(relation=relation.name_accusative())
                        )
                        p.change_happiness(-4)
                    else:
                        agreement = triangular(0, 100, 65)
                        agreement += randint(
                            0, max(0, (relation.relationship - 50) // 3)
                        )
                        agreement = min(round(agreement), randint(90, 100))
                        print(
                            _("You had a conversation with your {relation}.").format(
                                relation=relation.name_accusative()
                            )
                        )
                        display_event(
                            _("Agreement") + ": " + draw_bar(agreement, 100, 25)
                        )
                        if not relation.had_conversation:
                            p.change_happiness(4)
                            relation.change_relationship(
                                round_stochastic(agreement / 12)
                            )
                            relation.had_conversation = True
                elif choice == _("Compliment"):
                    appreciation = randint(0, 60) + randint(0, 40)
                    if randint(1, 100) <= p.smarts:
                        appreciation = max(
                            appreciation, randint(0, 60) + randint(0, 40)
                        )
                    print(
                        _("You complimented your {relation}.").format(
                            relation=relation.name_accusative()
                        )
                    )
                    display_bar(
                        _("{his_her} Appreciation: ").format(
                            his_her=relation.his_her().capitalize()
                        ),
                        appreciation,
                    )
                    press_enter()
                    if not relation.was_complimented:
                        p.change_karma(randint(0, 2))
                        relation.change_relationship(round_stochastic(appreciation / 6))
                        if randint(1, 300) <= round_stochastic(
                            appreciation * relation.relationship / 50
                        ):
                            display_event(
                                _("Your {relation} complimented you back!").format(
                                    relation=relation.name_accusative()
                                )
                            )
                            p.change_happiness(randint(6, 10))
                        relation.was_complimented = True
                elif choice == _("Insult"):
                    rel = relation.name_accusative()
                    if yes_no(
                        _("Are you sure you want to insult your {relation}?").format(
                            relation=rel
                        )
                    ):
                        display_event(_("You insulted your {rel}.").format(rel=rel))
                        relation.change_relationship(-randint(4, 8))
                        p.change_karma(-randint(2, 4))
                        if randint(1, 3) == 1 and relation.relationship < randint(
                            1, 100
                        ):
                            display_event(
                                _("Your {rel} insulted you back.").format(rel=rel)
                            )
                            p.change_happiness(-randint(4, 9))
                print()
        if choice == _("Activities"):
            print(_("Activities Menu"))
            print()
            choices = [_("Back")]
            if p.age >= 13:
                choices.append(_("Meditate"))
                choices.append(_("Library"))
            if p.age >= 18:
                choices.append(_("Gym"))
            choice = choice_input(*choices, return_text=True)
            clear_screen()
            if choice == _("Meditate"):
                print(_("You practiced meditation."))
                if not p.meditated:  # You can only get the bonus once per year
                    p.change_health(randint(2, 5))
                    p.change_happiness(randint(3, 6))
                    p.change_karma(randint(0, 3))
                    if randint(1, 12) == 1:
                        p.change_happiness(2)
                        print(_("You have achieved a deeper awareness of yourself."))
                        print(_("Karma") + ": " + draw_bar(p.karma, 100, 25))
                    p.meditated = True
            elif choice == _("Library"):
                print(_("You went to the library."))
                if not p.visited_library:  # You can only get the bonus once per year
                    p.change_happiness(randint(0, 4))
                    p.change_smarts(randint(2, 5))
                    p.visited_library = True
            elif choice == _("Gym"):
                if p.health < 10:
                    print(_("Your health is too weak to visit the gym."))
                else:
                    workout = randint(25, 75)
                    if p.health > 50:
                        workout += randint(0, (p.health - 50) // 2)
                    else:
                        workout -= randint(0, (50 - p.health) // 2)
                    lo = -25
                    hi = 25
                    if workout < 25:
                        lo = -workout
                    elif workout > 75:
                        hi = 100 - workout
                    workout += randint(lo, hi)
                    print(_("You worked out at the gym."))
                    print(_("Workout") + ": " + draw_bar(workout, 100, 25))
                    if not p.worked_out:
                        p.change_happiness(round(workout / 12) + randint(0, 1))
                        p.change_health(round(workout / 14) + randint(1, 2))
                        if p.looks < workout:
                            p.change_looks(
                                randint(1, 3) + randint(0, round(workout / 33))
                            )
                        p.worked_out = True
                    print()
        if choice == _("School"):
            print(_("School Menu"))
            print()
            display_bar(_("Grades"), p.grades)
            choice = choice_input(_("Back"), _("Study harder"), _("Drop out"))
            clear_screen()
            if choice == 2:
                print(_("You began studying harder"))
                if not p.studied:
                    p.change_grades(randint(5, 7 + (100 - p.grades) // 5))
                    p.change_smarts(randint(0, 2))
                    p.studied = True
            if choice == 3:
                can_drop_out = p.smarts < randint(8, 12) + randint(0, 13)
                can_drop_out &= not p.tried_to_drop_out
                if (
                    p.age >= 18
                    or p.uv_years > 0
                    or (p.age >= randint(15, 16) and can_drop_out)
                ):
                    p.dropped_out = True
                    p.grades = None
                    print(_("You dropped out of school."))
                    if p.uv_years > 0:
                        p.uv_years = 0
                else:
                    p.tried_to_drop_out = True
                    print(_("Your parents won't let you drop out of school."))

        if choice == _("Debug Menu"):
            choice = choice_input(_("Back"), _("Stats"), _("Identity"))
            if choice == 2:
                while True:
                    clear_screen()
                    print(_("Your stats"))
                    display_data(_("Happiness"), p.happiness)
                    display_data(_("Health"), p.health)
                    display_data(_("Smarts"), p.smarts)
                    display_data(_("Looks"), p.looks)
                    display_data(_("Karma"), p.karma)
                    choice = choice_input(
                        _("Back"),
                        _("Modify Happiness"),
                        _("Modify Health"),
                        _("Modify Smarts"),
                        _("Modify Looks"),
                        _("Modify Karma"),
                    )
                    if choice == 1:
                        break
                    elif choice == 2:
                        print(_("What would you like to set Happiness to? (0-100)"))
                        val = int_input_range_optional(0, 100)
                        if val is not None:
                            p.happiness = val
                    elif choice == 3:
                        print(_("What would you like to set Health to? (0-100)"))
                        val = int_input_range_optional(0, 100)
                        if val is not None:
                            p.health = val
                    elif choice == 4:
                        print(_("What would you like to set Smarts to? (0-100)"))
                        val = int_input_range_optional(0, 100)
                        if val is not None:
                            p.smarts = val
                    elif choice == 5:
                        print(_("What would you like to set Looks to? (0-100)"))
                        val = int_input_range_optional(0, 100)
                        if val is not None:
                            p.looks = val
                    elif choice == 6:
                        print(_("What would you like to set Karma to? (0-100)"))
                        val = int_input_range_optional(0, 100)
                        if val is not None:
                            p.karma = val
            elif choice == 3:
                while True:
                    clear_screen()
                    display_data(_("First name"), p.firstname)
                    display_data(_("Last name"), p.lastname)
                    display_data(_("Gender"), p.get_gender_str())
                    choice = choice_input(
                        _("Back"),
                        _("Change first name"),
                        _("Change last name"),
                        _("Change gender"),
                    )
                    if choice == 1:
                        break
                    elif choice == 2:
                        name = input(_("Enter first name: ")).strip()
                        if name:
                            p.firstname = name
                    elif choice == 3:
                        name = input(_("Enter last name: ")).strip()
                        if name:
                            p.lastname = name
                    elif choice == 4:
                        if p.gender == Gender.Male:
                            p.gender = Gender.Female
                        else:
                            p.gender = Gender.Male
