import random
from random import randint

from src.lifesim_lib.const import *
from src.countries import *
from src.lifesim_lib.translation import _
from src.lifesim_lib.lifesim_lib import *
from src.people.classes.parent import Parent
from src.people.classes.person import Person
from src.people.classes.sibling import Sibling
from src.people.classes.partner import Partner
from src.people.classes.child import Child
from src.menus.activities import activities_menu

def main_menu(player):
	print()
	display_data(_("Your name"), player.name)
	t = player.get_traits_str() if player.traits else "None"
	display_data(_("Traits"), t)
	display_data(_("Gender"), player.get_gender_str())
	display_data(_("Money"), f"${player.money:,}")
	if player.salary > 0:
		print(_("Salary") + f": ${player.salary:,}")
	if player.generation > 1:
		display_data(_("Generation"), player.generation)
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
	choices.append(_("View Saved Games"))
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
			elif isinstance(relation, (Sibling, Partner, Child)):
				bars.append((_("Smarts"), relation.smarts))
				bars.append((_("Looks"), relation.looks))
				if isinstance(relation, Sibling):
					bars.append((_("Petulance"), relation.petulance))
				elif isinstance(relation, Partner):
					bars.append((_("Craziness"), relation.craziness))
			print_align_bars(*bars)
			choices = [_("Back")]
			if relation.age >= 5:
				if player.age >= 1:
					choices.append(_("Spend time"))
				if player.age >= 3:
					choices.append(_("Have a conversation"))
				if player.age >= 6:
					choices.append(_("Compliment"))
					choices.append(_("Insult"))
				if isinstance(relation, Partner):
					choices.append(_("Have a baby"))
					if relation.status < 2:
						choices.append(_("Break up"))
					else:
						choices.append(_("Divorce"))
					if relation.status == 0:
						choices.append(_("Propose"))
					elif relation.status == 1:
						choices.append(_("Plan the wedding"))
						choices.append(_("Call off the engagement"))
				elif player.age >= 6 and isinstance(relation, Parent):
					choices.append(_("Ask for money"))
			choice = choice_input(*choices, return_text=True)
			clear_screen()
			if choice == _("Spend time"):
				if relation.relationship < 15:
					print(_("Your {relation} refused to see you.").format(relation=relation.name_accusative()))
					player.change_happiness(-4)
				else:
					enjoyment1 = max(randint(0, 70), randint(0, 70)) + randint(0, 30)
					if player.has_trait("CHEERFUL"):
						enjoyment1 = max(enjoyment1, randint(0, 100))
					elif player.has_trait("GRUMPY"):
						enjoyment1 = min(enjoyment1, randint(0, 100))
					enjoyment2 = round(random.triangular(0, 100, relation.relationship))
					if isinstance(relation, Child):
						enjoyment1 += round_stochastic((100 - enjoyment1)*max(0, 18 - relation.age)/randint(36, 100))
						enjoyment2 += round_stochastic((100 - enjoyment2)*max(0, 13 - relation.age)/randint(26, 39))
					print(_("You took your {relation} {place}.").format(relation=relation.name_accusative(), place=random.choice(SPEND_TIME_PLACES)))
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
						if player.has_trait("CHEERFUL"):
							player.change_happiness(3)
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
					agreement = random.triangular(0, 100, 70)
					agreement += randint(0, max(0, (relation.relationship - 50) // 3))
					if isinstance(relation, Sibling) and randint(1, 2) == 1:
						agreement -= randint(0, relation.petulance // 3)
					if player.age < 6:
						v = (6 - player.age) * 8
						agreement += randint(v // 4, v)
					agreement = clamp(
						round(agreement), randint(0, 10), randint(90, 100)
					)
					chat = random.choice(CHATS)
					discussion = random.choice(DISCUSSIONS)
					talk = random.choice(TALKS)
					heart_to_heart = random.choice(HEART_TO_HEARTS)
					sayings = [
						_(
							"You and your {relation} had a chat about the hierarchy of licorice."
						).format(relation=relation.name_accusative()),
						_("You and your {relation} had a chat about {chat}.").format(
							relation=relation.name_accusative(),
							chat=chat
						),
						_(
							"You and your {relation} had a chat about which is better, Star Wars or Star Trek."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} had a chat about which is better, Coke or Pepsi."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} had a chat about which is better, Lord of the Rings or Harry Potter."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} had a chat about who is better, the Red Sox or Yankees."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} discussed Frida Kahlo's moustache."
						).format(relation=relation.name_accusative()),
						_("You and your {relation} discussed {discussion}.").format(
							relation=relation.name_accusative(),
							discussion=discussion
						),
						_(
							"You and your {relation} discussed which is the best breed of dog."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} discussed which is the best breed of cat."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} discussed why dogs are better than cats."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} discussed why cats are better than dogs."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} talked about whether you would rather have overly large hands or small feet."
						).format(relation=relation.name_accusative()),
						_("You and your {relation} talked about {talk}.").format(
							relation=relation.name_accusative(),
							talk=talk
						),
						_(
							"You and your {relation} talked about who will win the Monaco Grand Prix."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} had a heart-to-heart about the best gift you ever received."
						).format(relation=relation.name_accusative()),
						_(
							"You and your {relation} had a heart-to-heart about {heart_to_heart}."
						).format(relation=relation.name_accusative(), heart_to_heart=heart_to_heart),
					]
					print(random.choice(sayings))
					display_bar(_("Agreement"), agreement)
					if not relation.had_conversation:
						player.change_happiness(
							8 if player.has_trait("CHEERFUL") else 4
						)
						relation.change_relationship(round_stochastic(agreement / 12))
						relation.had_conversation = True
					if agreement < 15:
						relation.change_relationship(-randint(2, 8))
						player.change_happiness(-4)
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
							player.change_happiness(-randint(2, 4))
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
							insult = random.choice(INSULTS)
							print(
								_("You called your {relation} {insult}.").format(
									relation=relation.name_accusative(), insult=insult
								)
							)
							relation.change_relationship(-randint(4, 7))
			elif choice == _("Ask for money"):
				typ = relation.name_accusative()
				if relation.asked_for_money >= 3:
					print(_("Your {parent} told you to stop asking for money.").format(parent=typ))
					if relation.relationship < 25:
						insult = random.choice(INSULTS)
						print(_("{he_she} called you {insult}.").format(he_she=relation.he_she().capitalize(), insult=insult))
					relation.change_relationship(-randint(5, 10))
				else:
					if relation.asked_for_money == 0 and randint(1, 35) <= relation.generosity:
						amount = 5 ** (relation.generosity/22) * (relation.money/100)**2 * math.sqrt(player.age)
						amount = max(randint(1, 5), round_stochastic(amount * random.uniform(0.6, 1.4)))
						print(_("Your {parent} gave you ${amount}.").format(parent=typ, amount=amount))
						player.money += amount
						relation.change_relationship(-randint(0, 8))
						relation.ask_money_cd = 3
					else:
						print(_("Your {parent} refused to give you any money.").format(parent=typ))
						relation.change_relationship(-randint(4, 8))
					relation.asked_for_money += 1
			elif choice == _("Compliment"):
				appreciation = randint(0, 60) + randint(0, 40)
				relationship = relation.relationship
				if relationship >= randint(51, 100):
					appreciation = max(appreciation, randint(0, 60) + randint(0, 40))
					if relationship >= randint(75, 120):
						appreciation = max(
							appreciation, randint(0, 60) + randint(0, 40)
						)
				elif relationship <= randint(0, 49):
					appreciation = min(appreciation, randint(0, 60) + randint(0, 40))
					if relationship <= randint(0, 25):
						appreciation = min(
							appreciation, randint(0, 60) + randint(0, 40)
						)
				compliments = COMPLIMENTS[:]
				if relation.gender == Gender.Male:
					compliments.extend([
						_("an alpha male"),
						_("handsome")
					])
				else:
					compliments.extend([
						_("an alpha female"),
						_("beautiful")
					])
				compliment = random.choice(COMPLIMENTS)
				print(
					_("You told your {relation} that {hes_shes} {compliment}.").format(
						relation=relation.name_accusative(),
						hes_shes=relation.hes_shes(),
						compliment=compliment,
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
					roll = randint(1, 300)
					if roll <= round_stochastic(
						appreciation * relation.relationship / 50
					):
						compliment = random.choice(COMPLIMENTS)
						display_event(
							_(
								"Your {relation} told you that you're {compliment}!"
							).format(
								relation=relation.name_accusative(),
								compliment=compliment,
							)
						)
						player.change_happiness(
							randint(6, 10) - (3 * (player.has_trait("GRUMPY")))
						)
						if player.has_trait("CHEERFUL"):
							player.change_happiness(4)
						if roll <= 15: #Like a natural 20, in a way
							relation.change_relationship(randint(25, 40))
					relation.was_complimented = True
			elif choice == _("Insult"):
				rel = relation.name_accusative()
				if yes_no(
					_("Are you sure you want to insult your {relation}?").format(
						relation=rel
					)
				):
					insult = random.choice(INSULTS)
					display_event(
						_("You called your {rel} {insult}.").format(
							rel=rel, insult=insult
						)
					)
					relation.change_relationship(-randint(4, 8))
					player.change_karma(-randint(2, 4))
					if isinstance(relation, Sibling):
						chance = 50 * (relation.petulance / 100) ** 1.5
					else:
						chance = (100 - relation.relationship) / 4
					attack_chance = 0
					if isinstance(relation, Sibling):
						attack_chance = 30 * (relation.petulance/100)**1.5
					elif isinstance(relation, Partner):
						attack_chance = 45 * (relation.craziness/100)**2
					if random.uniform(0, 100) < attack_chance:
						display_event(_("Your {rel} attacked you!").format(rel=rel))
						player.was_attacked(randint(4, 10), False)
						relation.change_relationship(-randint(4, 8))
					elif random.uniform(0, 100) < chance:
						insult = random.choice(INSULTS)
						display_event(
							_("Your {rel} called you {insult}!").format(
								rel=rel, insult=insult
							)
						)
						player.change_happiness(-randint(2, 6))
			elif choice == _("Have a baby"):
				already_pregnant = player.partner.is_pregnant if player.gender == Gender.Male else player.is_pregnant
				if already_pregnant:
					rel = player.partner.name_accusative()
					if player.gender == Gender.Male:
						print(_("Your {partner} is already pregnant!").format(partner=rel))
					else:
						print(_("You are already pregnant!"))
				elif relation.relationship >= randint(45, 75) and player.partner.years_together >= randint(1, 2):
					rel = player.partner.name_accusative()
					display_event(_("You and your {partner} tried for a baby.").format(partner=rel), cls=False)
					fertility = player.partner.fertility if player.gender == Gender.Male else player.fertility
					if randint(1, 100) <= fertility and randint(1, 4) < 4:
						if player.gender == Gender.Male:
							print(_("Your {partner} is pregnant with your baby!").format(partner=rel))
						else:
							print(_("You are pregnant with {name}'s baby!").format(name=player.partner.firstname))
						if yes_no(_("Would you like to keep it?")):
							if player.gender == Gender.Male:
								player.partner.is_pregnant = True
							else:
								player.is_pregnant = True
								player._recent_child_father = player.partner
					else:
						msg = _("You failed to get your {partner} pregnant.").format(partner=player.partner.name_accusative()) if player.gender == Gender.Male else _("You failed to get pregnant.")
						print(msg)
				else:
					print(_("Your {partner} doesn't want to have a baby with you.").format(partner=player.partner.name_accusative()))
					player.partner.change_relationship(-randint(4, 8))
			elif choice == _("Break up"):
				partner = player.partner.name_accusative()
				if yes_no(
					_("Are you sure you want to break up with your {partner}?").format(
						partner=partner
					)
				):
					print(
						_("You broke up with your {partner}.").format(partner=partner)
					)
					player.lose_partner()
			elif choice == _("Propose"):
				partner = player.partner
				name = partner.name_accusative()
				if (
					partner.years_together >= randint(3, 8 - partner.craziness // 20)
					and not partner.was_proposed_to
					and partner.relationship >= randint(50, 60) + randint(0, 40)
				):
					print(
						_("Your {partner} accepted your proposal!").format(partner=name)
					)
					partner.status = 1
					partner.change_relationship(randint(20, 50))
				else:
					print(
						_("Your {partner} rejected your proposal.").format(partner=name)
					)
					if not partner.was_proposed_to:
						player.change_happiness(-randint(3, 8))
						partner.change_relationship(-randint(4, 9))
						partner.was_proposed_to = True
			elif choice == _("Call off the engagement"):
				partner = player.partner.name_accusative()
				if yes_no(
					_("Are you sure you want to call off your engagement with your {partner}?").format(
						partner=partner
					)
				):
					print(
						_("You called off your engagement with your {partner}.").format(partner=partner)
					)
					player.partner.status = 0
					player.partner.change_relationship(-15)
			elif choice == _("Plan the wedding"):
				locations = {
					TranslateMarker("golf course"): 15300,
					TranslateMarker("vineyard"): 15300,
					TranslateMarker("family member's house"): 255,
					TranslateMarker("courthouse"): 51,
					TranslateMarker("restaurant"): 5100,
					TranslateMarker("drive-thru wedding chapel"): 255,
					TranslateMarker("country club"): 15300
				}
				places = list(locations.keys())
				choices = random.sample(places, 4)
				while True:
					print(_("Choose a location:"))
					choice = choice_input(*(list(map(lambda a: str(a).capitalize(), choices)) + ["Cancel"]))
					if choice <= len(choices):
						location = choices[choice - 1]
						price = locations[location]
						print(_("You have chosen to marry {name} at a {place}.\nCost: ${price}").format(name=relation.name, place=location, price=price))
						choice = choice_input(_("Do it"), _("Edit the plan"), _("Actually, never mind"))
						if choice == 1:
							if player.money < price:
								print(_("You don't have enough money for this wedding plan."))
							else:
								player.money -= price
								print(_("You married {name} at a {place}.").format(name=relation.name, place=location))
								player.change_happiness(randint(10, 16))
								relation.change_relationship(randint(30, 50))
								relation.status = 2
							break
						elif choice == 3:
							break
					else:
						break
			elif choice == _("Divorce"):
				partner = player.partner.name_accusative()
				if yes_no(_("Are you sure you want to divorce your {partner}?").format(partner=partner)):
					print(
						_("You divorced your {partner}.").format(partner=partner)
					)
					amount = round(player.money * random.uniform(0.4, 0.6)) 
					if amount > 0:
						player.change_happiness(-randint(10, 15))
						display_event(_("The judge has ordered you to pay {name} ${amount} to settle your divorce.").format(name=relation.name, amount=amount))
						player.money -= amount
					player.lose_partner()
			print()
	if choice == _("Activities"):	
		activities_menu(player)			
	if choice == _("School"):
		print(_("School Menu"))
		print()
		display_bar(_("Grades"), player.grades)
		choice = choice_input(_("Back"), _("Study harder"), _("Drop out"), _("Skip school"))
		clear_screen()
		if choice == 2:
			print(_("You began studying harder"))
			if not player.studied:
				player.change_grades(randint(5, 7 + (100 - player.grades) // 5))
				player.change_smarts(randint(0, 2) + (player.has_trait("NERD")))
				if randint(1, 2500) <= player.smarts:
					player.learn_trait("NERD")
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
		if choice == 4:
			#Skip school
			place = random.choice(SPEND_TIME_PLACES)
			display_event(_("You skipped school and went {place} instead.").format(place=place), cls=False)
			player.change_smarts(-2)
			player.change_grades(-randint(4, 8))
			if player.uv_years == 0 and one_in(5): #Can't get caught while in university
				display_event(_("You were caught skipping school!\nYou were sent to the principal's office and got detention."))
				player.change_happiness(-randint(15, 25))
				player.change_karma(-randint(1, 6))
			elif not player.skipped_school:
				player.change_happiness(randint(3, 7))
				player.change_karma(-randint(1, 6))
			player.skipped_school = True
				
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
				print()
				print(_("The below stats only matter if you have a job:"))
				display_data(_("Stress"), player.stress)
				display_data(_("Performance"), player.performance)
				print()
				choice = choice_input(
					_("Back"),
					_("Modify Happiness"),
					_("Modify Health"),
					_("Modify Smarts"),
					_("Modify Looks"),
					_("Modify Karma"),
					_("Modify Stress"),
					_("Modify Performance"),
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
				elif choice == 7:
					print(_("What would you like to set Stress to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						player.stress = val
				elif choice == 8:
					print(_("What would you like to set Performance to? (0-100)"))
					val = int_input_range_optional(0, 100)
					if val is not None:
						player.performance = val
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
		salary = round_stochastic(
			randexpo(30000, 65000)
		)  # TODO: Add a selection of different types of jobs
		if yes_no(
			_(
				"You found a job with a salary of ${salary:,}. Would you like to apply?"
			).format(salary=salary)
		):
			m = 100 + round_stochastic((salary - 40000) / 300)
			mod = (
				50 - player.smarts
			)  # Mod is inverted because we want to roll 100 OR LOWER to get the job
			if randint(1, 3) == 1:
				mod += round((50 - player.karma) / 2)
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
		print_align_bars(
			(_("Stress"), player.stress), (_("Performance"), player.performance)
		)
		display_data(_("Hours"), player.job_hours)
		can_retire = player.years_worked >= 10 and player.age >= 65
		choice = choice_input(
			_("Back"),
			_("Work Harder"),
			_("Retire") if can_retire else _("Quit Job"),
			_("Adjust Hours"),
			_("Request a Raise")
		)
		if choice == 2:
			print("You worked harder.")
			if not player.worked_harder:
				player.change_performance(randint(1, 10))
				player.change_stress(4)
				if player.has_trait("LAZY"):
					player.change_stress(6)
				player.worked_harder = True
		elif choice == 3:
			if can_retire:
				pension = player.calc_pension()
				if yes_no(
					_(
						"Do you want to retire? You will receive a yearly pension of ${pension}"
					).format(pension=pension)
				):
					player.lose_job()
					player.salary = pension
					player.change_happiness(randint(25, 50))
					print(
						_(
							"You retired and are now receiving pension of ${pension}."
						).format(pension=pension)
					)
			elif yes_no(_("Are you sure you want to quit your job?")):
				player.lose_job()
				print(_("You quit your job."))
		elif choice == 4:
			print(_("What would you like to set your hours to? (38 - 70)"))
			player.update_hours(int_input_range(38, 70))
		elif choice == 5:
			if player.age - player.last_raise >= 10 and not player.asked_for_raise and player.performance >= randint(40, 120):
				print(_("Your request for a raise has been approved."))
				perc = round(randint(20, 85) / 10, 2)
				player.salary += round(player.salary * perc/100)
				display_event(_("You got a raise of {perc}%").format(perc=perc))
				player.times_asked_since_last_raise = 0
				player.last_raise = player.age
			else:
				display_event(_("Your request for a raise has been rejected."))
				if player.times_asked_since_last_raise >= 2 and randint(1, 9) == 1:
					display_event(_("Your boss fired you for asking for a raise."))
					player.lose_job()
					player.change_happiness(-randint(25, 35))
				player.times_asked_since_last_raise += 1
			player.asked_for_raise = True
	elif choice == _("View Saved Games"):
		players = list(filter(lambda p: p["ID"] != player.ID, get_saves()))
		if not players:
			print(_("No previously saved games"))
		else:
			print(_("Previously saved games:"))
			choices = list(map(lambda p: p["name"], players))
			choices.append(_("Back"))
			choice = choice_input(*choices)
			clear_screen()
			if choice < len(choices):
				d = players[choice - 1]
				print(d["name"] + "\n")
				choice = choice_input(_("Back"), _("Load Save"), _("Delete Save"))
				if choice == 2:
					if yes_no(_("Would you like to load this save?")):
						player.save_game()
						player.__init__()  # Re-initialize in preparation for loading a save
						player.__dict__.update(d)
						clear_screen()
				elif choice == 3:
					if yes_no(_("Are you sure you want to delete this save?")):
						os.remove(d["save_path"])
