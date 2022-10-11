import random
from random import randint

from src.lifesim_lib.const import *
from src.lifesim_lib.translation import _
from src.lifesim_lib.lifesim_lib import *
from src.people.classes.parent import Parent
from src.people.classes.person import Person
from src.people.classes.sibling import Sibling

def main_menu(player):
	print()
	display_data(_("Your name"), player.name)
	display_data(_("Gender"), player.get_gender_str())
	print(_("Money") + f": ${player.money:,}")
	if player.salary > 0:
		print(_("Salary") + f": ${player.salary:,}")
	
	player.display_stats()
	print()
	choices = [_("Age +1"), _("Relationships"), _("Activities")]
	if player.is_in_school():
		choices.append(_("School"))
	elif player.age >= 18:
		if player.has_job:
			choices.append(_("Job Menu"))
		else:
			choices.append(_("Find a Job"))
	if DEBUG:
		choices.append(_("Debug Menu"))
	choice = choice_input(*choices, return_text=True)
	clear_screen()
	if choice == _("Age +1"):
		print()
		player.age_up()
	if choice == _("Relationships"):
		relations = player.relations
		print(_("Relationships: "))
		for num, relation in enumerate(relations):
			print(f"{num+1}. {relation.name} ({relation.get_translated_type()})")
		back = _("Back")
		print(f"{len(relations)+1}. {back}")
		choice = int_input_range(1, len(relations) + 1)
		clear_screen()
		if choice <= len(player.relations):
			relation = relations[choice - 1]
			print(
				_("Name")
				+ ": "
				+ relation.name
				+ f" ({relation.get_translated_type()})"
			)
			print(_("Age") + f": {relation.age}")
			bars = [(_("Relationship"), relation.relationship)]
			if isinstance(relation, Parent):
				bars.append((_("Generosity"), relation.generosity))
				bars.append((_("Money"), relation.money))
			elif isinstance(relation, Sibling):
				bars.append((_("Smarts"), relation.smarts))
				bars.append((_("Looks"), relation.looks))
				bars.append((_("Petulance"), relation.petulance))
			print_align_bars(*bars)
			choices = [_("Back")]
			if relation.age >= 5:
				if player.age >= 3:
					choices.append(_("Spend time"))
					choices.append(_("Have a conversation"))
				if player.age >= 6:
					choices.append(_("Compliment"))
					choices.append(_("Insult"))
			choice = choice_input(*choices, return_text=True)
			clear_screen()
			if choice == _("Spend time"):
				if relation.relationship < 15:
					print(_("Your {relation} refused to see you."))
					player.change_happiness(-4)
				else:
					print(
						_("You spent time with your {relation}.").format(
							relation=relation.name_accusative()
						)
					)
					enjoyment1 = max(randint(0, 70), randint(0, 70)) + randint(0, 30)
					enjoyment2 = round(random.triangular(0, 100, relation.relationship))
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
						player.change_happiness(round_stochastic(enjoyment1 / 12))
						relation.change_relationship(round_stochastic(enjoyment2 / 12))
						relation.spent_time = True
			elif choice == _("Have a conversation"):
				if relation.relationship < 25:
					display_event(
						_(
							"Your {relation} isn't interested in having a conversation with you."
						).format(relation=relation.name_accusative())
					)
					player.change_happiness(-4)
				else:
					agreement = random.triangular(0, 100, 65)
					agreement += randint(0, max(0, (relation.relationship - 50) // 3))
					if isinstance(relation, Sibling) and randint(1, 2) == 1:
						agreement -= randint(0, relation.petulance // 3)
					agreement = clamp(
						round(agreement), randint(0, 10), randint(90, 100)
					)
					print(
						_("You had a conversation with your {relation}.").format(
							relation=relation.name_accusative()
						)
					)
					display_bar(_("Agreement"), agreement)
					if not relation.had_conversation:
						player.change_happiness(4)
						relation.change_relationship(round_stochastic(agreement / 12))
						relation.had_conversation = True
					if agreement < 15:
						relation.change_relationship(-randint(2, 8))
						print(
							_(
								"You and your {relation} got into an argument. What will you do?"
							).format(relation=relation.name_accusative())
						)
						choice = choice_input(
							_("Apologize"),
							_("Agree to disagree"),
							_("Insult {him_her}").format(him_her=relation.him_her()),
						)
						if choice == 1:
							player.change_karma(randint(1, 3))
							print(
								_("You apologized to your {relation}").format(
									relation=relation.name_accusative()
								)
							)
							relation.change_relationship(randint(2, 4))
						elif choice == 2:
							print(_("You agreed to disagree"))
						elif choice == 3:
							player.change_karma(-randint(2, 6))
							print(
								_("You insulted your {relation}").format(
									relation=relation.name_accusative()
								)
							)
							relation.change_relationship(-randint(4, 7))
			elif choice == _("Compliment"):
				appreciation = randint(0, 60) + randint(0, 40)
				diff = player.smarts - relation.smarts + 50
				if randint(1, 100) <= diff:
					appreciation = max(appreciation, randint(0, 60) + randint(0, 40))
				print(
					_("You complimented your {relation}.").format(
						relation=relation.name_accusative()
					)
				)
				display_bar(
					_("{his_her} Appreciation").format(
						his_her=relation.his_her().capitalize()
					),
					appreciation,
				)
				press_enter()
				if not relation.was_complimented:
					player.change_karma(randint(0, 2))
					relation.change_relationship(round_stochastic(appreciation / 6))
					if randint(1, 300) <= round_stochastic(
						appreciation * relation.relationship / 50
					):
						display_event(
							_("Your {relation} complimented you back!").format(
								relation=relation.name_accusative()
							)
						)
						player.change_happiness(randint(6, 10))
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
					player.change_karma(-randint(2, 4))
					if isinstance(relation, Sibling):
						chance = 50 * (relation.petulance/100)**1.5
					else:
						chance = (100 - relation.relationship) / 4
					if random.uniform(0, 100) < chance:
						display_event(
							_("Your {rel} insulted you back.").format(rel=rel)
						)
						player.change_happiness(-randint(1, 5) if isinstance(relation, Sibling) else -randint(3, 8))
			print()
	if choice == _("Activities"):
		print(_("Activities Menu"))
		print()
		choices = [_("Back")]
		if 3 <= player.age < 13:
			choices.append(_("Play with your toys"))
		if player.age >= 5:
			choices.append(_("Arts and Crafts"))
		if player.age >= 13:
			choices.append(_("Meditate"))
			choices.append(_("Library"))
			choices.append(_("Gym"))
		if player.age >= 18:
			choices.append(_("Lottery"))
		choices.append(_("Surrender"))
		choice = choice_input(*choices, return_text=True)
		clear_screen()
		if choice == _("Play with your toys"):
			if player.depressed:
				print(_("You don't feel like playing, but you decide to try anyway."))
				happy_gain = randint(0, 6)
			else:
				sayings = [
					_("You played with your toys."),
					_("You had a lot of fun playing with your toys.")
				]
				print(random.choice(sayings))
				happy_gain = randint(5, 10)
			if not player.played:
				player.played = True
				player.change_happiness(happy_gain)
		if choice == _("Arts and Crafts"):
			if randint(1, 10) == 1:
				print(_("You thought about doing arts and crafts, but couldn't decide what to make."))
				player.change_happiness(-randint(1, 3))
			else:
				if randint(1, 2) == 1 or player.age < 16:
					print(_("You decided to paint."))
					if not player.did_arts_and_crafts:
						player.change_happiness(randint(2, 4))
						player.change_smarts(randint(0, 2))
				else:
					print(_("You decided to bake something tasty!"))
					if not player.did_arts_and_crafts:
						player.change_happiness(randint(3, 6))
						player.change_smarts(randint(1, 3)) 
				player.did_arts_and_crafts = True
		if choice == _("Meditate"):
			print(_("You practiced meditation."))
			if not player.meditated:  # You can only get the bonus once per year
				player.change_health(randint(2, 4))
				player.change_happiness(randint(3, 5))
				player.change_karma(randint(1, 3))
				player.change_stress(-randint(3, 8))
				if player.times_meditated == 0 or randint(1, 20) == 1: #Your first meditation is guaranteed to cause a deeper awareness
					player.change_happiness(2)
					player.change_stress(-3)
					print(_("You have achieved a deeper awareness of yourself."))
					display_bar(_("Karma"), player.karma)
				player.meditated = True
				player.times_meditated += 1
		elif choice == _("Library"):
			print(_("You went to the library."))
			enjoyment = randint(15, 65)
			display_bar(_("Your Enjoyment"), enjoyment)
			if not player.visited_library:  # You can only get the bonus once per year
				player.change_happiness(round_stochastic(enjoyment/15))
				player.change_smarts(randint(2, 5))
				player.visited_library = True
		elif choice == _("Gym"):
			if player.health < 10:
				print(_("Your health is too weak to visit the gym."))
			else:
				workout = randint(25, 75)
				if player.health > 50:
					workout += randint(0, (player.health - 50) // 2)
				else:
					workout -= randint(0, (50 - player.health) // 2)
				lo = -25
				hi = 25
				if workout < 25:
					lo = -workout
				elif workout > 75:
					hi = 100 - workout
				workout += randint(lo, hi)
				print(_("You worked out at the gym."))
				print(_("Workout") + ": " + draw_bar(workout, 100, 25))
				if not player.worked_out:
					player.change_happiness(round(workout / 12) + randint(0, 1))
					player.change_health(round(workout / 14) + randint(1, 2))
					if player.looks < workout:
						player.change_looks(
							randint(1, 3) + randint(0, round(workout / 33))
						)
					player.worked_out = True
				print()
		elif choice == _("Lottery"):
			print(_("Play the lottery today!"))
			print(_("Ticket cost: $4 each"))
			print(_("Lottery jackpot: ${jackpot}").format(jackpot=player.lottery_jackpot))
			choice = choice_input(_("Buy a ticket"), _("Buy 10 tickets"), _("Back"))
			ticket_num = 0
			if choice == 1:
				ticket_num = 1
			elif choice == 2:
				ticket_num = 10
			cost = ticket_num * 4
			if ticket_num > 0:
				if player.money < cost:
					print(_("You don't have enough money"))
				else:
					player.money -= cost
					print(_("Guess the 4 winning numbers between 1 and 20. Each number in the line must be separated by a space."))
					if ticket_num > 1:
						print(_("The numbers within each line must be unique."))
					else:
						print(_("The numbers must be unique."))
					guessed = []
					for i in range(ticket_num):
						valid = False
						while not valid:
							valid = True
							if ticket_num > 1:
								msg = _("Guess #{num}: ").format(num=i+1)
							else:
								msg = _("Guess: ")
							guess = input(msg)
							nums = guess.split()
							try:
								nums = list(map(int, nums))
							except ValueError:
								print(_("The values must all be integers."))
								valid = False
								continue
							if len(nums) != 4:
								print(_("You must enter exactly 4 numbers"))
								valid = False
							elif not all(1 <= val <= 20 for val in nums):
								print(_("All values must be between 1 and 20"))
								valid = False
							elif len(nums) != len(set(nums)):
								print(_("All values must be unique."))
								valid = False
							else:
								guessed.append(nums)
					winning = random.sample(range(1, 21), 4)
					print(_("The winning numbers are {nums}").format(nums=", ".join(map(str, winning))))	
					won = False
					for guess in guessed:
						if set(guess) == set(winning):
							won = True
							break
					if won:
						print(_("YOU WON THE ${amount} LOTTERY JACKPOT!!!").format(amount=player.lottery_jackpot))
						player.change_happiness(100)
						player.money += player.lottery_jackpot
						player.change_jackpot()
					else:
						print(_("You did not win the ${amount} lottery jackpot.").format(amount=player.lottery_jackpot))
		elif choice == _("Surrender"):
			if yes_no(_("Are you sure you want to surrender this life?")):
				if yes_no(_("This will kill your current character. Continue?")):
					player.die(_("You surrendered."))
	if choice == _("School"):
		print(_("School Menu"))
		print()
		display_bar(_("Grades"), player.grades)
		choice = choice_input(_("Back"), _("Study harder"), _("Drop out"))
		clear_screen()
		if choice == 2:
			print(_("You began studying harder"))
			if not player.studied:
				player.change_grades(randint(5, 7 + (100 - player.grades) // 5))
				player.change_smarts(randint(0, 2))
				player.studied = True
		if choice == 3:
			can_drop_out = player.smarts < randint(8, 12) + randint(0, 13)
			can_drop_out &= not player.tried_to_drop_out
			if (
				player.age >= 18
				or player.uv_years > 0
				or (player.age >= randint(15, 16) and can_drop_out)
			):
				player.dropped_out = True
				player.grades = None
				print(_("You dropped out of school."))
				if player.uv_years > 0:
					player.uv_years = 0
			else:
				player.tried_to_drop_out = True
				print(_("Your parents won't let you drop out of school."))
	if choice == _("Debug Menu"):
		choice = choice_input(_("Back"), _("Stats"), _("Identity"))
		if choice == 2:
			while True:
				clear_screen()
				print(_("Your stats"))
				display_data(_("Happiness"), player.happiness)
				display_data(_("Health"), player.health)
				display_data(_("Smarts"), player.smarts)
				display_data(_("Looks"), player.looks)
				display_data(_("Karma"), player.karma)
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
						player.happiness = val
				elif choice == 3:
					print(_("What would you like to set Health to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						player.health = val
				elif choice == 4:
					print(_("What would you like to set Smarts to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						player.smarts = val
				elif choice == 5:
					print(_("What would you like to set Looks to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						player.looks = val
				elif choice == 6:
					print(_("What would you like to set Karma to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						player.karma = val
		elif choice == 3:
			while True:
				clear_screen()
				display_data(_("First name"), player.firstname)
				display_data(_("Last name"), player.lastname)
				display_data(_("Gender"), player.get_gender_str())
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
						player.firstname = name
				elif choice == 3:
					name = input(_("Enter last name: ")).strip()
					if name:
						player.lastname = name
				elif choice == 4:
					if player.gender == Gender.Male:
						player.gender = Gender.Female
					else:
						player.gender = Gender.Male
	if choice == _("Find a Job"):
		salary = round_stochastic(randexpo(30000, 55000)) #TODO: Add a selection of different types of jobs
		if yes_no(_("You found a job with a salary of ${salary:,}. Would you like to apply?").format(salary=salary)):
			m = 100 + round_stochastic((salary-30000)/600)
			mod = 50 - player.smarts #Mod is inverted because we want to roll 100 OR LOWER to get the job
			roll = randint(1, m)
			if mod > 0:
				roll += randint(0, mod)
			elif mod < 0:
				roll -= randint(0, abs(mod))
			if roll <= 100:
				print(_("You got the job!"))
				player.change_happiness(4)
				player.get_job(salary)
			else:
				print(_("You didn't get an interview."))
				player.change_happiness(-randint(1, 4))
		else:
			clear_screen()
	elif choice == _("Job Menu"):
		print(_("Your job"))
		print()
		display_bar(_("Stress"), player.stress)
		can_retire = player.years_worked >= 10 and player.age >= 65
		choice = choice_input(_("Back"), _("Retire") if can_retire else _("Quit Job"))
		if choice == 2:
			if can_retire:
				pension = round(player.salary * min(player.years_worked, 35) * 0.02)
				if yes_no(_("Do you want to retire? You will receive a yearly pension of ${pension}").format(pension=pension)):
					player.lose_job()
					player.salary = pension
					player.change_happiness(randint(25, 50))
					print(_("You retired and are now receiving pension of ${pension}.").format(pension=pension))
			elif yes_no(_("Are you sure you want to quit your job?")):
				player.lose_job()
				print(_("You quit your job."))
		#TODO: Add ability to ask for a raise