from src.people.classes.player import Player
from src.people.classes.sibling import Sibling
from src.lifesim_lib.translation import _
from src.lifesim_lib.const import SAVE_PATH
import os, random, pickle
from random import randint
from src.lifesim_lib.lifesim_lib import *


def start_menu():
    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    saves = get_save_files()
    if saves:
        choice = choice_input(_("Load Game"), _("New Game"))
        if choice == 1:
            players = get_saves(saves)
            choices = [p["name"] for p in players]
            choice = choice_input(*choices)
            d = players[choice - 1]
            return Player.load(d)
    choice = choice_input(_("Random Life"), _("Custom Life"))

    if choice == 2:
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
        player = Player(first, last, Gender.Male if choice == 1 else Gender.Female)
        print(_("Would you like to Randomize or Customize your traits?"))
        choice = choice_input(_("Randomize"), _("Customize"))
        if choice == 1:
            player.randomize_traits()
        else:
            player.traits = set()
            all_traits = [t for t in Trait]
            while True:
                clear_screen()
                print(_("Enter a number to select or deselect a trait"))
                print(_('Select "Done" when finished'))
                print()
                print(_("Traits:"))
                if player.traits:
                    print(player.get_traits_str())
                else:
                    print(_("None"))
                print()
                can_choose = lambda t: not any(t.conflicts_with(other) for other in player.traits)
                options = [trait for trait in all_traits if can_choose(trait)]
                choices = list(map(lambda t: get_colored(t.name_, t.get_color()), options))
                choices.append(_("Done"))
                choice = choice_input(*choices)
                if choice == len(choices):
                    if yes_no(_("Would you like to start with these traits?")):
                        break
                else:
                    trait = options[choice - 1]
                    if trait in player.traits:
                        player.traits.remove(trait)
                    else:
                        player.traits.add(trait)
            clear_screen()   
        return player
    else:
        player = Player()
    mother = player.parents["Mother"]
    father = player.parents["Father"]
    print(
        _("Your mother is {name}, age {age}.").format(name=mother.name, age=mother.age)
    )
    print(
        _("Your father is {name}, age {age}.").format(name=father.name, age=father.age)
    )
    sibling_age = randint(2, 10)
    if (
        mother.age >= randint(16, 20) + sibling_age
        and father.age >= randint(16, 18) + sibling_age
        and randint(1, 6) < 6
    ):
        whichlast = random.choice(
            (player.parents["Mother"].lastname, player.parents["Father"].lastname)
        )
        theirsmarts = round_stochastic((randint(0, 100) + player.smarts) / 2)
        theirlooks = round_stochastic((randint(0, 100) + player.looks) / 2)
        sibling = Sibling(
            whichlast, sibling_age, Gender.random(), theirsmarts, theirlooks
        )
        player.relations.append(sibling)
        print(
            _("You have a {siblingtype} named {name}, age {age}.").format(
                siblingtype=sibling.get_translated_type().lower(),
                name=sibling.name,
                age=sibling.age,
            )
        )
    player.randomize_traits()
    return player
