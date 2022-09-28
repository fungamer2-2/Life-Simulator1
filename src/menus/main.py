from random import randint, triangular

from src.lifesim_lib.lifesim_lib import (
    choice_input,
    clear_screen,
    display_bar,
    display_event,
    draw_bar,
    Gender,
    int_input_range,
    press_enter,
    print_align_bars,
    round_stochastic,
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

    gender = _("Male") if p.gender == Gender.Male else _("Female")
    while True:
        print()
        print(_("Your name") + f": {p.name}")
        print(_("Gender") + f": {gender}")
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
                        p.change_happiness(enjoyment1 // 12 + randint(0, 1))
                        relation.change_relationship(enjoyment2 // 12 + randint(0, 1))
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
                            relation.change_relationship(agreement // 16)
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
                        p.change_karma(randint(0, 3))
                        relation.change_relationship(round_stochastic(appreciation / 6))
                        if randint(1, 200) <= appreciation:
                            display_event(
                                _("Your {relation} complimented you back!").format(
                                    relation=relation.name_accusative()
                                )
                            )
                            p.change_happiness(randint(5, 9))
                        relation.was_complimented = True
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
                    p.change_grades(randint(2, 3 + (100 - p.grades) // 5))
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
