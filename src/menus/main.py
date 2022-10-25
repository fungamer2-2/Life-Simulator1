import random
from random import randint

from src.lifesim_lib.const import *
from src.lifesim_lib.translation import _
from src.lifesim_lib.lifesim_lib import *
from src.people.classes.parent import Parent
from src.people.classes.person import Person
from src.people.classes.sibling import Sibling
from src.people.classes.partner import Partner

def main_menu(player):
	print()
	display_data(_("Your name"), player.name)
	if player.traits:
		display_data(_("Traits"), player.get_traits_str())
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
			elif isinstance(relation, (Sibling, Partner)):
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
					choices.append(_("Have a conversation"))
				if player.age >= 6:
					choices.append(_("Compliment"))
					choices.append(_("Insult"))
				if isinstance(relation, Partner):
					if relation.status < 2:
						choices.append(_("Break up"))
					else:
						choices.append(_("Divorce"))
					if relation.status == 0:
						choices.append(_("Propose"))
					elif relation.status == 1:
						choices.append(_("Plan the Wedding"))
			choice = choice_input(*choices, return_text=True)
			clear_screen()
			if choice == _("Spend time"):
				if relation.relationship < 15:
					print(_("Your {relation} refused to see you."))
					player.change_happiness(-4)
				else:
					enjoyment1 = max(randint(0, 70), randint(0, 70)) + randint(0, 30)
					if player.has_trait("CHEERFUL"):
						enjoyment1 = max(enjoyment1, randint(0, 100))
					elif player.has_trait("GRUMPY"):
						enjoyment1 = min(enjoyment1, randint(0, 100))
					if player.age >= 1 and player.age < 3:
						sayings = [
							_("You did some finger-painting with your {relation}.").format(relation=relation.name_accusative()),
							_("You played in the mud with your {relation}.").format(relation=relation.name_accusative()),
							_("You and your {relation} drew in your colouring book together").format(relation=relation.name_accusative()),
							_("You and your {relation} squished clay between your fingers.").format(relation=relation.name_accusative()),
							_("You and your {relation} drew with your large crayons.").format(relation=relation.name_accusative()),
							_("You and your {relation} played with your toys together.").format(relation=relation.name_accusative()),
							_("You and your {relation} played with your blocks.").format(relation=relation.name_accusative()),
							_("You and your {relation} played in your sandbox.").format(relation=relation.name_accusative()),
							_("You and your {relation} played with your stuffed animals.").format(relation=relation.name_accusative()),
							_("Your {relation} pushed you on your toddler swing.").format(relation=relation.name_accusative()),
							_("Your {relation} played with you and your toys.").format(relation=relation.name_accusative()),
							_("Your {relation} played with you.").format(relation=relation.name_accusative()),
							_("Your {relation} raced you around the house.").format(relation=relation.name_accusative()),
							_("Your {relation} tickled you until you giggled.").format(relation=relation.name_accusative()),
							_("You and your {relation} went to the park.").format(relation=relation.name_accusative()),
							_("You and your {relation} went to the shops.").format(relation=relation.name_accusative()),
							
						]
						print(random.choice(sayings))
					if player.age >= 3:
						sayings = [
							_("You took your {relation} shopping a flea market.").format(relation=relation.name_accusative()),
							_("You took your {relation} bowling.").format(relation=relation.name_accusative()),
							_("You took your {relation} to the beach.").format(relation=relation.name_accusative()),
							_("You took your {relation} to play golf.").format(relation=relation.name_accusative()),
							_("You took your {relation} to get cornrow braids.").format(relation=relation.name_accusative()),
							_("You took your {relation} to do some gardening.").format(relation=relation.name_accusative()),
							_("You took your {relation} to a pilates class.").format(relation=relation.name_accusative()),
							_("You took your {relation} to play catch.").format(relation=relation.name_accusative()),
							_("You took your {relation} to make homemade mini pizzas.").format(relation=relation.name_accusative()),
							_("You took your {relation} to perform in a flashmob at the courthouse.").format(relation=relation.name_accusative()),
							_("You took your {relation} to do a puzzle at the library.").format(relation=relation.name_accusative()),
							_("You took your {relation} to relax while floating in a natural hot spring.").format(relation=relation.name_accusative()),
							_("You took your {relation} crocheting.").format(relation=relation.name_accusative()),
						]
						print(random.choice(sayings))
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
					agreement = random.triangular(0, 100, 65)
					agreement += randint(0, max(0, (relation.relationship - 50) // 3))
					if isinstance(relation, Sibling) and randint(1, 2) == 1:
						agreement -= randint(0, relation.petulance // 3)
					agreement = clamp(
						round(agreement), randint(0, 10), randint(90, 100)
					)
					chats = random.choice(CHATS)
					discussions = random.choice(DISCUSSIONS)
					talks = random.choice(TALKS)
					heart_to_hearts = (HEART_TO_HEARTS)
					if player.age >= 3:
						sayings = [
							_("You and your {relation} had a chat about the hierarchy of licorice.").format(relation=relation.name_accusative()),
							_("You and your {relation} had a chat about {chats}.").format(relation=relation.name_accusative()),
							_("You and your {relation} had a chat about which is better, Star Wars or Star Trek.").format(relation=relation.name_accusative()),
							_("You and your {relation} had a chat about which is better, Coke or Pepsi.").format(relation=relation.name_accusative()),
							_("You and your {relation} had a chat about which is better, Lord of the Rings or Harry Potter.").format(relation=relation.name_accusative()),
							_("You and your {relation} had a chat about who is better, the Red Sox or Yankees.").format(relation=relation.name_accusative()),
							_("You and your {relation} discussed Frida Kahlo's moustache.").format(relation=relation.name_accusative()),
							_("You and your {relation} discussed {discussions}.").format(relation=relation.name_accusative()),
							_("You and your {relation} discussed which is the best breed of dog.").format(relation=relation.name_accusative()),
							_("You and your {relation} discussed which is the best breed of cat.").format(relation=relation.name_accusative()),
							_("You and your {relation} discussed why dogs are better than cats.").format(relation=relation.name_accusative()),
							_("You and your {relation} discussed why cats are better than dogs.").format(relation=relation.name_accusative()),
							_("You and your {relation} talked about whether you would rather have overly large hands or small feet.").format(relation=relation.name_accusative()),
							_("You and your {relation} talked about {talks}.").format(relation=relation.name_accusative()),
							_("You and your {relation} talked about who will win the Monaco Grand Prix.").format(relation=relation.name_accusative()),
							_("You and your {relation} Had a heart-to-heart about the best gift you ever received.").format(relation=relation.name_accusative()),
							_("You and your {relation} Had a heart-to-heart about {heart_to_hearts}.").format(relation=relation.name_accusative()),
						]
						print(random.choice(sayings))
					display_bar(_("Agreement"), agreement)
					if not relation.had_conversation:
						player.change_happiness(8 if player.has_trait("CHEERFUL") else 4)
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
				relationship = relation.relationship
				if relationship >= randint(51, 100):
					appreciation = max(appreciation, randint(0, 60) + randint(0, 40))
					if relationship >= randint(75, 120):
						appreciation = max(appreciation, randint(0, 60) + randint(0, 40))
				elif relationship <= randint(0, 49):
					appreciation = min(appreciation, randint(0, 60) + randint(0, 40))
					if relationship <= randint(0, 25):
						appreciation = min(appreciation, randint(0, 60) + randint(0, 40))
				compliment = random.choice(COMPLIMENTS)
				print(
					_("You told your {relation} that {hes_shes} {compliment}.").format(
						relation=relation.name_accusative(),
						hes_shes=relation.hes_shes(),
						compliment=compliment
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
					if randint(1, 300) <= round_stochastic(appreciation * relation.relationship / 50):
						compliment = random.choice(COMPLIMENTS)
						display_event(
							_("Your {relation} told you that you're {compliment}!").format(
								relation=relation.name_accusative(),
								compliment=compliment
							)
						)
						player.change_happiness(randint(6, 10) - (3*(player.has_trait("GRUMPY"))))
						if player.has_trait("CHEERFUL"):
							player.change_happiness(4)
						if randint(1, 6) == 1:
							relation.change_relationship(randint(5, 25))
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
			elif choice == _("Break up"):
				partner = player.partner.name_accusative()
				if yes_no(_("Are you sure you want to break up with your {partner}?").format(partner=partner)):
					print(_("You broke up with your {partner}.").format(partner=partner))
					player.lose_partner()
			elif choice == _("Propose"):
				partner = player.partner
				name = partner.name_accusative()
				if partner.years_together >= randint(3, 4) and not partner.was_proposed_to and partner.relationship >= randint(50, 60) + randint(0, 40):
					print(_("Your {partner} accepted your proposal!").format(partner=name))
					partner.status = 1
					partner.change_relationship(randint(20, 50))
				else:
					print(_("Your {partner} rejected your proposal.").format(partner=name))
					if not partner.was_proposed_to:
						player.change_happiness(-randint(3, 8))
						partner.change_relationship(-randint(4, 9))
						partner.was_proposed_to = True
			elif choice == _("Plan the Wedding"):
				print(_("Coming soon..."))
			print()
	if choice == _("Activities"):
		print(_("Activities Menu"))
		print()
		choices = [_("Back")]
		if 1 <= player.age < 13:
			choices.append(_("Play with your toys"))
		if player.age >= 4:
			choices.append(_("Doctor"))
		if player.age >= 1:
			choices.append(_("Arts and Crafts"))
		if player.age >= 12:
			choices.append(_("Meditate"))
			choices.append(_("Library"))
			choices.append(_("Gym"))
			choices.append(_("Listen to music"))
		if player.age >= 18:
			choices.append(_("Lottery"))
			if player.marital_status == 0: 
				choices.append(_("Find a Partner"))
		choices.append(_("Surrender"))
		choice = choice_input(*choices, return_text=True)
		clear_screen()
		if choice == _("Play with your toys"):
			if player.is_depressed():
				print(_("You don't feel like playing, but you decide to try anyway."))
				happy_gain = randint(0, 6)
				if player.has_trait("CHEERFUL"):
					happy_gain += 2
			else:
				happy_gain = randint(5, 10)
				if player.has_trait("CHEERFUL"):
					happy_gain += 5
				if player.age < 3:
					sayings = [
						_("You played with your toys."),
						_("You had a lot of fun playing with your toys."),
						_("You played with your toy wagon."),
						_("You played with some of your balls."),
						_("You raced around on your foot propelled bike."),
						_("You played with your push-pull toy."),
						_("You put toys in your wagon and pulled them around the living room."),
						_("You swung on your toddler swing."),
						_("You slid on your toddler slide."),
						_("You played with your stacking toys."),
						_("You played with your nesting toys."),
						_("You played with your shape sorter."),
						_("You played with your pop-up toys."),
						_("You played with your puzzle with knobs."),
						_("You played with your blocks."),
						_("You played in your sandbox."),
						_("You played with your sandbox toys."),
						_("You played in your wading pool."),
						_("You played with your wading pool toys"),
						_("You played with your bath toys."),
						_("Your mum gave you a bath and you played with your bath toys."),
						_("Your dad gave you a bath and you played with your bath toys."),
						_("You played with your stuffed animals."),
						_("You played with your dolls."),
						_("You played with your play vehicles."),
						_("You played with your toy kitchen equipment."),
						_("You played with your toy kitchen gadgets."),
						_("You played with your toy telephone."),
						_("You played with your toy lawn mower."),
						_("You played with your toy shopping cart."),
						_("You played with your toy workbench."),
						_("You played in your playhouse."),
						_("You pretended to hold a meeting at your toy table and chairs with your stuffed animals."),
						_("You made a sausage out of clay."),
						_("You made a a ball out of clay."),
						_("You played with your playdough."),
						_("You played with your toy guitar."),
						_("You played with your toy piano."),
					]
					print(random.choice(sayings))
				if player.age >= 3 and player.age < 6:
					sayings = [
						_("You played with your toys."),
						_("You had a lot of fun playing with your toys."),
						_("You played with your toy wagon."),
						_("You played with some of your balls."),
						_("You played with your push-pull toy."),
						_("You put toys in your wagon and pulled them around the living room."),
						_("You swung on your toddler swing."),
						_("You slid on your toddler slide."),
						_("You played with your stacking toys."),
						_("You played with your nesting toys."),
						_("You played with your shape sorter."),
						_("You played with your pop-up toys."),
						_("You played with your puzzle with knobs."),
						_("You played with your blocks."),
						_("You played in your sandbox."),
						_("You played with your sandbox toys."),
						_("You played in your wading pool."),
						_("You played with your wading pool toys"),
						_("You played with your bath toys."),
						_("Your mum gave you a bath and you played with your bath toys."),
						_("Your dad gave you a bath and you played with your bath toys."),
						_("You played with your stuffed animals."),
						_("You played with your dolls."),
						_("You played with your play vehicles."),
						_("You played with your toy kitchen equipment."),
						_("You played with your toy kitchen gadgets."),
						_("You played with your toy telephone."),
						_("You played with your toy lawn mower."),
						_("You played with your toy shopping cart."),
						_("You played with your toy workbench."),
						_("You played in your playhouse."),
						_("You pretended to hold a meeting at your toy table and chairs with your stuffed animals."),
						_("You made a rough pot of clay."),
						_("You made a rough bowl out of clay."),
						_("You played with your playdough."),
						_("You played with your toy guitar."),
						_("You played with your toy piano."),
						_("You kicked a ball in your yard."),
						_("You fed your baby doll."),
						_("You changed the daiper on your baby doll."),
						_("You bathed your baby doll."),
						_("You put your mum's clothes on and dressed up as her."),
						_("You put your dad's clothes on and dressed up as him."),
						_("You climbed on your climbing gym."),
						_("You dressed up your stuffed animals."),
						_("You changed your doll's clothes."),
						_("You played with your chalk."),
						_("You rode your tricycle."),
						_("You read a storybook."),
						_("You played with your finger puppets."),
						_("You played with your hand puppet."),
						_("You played a simple board game."),
						_("You played a word matching game."),
						_("You played a picture matching game."),
						_("You played make believe with a cardboard box."),
						_("You made a fort using bed sheets and cushions."),
					]
					print(random.choice(sayings))
				if player.age >= 6 and player.age < 10:
					sayings = [
						_("You played with your toys."),
						_("You had a lot of fun playing with your toys."),
						_("You played with some of your balls."),
						_("You played with your Lego."),
						_("You played with your stuffed animals."),
						_("You played with your dolls."),
						_("You played with your toy cars."),
						_("You kicked a ball in your yard."),
						_("You fed your baby doll."),
						_("You changed the daiper on your baby doll."),
						_("You bathed your baby doll."),
						_("You put your mum's clothes on and dressed up as her."),
						_("You put your dad's clothes on and dressed up as him."),
						_("You climbed on your climbing gym."),
						_("You dressed up your stuffed animals."),
						_("You changed your doll's clothes."),
						_("You played with your chalk and drew on the sidewalk."),
						_("You rode your tricycle."),
						_("You read a storybook."),
						_("You played with your finger puppets."),
						_("You played with your hand puppet."),
						_("You played a board game."),
						_("You played a word game."),
						_("You played a video game."),
						_("You made a costume out of a cardboard box."),
						_("You made a fort using bed sheets and cushions."),
						_("You rode your bicycle."),
						_("You played with some gym equipment."),
						_("You played with your baseball glove."),
						_("You played with your hockey stick."),
						_("You played with your tennis racquet."),
						_("You played tennis with your family."),
						_("You played football with your friends."),
						_("You walked on your stilts."),
						_("You skated on your ice skates."),
						_("You skated on your roller blades."),
						_("You skated on your skateboard."),
						_("You rode your scooter."),
						_("You rode your pogo stick."),
						_("You played with your jump rope."),
						_("You made a paper aeroplane."),
						_("You played with your action figures."),
						_("You played with your train set."),
						_("You played with your magic set."),
						_("You played with your craft kit."),
						_("You played with your science set."),
						_("You painted a basic picture."),
						_("You played tabletop sports."),
						_("You played with a jigsaw puzzle."),
						_("You played with your fashion dolls."),
						_("You played with your career dolls."),
						_("You played with your dollhouse."),
						_("You played with your puppets."),
						_("You played with your toy theatre."),
						_("You played with your marionettes."),
						_("You read a fairytale and imagined you were in it."),
					]
					print(random.choice(sayings))
				if player.age >= 10 and player.age < 13:
					sayings = [
						_("You played with your toys."),
						_("You had a lot of fun playing with your toys."),
						_("You played with some of your balls."),
						_("You played with your Lego."),
						_("You played with your stuffed animals."),
						_("You played with your dolls."),
						_("You played with your toy cars."),
						_("You kicked a ball in your yard."),
						_("You dressed up your stuffed toys."),
						_("You played with your chalk and drew on the sidewalk."),
						_("You read a storybook."),
						_("You played with your finger puppets."),
						_("You played with your hand puppet."),
						_("You played a board game."),
						_("You played a word game."),
						_("You played a video game."),
						_("You made a fort using bed sheets and cushions, and slept in it."),
						_("You rode your bicycle."),
						_("You played with some gym equipment."),
						_("You played baseball with your friends."),
						_("You played hockey with your friends."),
						_("You played tennis with your friends."),
						_("You played tennis with your family."),
						_("You played with your football."),
						_("You played football with your friends."),
						_("You walked on your stilts."),
						_("You skated on your ice skates."),
						_("You went ice skating with your friends."),
						_("You skated on your roller blades."),
						_("You went roller blading with your friends."),
						_("You skated on your skateboard."),
						_("You went skateboarding with your friends."),
						_("You rode your scooter."),
						_("You rode your pogo stick."),
						_("You played with your jump rope."),
						_("You played jump rope with your friends."),
						_("You played with your basketball."),
						_("You played basketball with your friends."),
						_("You played with your netball."),
						_("You played netball with your friends."),
						_("You made a paper aeroplane."),
						_("You played with your action figures."),
						_("You played with your train set."),
						_("You played with your magic set."),
						_("You played with your craft kit."),
						_("You played with your science set."),
						_("You painted a picture."),
						_("You played tabletop sports."),
						_("You completed a jigsaw puzzle."),
						_("You played with your fashion dolls."),
						_("You played with your career dolls."),
						_("You played with your puppets."),
						_("You played with your toy theatre."),
						_("You played with your marionettes."),
						_("You read a story and imagined you were in it."),
						_("You played chess with a friend."),
						_("You played foosball with a friend."),
						_("You played darts with a friend."),
						_("You played with your RC car."),
						_("You played with your drone."),
						_("You read a mystery book."),
						_("You read an adventure book."),
						_("You played checkers with a friend."),
						_("You played solitaire with a pack of cards."),
						_("You played dominoes with some friends."),
						_("You made a robot with Meccano"),
					]
					print(random.choice(sayings))
				if not player.played:
					player.played = True
					player.change_happiness(happy_gain)
		elif choice == _("Arts and Crafts"):
			if randint(1, 10) == 1:
				print(_("You thought about doing arts and crafts, but couldn't decide what to make."))
				player.change_happiness(-randint(1, 3))
			else:
				happy_gain = randint(2, 6)
				if player.has_trait("CHEERFUL"):
						player.change_happiness(randint(1, 3))
				if player.has_trait("NERD"):
						player.change_smarts(randint(2, 3))
				if player.has_trait("GENIUS"):
						player.change_smarts(randint(3, 4))
				if player.age >= 1 and player.age < 3:
					sayings = [
						_("You decided to finger-paint."),
						_("You decided to make something from mud!"),
						_("You drew in your colouring book"),
						_("You squished clay between your fingers."),
						_("You drew with your large crayons."),
					]
					print(random.choice(sayings))
				if player.age >= 3 and player.age < 6:
					sayings = [
						_("You decided to draw."),
						_("You decided to make something from clay!"),
						_("You decided to finger-paint."),
						_("You played with your crayons."),
						_("You drew in your colouring book."),
						_("You drew a house that looked like a triangle on top of a square."),
						_("You drew a stick figure picture of your family."),
					]
					print(random.choice(sayings))
				if player.age >= 6 and player.age < 10:
					sayings = [
						_("You decided to draw."),
						_("You decided to make something from clay!"),
						_("You decided to finger-paint."),
						_("You drew with your crayons."),
						_("You drew in your colouring book."),
						_("You tried to draw a picture of your house."),
						_("You tried to draw a picture of your family."),
						_("You tried to draw a picture of a landscape."),
						_("You tried to draw a picture of a cat."),
						_("You tried to draw a picture of a bowl of fruit."),
						_("You tried to draw your favourite cartoon character."),
					]
					print(random.choice(sayings))	
				if player.age >= 10 and player.age < 13:
					sayings = [
						_("You decided to draw."),
						_("You decided to make something from clay!"),
						_("You decided to finger-paint."),
						_("You drew with your crayons."),
						_("You drew in your colouring book."),
						_("You drew a picture of your house."),
						_("You drew a picture of your family."),
						_("You drew a picture of a landscape."),
						_("You drew a picture of a cat."),
						_("You drew a picture of a bowl of fruit."),
						_("You drew your favourite cartoon character."),
						_("You tried to paint a picture of your house."),
						_("You tried to paint a picture of your family."),
						_("You tried to paint a picture of a landscape."),
						_("You tried to paint a picture of a cat."),
						_("You tried to paint a picture of a bowl of fruit."),
					]
					print(random.choice(sayings))
				if player.age >= 13 and player.age < 16:
					sayings = [
						_("You decided to draw."),
						_("You decided to make something from clay!"),
						_("You decided to finger-paint."),
						_("You drew with charcoal."),
						_("You drew a picture of your house."),
						_("You drew a picture of your family."),
						_("You drew a picture of a landscape."),
						_("You drew a picture of a cat."),
						_("You drew a picture of a bowl of fruit."),
						_("You drew your favourite cartoon character."),
						_("You painted a picture of your house."),
						_("You painted a picture of your family."),
						_("You painted a picture of a landscape."),
						_("You painted a picture of a cat."),
						_("You painted a picture of a bowl of fruit."),
					]
					print(random.choice(sayings))

					if not player.did_arts_and_crafts:
						player.change_happiness(randint(2, 4))
						player.change_smarts(randint(1, 2))
					else:
						print(_("You decided to bake something tasty!"))
					if not player.did_arts_and_crafts:
						player.change_happiness(randint(3, 6))
						player.change_smarts(randint(0, 3)) 
				if not player.did_arts_and_crafts:
					if player.has_trait("CHEERFUL"):
						player.change_happiness(3)
					if player.has_trait("NERD"):
						player.change_smarts(randint(0, 2))
				player.did_arts_and_crafts = True
		elif choice == _("Listen to music"):
			print(_("You listened to some music."))
			if not player.listened_to_music:
				player.change_happiness(randint(4, 8) + 3 * player.has_trait("CHEERFUL"))
				player.change_health(randint(0, 2))
				player.change_stress(-randint(1, 7))
				player.change_smarts(randint(0, 1 + player.has_trait("NERD")))
				player.listened_to_music = True
		elif choice == _("Find a Partner"):
			if player.date_options <= 0:
				print(_("You are unable to find anyone to ask on a date."))
			else:
				partner = player.generate_partner()
				string = _("a male") if partner.gender == Gender.Male else _("a female")
				print(_("You met {a_male_female} named {name}.").format(a_male_female=string, name=partner.name))
				partner.print_info()
				him_her = partner.him_her()
				hes_shes = partner.hes_shes()
				choice = choice_input(
					_("Ask {him_her} out").format(him_her=him_her),
					_("No, {hes_shes} not my type").format(hes_shes=hes_shes)
				)
				if choice == 1:
					if partner.compatibility_check(player):
						print(_("You are now dating {name}.").format(name=partner.name))
						player.change_happiness(randint(15, 20))
						player.partner = partner
						player.relations.append(partner)
					else:
						print(_("{name} rejected you.").format(name=partner.name))
						player.change_happiness(-randint(2, 4))
				player.date_options -= 1
		elif choice == _("Doctor"):
			has_fee = player.age >= 18
			if has_fee:
				visit = yes_no(_("Would you like to visit the doctor? ($100 consultation fee)"))
			else:
				visit = yes_no(_("Would you like to visit the doctor?"))
			if visit:
				if has_fee and player.money < 100:
					print(_("You don't have enough money."))
				else:
					if has_fee:
						player.money -= 100
					if len(player.illnesses) == 0:
						print(_("The doctor has determined that you are not suffering from any illnesses."))
					else:
						print(_("The doctor has determined that you are currently suffering from the following:"))
						s = [ILLNESSES_TRANSLATIONS.get(name, name) for name in player.illnesses]
						print(", ".join(s))
						options = ["Back"]
						options.extend(_("Treat {illness}").format(illness=n) for n in s)
						choice = choice_input(*options)
						if choice > 1:
							was_cured = False
							illness = player.illnesses[choice - 2]
							if illness == "Depression":
								was_cured = randint(1, 4) == 1 and player.happiness >= randint(20, 35)
								if was_cured:
									player.change_health(randint(4, 8))
									player.change_happiness((100 - player.happiness)//2)
							elif illness == "High Blood Pressure":
								was_cured = player.stress < randint(65, 85) and randint(1, 3) == 1
								if was_cured:
									player.change_health(randint(4, 8))
									player.change_happiness(randint(3, 6))
							print(_("You were treated for your {illness}.").format(illness=illness))
							if was_cured:
								display_event(_("You are no longer suffering from {illness}.").format(illness=illness))
								player.remove_illness(illness)
							else:
								player.change_health(randint(3, 5))
								player.change_happiness(randint(3, 5))
								display_event(_("You continue to suffer from {illness}.").format(illness=illness))
		elif choice == _("Meditate"):
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
				if player.has_trait("CHEERFUL"):
					player.change_happiness(4)
				player.meditated = True
				player.times_meditated += 1
		elif choice == _("Library"):
			print(_("You went to the library."))
			enjoyment = randint(15, 65)
			if player.has_trait("CHEERFUL"):
				enjoyment = max(enjoyment, randint(15, 65))
			elif player.has_trait("GRUMPY"):
				enjoyment = min(enjoyment, randint(15, 65))
			if player.has_trait("GENIUS"):
				enjoyment += randint(5, 20)
			elif player.has_trait("NERD"):
				enjoyment += randint(0, 15)
			display_bar(_("Your Enjoyment"), enjoyment)
			if not player.visited_library:  # You can only get the bonus once per year
				player.change_happiness(round_stochastic(enjoyment/15))
				if player.has_trait("CHEERFUL"):
					player.change_happiness(3)
				player.change_smarts(randint(2, 5))
				if player.has_trait("GENIUS"):
					player.change_smarts(5)
				elif player.has_trait("NERD"):
					player.change_smarts(3)
				player.visited_library = True
		elif choice == _("Gym"):
			if player.health < 10:
				print(_("Your health is too weak to visit the gym."))
			else:
				enjoyment = randint(35, 80)
				if randint(1, 3) == 1:
					enjoyment += randint(10, 20)
				print(_("You worked out at the gym."))
				display_bar(_("Your Enjoyment"), enjoyment)
				if not player.worked_out:
					player.change_happiness(round_stochastic(enjoyment / 12))
					if player.has_trait("CHEERFUL"):
						player.change_happiness(3)
					player.change_health(randint(3, 6))
					if player.looks < randint(1, 100) and randint(1, 100) <= 70:
						player.change_looks(randint(2, 4))
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
				player.change_smarts(randint(0, 2) + (player.has_trait("NERD")))
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
					_("Modify Performance")
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
		salary = round_stochastic(randexpo(30000, 55000)) #TODO: Add a selection of different types of jobs
		if yes_no(_("You found a job with a salary of ${salary:,}. Would you like to apply?").format(salary=salary)):
			m = 100 + round_stochastic((salary-40000)/300)
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
		print_align_bars(
			(_("Stress"), player.stress),
			(_("Performance"), player.performance)
		)
		can_retire = player.years_worked >= 10 and player.age >= 65
		choice = choice_input(_("Back"), _("Work Harder"), _("Retire") if can_retire else _("Quit Job"))
		if choice == 2:
			print("You worked harder.")
			if not player.worked_harder:
				player.change_performance(randint(1, 10))
				player.change_stress(4)
				if player.has_trait("LAZY"):
					player.change_stress(6)
				player.worked_harder = True
		if choice == 3:
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
						player.__init__() #Re-initialize in preparation for loading a save
						player.__dict__.update(d)
						clear_screen()
				elif choice == 3:
					if yes_no(_("Are you sure you want to delete this save?")):
						os.remove(d["save_path"])
