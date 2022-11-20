import random, time, math
from random import randint

from src.lifesim_lib.const import *
from src.lifesim_lib.translation import _
from src.lifesim_lib.lifesim_lib import *
from src.people.classes.child import Child

def activities_menu(player):
	selected = False
	while not selected:
		print(_("Activities Menu"))
		print()
		choices = [_("Back")]
		if 3 <= player.age < 13:
			choices.append(_("Play with your toys"))
		if player.age >= 4:
			choices.append(_("Doctor"))
		if player.age >= 5:
			choices.append(_("Arts and Crafts"))
		if player.age >= 6:
			choices.append(_("Mind & Body"))
		if player.age >= 12:
			choices.append(_("Listen to music"))
		if player.age >= 18:
			if player.age >= 21:
				choices.append(_("Adoption"))
			choices.append(_("Lottery"))
			choices.append(_("Plastic Surgery"))
			if player.marital_status == 0:
				choices.append(_("Find a Partner"))
		choices.append(_("Surrender"))
		choice = choice_input(*choices, return_text=True)
		clear_screen()
		if choice == _("Back"):
			selected = True
		elif choice == _("Play with your toys"):
			selected = True
			if player.is_depressed():
				print(_("You don't feel like playing, but you decide to try anyway."))
				happy_gain = randint(0, 6)
				if player.has_trait("CHEERFUL"):
					happy_gain += 2
			else:
				happy_gain = randint(5, 10)
				if player.has_trait("CHEERFUL"):
					happy_gain += 5
				sayings = [
					"You played with your toys.",
					"You had a lot of fun playing with your toys.",
				]
				if one_in(2):
					if player.age < 3:
						sayings = [
							_("You played with your toy wagon."),
							_("You played with some of your balls."),
							_("You raced around on your foot propelled bike."),
							_("You played with your push-pull toy."),
							_(
								"You put toys in your wagon and pulled them around the living room."
							),
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
							_(
								"Your mum gave you a bath and you played with your bath toys."
							),
							_(
								"Your dad gave you a bath and you played with your bath toys."
							),
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
							_(
								"You pretended to hold a meeting at your toy table and chairs with your stuffed animals."
							),
							_("You made a sausage out of clay."),
							_("You made a a ball out of clay."),
							_("You played with your playdough."),
							_("You played with your toy guitar."),
							_("You played with your toy piano."),
						]
					elif player.age < 6:
						sayings = [
							_("You played with your toy wagon."),
							_("You played with some of your balls."),
							_("You played with your push-pull toy."),
							_(
								"You put toys in your wagon and pulled them around the living room."
							),
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
							_(
								"Your mum gave you a bath and you played with your bath toys."
							),
							_(
								"Your dad gave you a bath and you played with your bath toys."
							),
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
							_(
								"You pretended to hold a meeting at your toy table and chairs with your stuffed animals."
							),
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
					elif player.age < 10:
						sayings = [
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
					else:
						sayings = [
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
							_(
								"You made a fort using bed sheets and cushions, and slept in it."
							),
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
			selected = True
			if player.age >= randint(5, 10) and one_in(10):
				sayings = [
					_(
						"You thought about doing arts and crafts, but couldn't decide what to make."
					),
					_("For some reason, you couldn't think of any ideas."),
					_(
						"You came up with a cool arts and crafts idea, only to quickly forget what it was."
					),
					_("You were unable to think of anything creative to do."),
					_(
						"You felt a bit frustrated when you couldn't come up with any creative ideas."
					),
				]
				print(random.choice(sayings))
				player.change_happiness(-randint(2, 4))
			else:
				if player.age < 3:
					sayings = [
						_("You decided to finger-paint."),
						_("You decided to make something from mud!"),
						_("You drew in your colouring book"),
						_("You squished clay between your fingers."),
						_("You drew with your large crayons."),
					]
				elif player.age < 6:
					sayings = [
						_("You decided to draw."),
						_("You decided to make something from clay!"),
						_("You decided to finger-paint."),
						_("You played with your crayons."),
						_("You drew in your colouring book."),
						_(
							"You drew a house that looked like a triangle on top of a square."
						),
						_("You drew a stick figure picture of your family."),
					]
				elif player.age < 10:
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
				elif player.age < 13:
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
				else:
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
					player.change_happiness(randint(2, 5))
					player.change_smarts(randint(1, 2))
					if player.has_trait("CHEERFUL"):
						player.change_happiness(3)
					if player.has_trait("NERD"):
						player.change_smarts(randint(0, 2))
			player.did_arts_and_crafts = True
		elif choice == _("Listen to music"):
			selected = True
			music_categories = [_("pop music"), _("rock music"), _("hip-hop"), _("latin music")]
			if one_in(2):
				print(_("You listened to some music."))
			else:
				sayings = [
					_("You listened to some {music_type}.").format(music_type=random.choice(music_categories)),
					_("You played your favorite song."),
					_("You listened to a song by {music_artist}.").format(music_artist=random.choice(MUSIC_ARTISTS))
				]
				print(random.choice(sayings))
			if not player.listened_to_music:
				player.change_happiness(
					randint(4, 8) + 3 * player.has_trait("CHEERFUL")
				)
				player.change_health(randint(0, 2))
				player.change_stress(-randint(1, 7))
				player.change_smarts(randint(0, 1 + player.has_trait("NERD")))
				player.listened_to_music = True
		elif choice == _("Find a Partner"):
			selected = True
			if player.date_options <= 0:
				print(_("You are unable to find anyone to ask on a date."))
			else:
				partner = player.generate_partner()
				string = _("a male") if partner.gender == Gender.Male else _("a female")
				print(
					_("You met {a_male_female} named {name}.").format(
						a_male_female=string, name=partner.name
					)
				)
				partner.print_info()
				him_her = partner.him_her()
				hes_shes = partner.hes_shes()
				choice = choice_input(
					_("Ask {him_her} out").format(him_her=him_her),
					_("No, {hes_shes} not my type").format(hes_shes=hes_shes),
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
			selected = True
			has_fee = player.age >= 18
			if has_fee:
				visit = yes_no(
					_("Would you like to visit the doctor? ($100 consultation fee)")
				)
			else:
				visit = yes_no(_("Would you like to visit the doctor?"))
			if visit:
				if has_fee and player.money < 100:
					print(_("You don't have enough money."))
				else:
					if has_fee:
						player.money -= 100
					if len(player.illnesses) == 0:
						print(
							_(
								"The doctor has determined that you are not suffering from any illnesses."
							)
						)
					else:
						print(
							_(
								"The doctor has determined that you are currently suffering from the following:"
							)
						)
						s = [
							ILLNESSES_TRANSLATIONS.get(name, name)
							for name in player.illnesses
						]
						print(", ".join(map(str, s)))
						options = ["Back"]
						options.extend(
							_("Treat {illness}").format(illness=n) for n in s
						)
						choice = choice_input(*options)
						if choice > 1:
							was_cured = False
							illness = player.illnesses[choice - 2]
							if illness == "Depression":
								was_cured = one_in(4) and player.happiness >= randint(20, 35)
								if was_cured:
									player.change_health(randint(4, 8))
									player.change_happiness(
									   (100 - player.happiness) // 2
									)
							elif illness == "High Blood Pressure":
								was_cured = player.stress < randint(50, 80) and one_in(3)
								if was_cured:
									player.change_health(randint(4, 8))
									player.change_happiness(randint(3, 6))
							elif illness == "Common Cold":
								was_cured = True
								player.change_health(randint(4, 6))
								player.change_happiness(randint(4, 7))
							elif illness == "Flu":
								was_cured = True
								player.change_health(randint(5, 6))
								player.change_happiness(randint(4, 8))
							elif illness == "Cancer":
								was_cured = one_in(20) and randint(1, 100) <= player.health
								if was_cured:
									player.change_health(randint(30, 50))
									player.change_happiness(randint(20, 40))
								else:
									player.change_health(randint(5, 9))
									player.change_happiness(randint(3, 7))
							print(
								_("You were treated for your {illness}.").format(
									illness=illness
								)
							)
							n = str(illness)
							if illness in ["Common Cold", "Flu"]:
								n = _("the {n}").format(n=n)
							n = n.lower()
							if was_cured:
								display_event(
									_(
									   "You are no longer suffering from {illness}."
									).format(illness=n)
								)
								player.remove_illness(illness)
							else:
								player.change_health(randint(3, 5))
								player.change_happiness(randint(3, 5))
								display_event(
									_("You continue to suffer from {illness}.").format(
									   illness=n
									)
								)
		elif choice == _("Mind & Body"):
			print(_("Mind & Body"))
			print()
			choices = [_("Back")]
			if player.age >= 12:
				choices.extend([
					_("Meditate"),
					_("Gym"),
					_("Library")
				])
			choices.append(_("Read a Book"))
			choice = choice_input(*choices, return_text=True)
			clear_screen()
			if choice != _("Back"):
				selected = True
			if choice == _("Meditate"):
				print(_("You practiced meditation."))
				if not player.meditated:  # You can only get the bonus once per year
					player.change_health(randint(2, 4))
					player.change_happiness(randint(3, 5))
					player.change_karma(randint(1, 3))
					player.change_stress(-randint(3, 8))
					if player.has_trait("MEDITATOR"):
						player.change_stress(-4)
						player.change_happiness(2)
						player.change_health(randint(1, 2))
					if player.times_meditated == 0 or one_in(20):  
						# Your first meditation is guaranteed to cause a deeper awareness
						player.change_happiness(2)
						player.change_stress(-3)
						print(_("You have achieved a deeper awareness of yourself."))
						display_bar(_("Karma"), player.karma)
						if player.times_meditated > 0 and x_in_y(2, 5) and not x_in_y(player.stress, 100):
							player.learn_trait("MEDITATOR")
					if player.has_trait("CHEERFUL"):
						player.change_happiness(4)
					player.meditated = True
					player.times_meditated += 1
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
				if player.has_trait("BOOK_LOVER"):
					enjoyment = max(enjoyment, randint(35, 100))	
				display_bar(_("Your Enjoyment"), enjoyment)
				if not player.visited_library:  # You can only get the bonus once per year
					happy_gain = enjoyment / 15
					if player.has_trait("BOOK_LOVER"):
						happy_gain *= 1.5
						happy_gain += 2
					player.change_happiness(round_stochastic(happy_gain))
					if player.has_trait("CHEERFUL"):
						player.change_happiness(3)
					player.change_smarts(randint(2, 5))
					if player.has_trait("GENIUS"):
						player.change_smarts(5)
					elif player.has_trait("NERD"):
						player.change_smarts(3)
					player.times_visited_library += 1
					if one_in(48) and random.random() < 0.95**player.times_visited_library:
						can_learn_nerd = not player.has_trait("NERD")
						if can_learn_nerd and x_in_y(player.smarts, 200):
							player.learn_trait("NERD")
						else:
							player.learn_trait("BOOK_LOVER")
					player.visited_library = True
			elif choice == _("Read a Book"):
				#print(_("Coming soon!"))
				done = False
				while not done:
					available = [b for b in BOOKS if player.age >= b[3]]
					selection = random.sample(available, min(len(available), 5))
					names = [s[0] for s in selection]
					clear_screen()
					print(_("Which book would you like to read?"))
					choice = choice_input(*(names + [_("Back")]))
					if choice <= len(names):
						book = selection[choice - 1]
						title = book[0]
						category = book[1]
						total_pages = book[2]
						happy_amount = book[4]
						if player.has_trait("BOOK_LOVER"):
							if happy_amount > 0:
								happy_amount = math.ceil(min(happy_amount * 1.5, (100 + happy_amount) / 2))
							else:
								happy_amount = -(abs(happy_amount)//2)
						smarts_amount = book[5]
						reading = True
						pages = 0
						while reading:
							clear_screen()
							print(_('You are reading "{book_title}"').format(book_title=title))
							display_data(_("Category"), category)
							display_data(_("Pages read"), f"{pages}/{total_pages}")
							print()
							print(_("Press 1 to read each page"))
							choice = choice_input(_("Read page"), _("Abandon it"), _("Pick a different book"))
							if choice == 1:
								pages += 1
								if pages >= total_pages:
									time.sleep(0.5)
									print(_("You read all {pages} pages of \"{book}\".").format(pages=total_pages, book=title))
									done = True
									reading = False
									enjoyment = randint(25, 50) + randint(0, 25)
									if happy_amount > 0:
										r = (happy_amount/100)**0.7
										enjoyment = round_stochastic(enjoyment + (100 - enjoyment)*r)
									display_bar(_("Your Enjoyment"), enjoyment)
									learn = []
									if total_pages > randint(48, 150) and x_in_y(math.sqrt(smarts_amount), 100):
										learn.append("NERD")
									if x_in_y(math.sqrt(happy_amount), 100):
										learn.append("BOOK_LOVER")
									if learn:
										player.learn_trait(random.choice(learn))
									press_enter()
									h_amount = math.ceil(random.uniform(0.8, 1) * happy_amount * (1 - player.happiness/100))
									s_amount = math.ceil(random.uniform(0.8, 1) * smarts_amount * (1 - player.smarts/100))
									player.change_happiness(h_amount)
									player.change_smarts(s_amount)
							else:
								reading = False
								if choice == 2:
									done = True
					else:
						done = True
		elif choice == _("Plastic Surgery"):
			selected = True
			if player.age - player.last_plastic_surgery < 8:
				print(_("Please wait a while before getting another plastic surgery."))
			elif yes_no(_("Would you like to receive plastic surgery? (Cost: $25000)")):
				if player.money < 25000:
					print(_("You don't have enough money"))
				else:
					player.money -= 25000
					if one_in(6):
						damage = randint(15, 70)
						val = round_stochastic(damage / 2)
						print(_("Your plastic surgery was botched!"))
						display_bar(_("Damage"), val)
						press_enter()
						player.change_happiness(-val)
						player.change_health(-val)
						player.change_looks(-val)
						if player.health <= 0 and one_in(6) and not x_in_y(player.karma, 100) and damage >= randint(25, 100):
							player.die(_("You died after receiving a botched plastic surgery."))
					else:
						results = min(randint(14, 100), randint(14, 100))
						print(_("Your plastic surgery was successful."))
						display_bar(_("Results"), results)
						press_enter()
						val = round_stochastic(results / 2)
						player.change_happiness(val)
						player.change_looks(val)
					player.last_plastic_surgery = player.age
		elif choice == _("Adoption"):
			selected = True
			if player.age > 70:
				print(_("You are too old to adopt a child."))
			elif len(player.children) >= 5:
				print(_("You already have enough children."))
			else:
				gender = Gender.random()
				smarts = randint(0, 50) + randint(0, 50)
				looks = randint(0, 50) + randint(0, 50)
				c = Child(random_name(gender), random_last_name(), gender, smarts, looks, adopted=True)
				age = randint(1, 17)
				for i in range(age):
					c.total_happiness += randint(30, 100)
				c.age = age
				if c.gender == Gender.Male:
					s = _("a {age}-year-old boy")
				else:
					s = _("a {age}-year-old girl")
				s = s.format(age=c.age)
				print(_("You have an opportunity to adopt {name}, {name_and_age}.").format(name=c.name, name_and_age=s))		
				print_align_bars(
					(_("Smarts"), c.smarts),
					(_("Looks"), c.looks)
				)
				cost = randint(10000, 30000)
				display_data(_("Cost"), f"${cost}")
				if yes_no(_("Would you like to adopt this child?")):
					if player.money < cost:
						print(_("You don't have enough money"))
					else:
						c.happiness = randint(40, 100)
						player.money -= cost
						if yes_no(_("Would you like to change {name}'s last name to match yours?").format(name=c.name)):
							c.lastname = player.lastname
							c.update_name()
						print(_("You have adopted {name}, {name_and_age}.").format(name=c.name, name_and_age=s))
						player.change_happiness(randint(15, 30))
						player.relations.append(c)
						player.children.append(c)
		elif choice == _("Lottery"):
			selected = True
			print(_("Play the lottery today!"))
			print(_("Ticket cost: $4 each"))
			print(
				_("Lottery jackpot: ${jackpot}").format(jackpot=player.lottery_jackpot)
			)
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
					print(
						_(
							"Guess the 4 winning numbers between 1 and 20. Each number in the line must be separated by a space."
						)
					)
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
								msg = _("Guess #{num}: ").format(num=i + 1)
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
					print(
						_("The winning numbers are {nums}").format(
							nums=", ".join(map(str, winning))
						)
					)
					won = False
					for guess in guessed:
						if set(guess) == set(winning):
							won = True
							break
					if won:
						print(
							_("YOU WON THE ${amount} LOTTERY JACKPOT!!!").format(
								amount=player.lottery_jackpot
							)
						)
						player.change_happiness(100)
						player.money += player.lottery_jackpot
						player.change_jackpot()
					else:
						print(
							_("You did not win the ${amount} lottery jackpot.").format(
								amount=player.lottery_jackpot
							)
						)
		elif choice == _("Surrender"):
			selected = True
			if yes_no(_("Are you sure you want to surrender this life?")):
				if yes_no(_("This will kill your current character. Continue?")):
					player.die(_("You surrendered."))
							      