import os as _os

DEBUG = False

MALE_NAMES = open("assets/male_names.txt").read().splitlines()
FEMALE_NAMES = open("assets/female_names.txt").read().splitlines()
LAST_NAMES = open("assets/last_names.txt").read().splitlines()

SAVE_PATH = filename = _os.getcwd() + "/game_saves"  # + "/gamedata.pickle"

SALARY_TAX_BRACKETS = [
    [9950, 0.1],
    [40525, 0.12],
    [86375, 0.22],
    [164925, 0.24],
    [209425, 0.32],
    [523600, 0.35],
    0.37,
]

from src.lifesim_lib.translation import _

ILLNESSES_TRANSLATIONS = {
    "Depression": _("Depression"),
    "High Blood Pressure": _("High Blood Pressure"),
}

SPEND_TIME_PLACES = [
	_("shopping at a flea market"),
	_("bowling"),
	_("to the beach"),
	_("to play golf"),
	_("to do some gardening"),
	_("to a pilates class"),
	_("to play catch"),
	_("to make homemade mini pizzas"),
	_("to perform in a flashmob at the courthouse"),
	_("to do a puzzle at the library"),
	_("to relax while floating in a natural hot spring"),
	_("crocheting"),
	_("to bring donuts to the police station"),
	_("to blow bubbles"),
	_("bird-watching"),
	_("for a picnic"),
	_("to a baseball game"),
	_("to an arcade"),
	_("to an art museum"),
	_("to a tennis match"),
	_("to the circus"),
	_("to the movies"),
	_("to play tennis"),
	_("to fly a kite"),
	_("bungee-jumping"),
	_("fishing"),
	_("shopping"),
	_("to a hockey game")
]

COMPLIMENTS = [
    _("a boss"),
    _("a bubbly personality"),
    _("a brilliant mind"),
    _("a champion"),
    _("a gem"),
    _("a genius"),
    _("a jewel"),
    _("a legend"),
    _("a player"),
    _("a revolutionary"),
    _("a smart cookie"),
    _("a treasure"),
    _("a winner"),
    _("a wizard"),
    _("a VIP"),
    _("a visionary"),
    _("adorable"),
    _("admirable"),
    _("an OG"),
    _("an eager beaver"),
    _("brave"),
    _("bright"),
    _("brilliant"),
    _("charming"),
    _("clever"),
    _("cool"),
    _("courageous"),
    _("cute"),
    _("dashing"),
    _("delightful"),
    _("dope"),
    _("elite"),
    _("fascinating"),
    _("fearless"),
    _("fine"),
    _("fresh"),
    _("gorgeous"),
    _("golden"),
    _("groovy"),
    _("inspiring"),
    _("intelligent"),
    _("legendary"),
    _("lionhearted"),
    _("magnetic"),
    _("magnificent"),
    _("motivating"),
    _("neat"),
    _("nifty"),
    _("one-of-a-kind"),
    _("a perfect 10"),
    _("phenomenal"),
    _("rad"),
    _("savage"),
    _("smart"),
    _("spectatular"),
    _("stellar"),
    _("strong"),
    _("stunning"),
    _("stylish"),
    _("swell"),
    _("the best"),
    _("the GOAT"),
    _("the greatest"),
    _("the life of the party"),
    _("unparalled"),
    _("wise"),
    _("wonderful"),
    _("world-class"),
]

MUSIC_ARTISTS = [
	_("The Beatles"), 
	_("Eminem"),
	_("Michael Jackson"),
	_("Elton John"),
	_("Elvis Presley"),
	_("Rihanna"),
	_("Madonna"),
	_("Pink Floyd"),
	_("Mariah Carey"),
	_("Taylor Swift"),
	_("Beyoncé"),
	_("Whitney Houston"),
	_("The Rolling Stones"),
	_("Drake"),
	_("Justin Bieber"),
	_("Ed Sheeran"),
	_("Bruno Mars")
]

# Insults moved to the bottom

#------------------------------------------------------------------
# Flirts

# School flirts
# Suggest that Primary school = primary school flirts; Middle school = Middle school & primary school flirts; High school = High school, middle school & primary school flirts
# Primary School flirts:
#   You complimented your classmate, {name}, on {his_her} haircut.
#   You followed your classmate, {name}, around school trying to get {him_her} to notice you.
#   You teased your classmate, {name}, just to get {his_her} attention.
#-   You sat next to your classmate, {name}, at lunch just to get {his_her} attention.
#-   You passed a charmingly funny note to your classmate, {name}, in class.
#-   You passed a note to your classmate, {name}, in class.
#-   You gave your classmate, {name}, a shy smirk and a wink from across the room.
#-   You gave your classmate, {name}, an enamouring smirk and wink from across the room.
#-   You gave your classmate, {name}, a confident smirk and wink from across the room.
#-   You did the Lean dance move to try to impress your classmate, {name}.
#-   You did the Carlton dance move to try to impress your classmate, {name}.
#-   You did the Dejo dance move to try to impress your classmate, {name}.
#-   You did the Moonwalk dance move to try to impress your classmate, {name}.
#-   You did the Robot dance move to try to impress your classmate, {name}.
#-   You did the Soulja Boy dance move to try to impress your classmate, {name}.
#-   You did the Single Ladies dance move to try to impress your classmate, {name}.

#   You did the {DANCE_MOVE} dance move to try to impress your classmate, {name}.
DANCE_MOVE = [
    _("Carlton"),
    _("Dejo"),
    _("Lean"),
    _("Moonwalk"),
    _("Robot"),
    _("Running Man"),
    _("Single Ladies"),
    _("Soulja Boy"),
    _("Shoot"),
]
#   You gave your classmate, {name}, {FLIRT_VERB_SMIRK} smirk and a wink from across the room.
FLIRT_VERB_SMIRK = [
    _("an awkward"),
    _("a confident"),
    _("an enamouring"),
    _("a shy"),
    _("a smooth"),
]
#   You sat next to your classmate, {name}, {FLIRT_LOCATION_SAT} just to get {his_her} attention.
FLIRT_LOCATION_SAT = [
    _("at lunch"),
    _("by the pool"),
    _("by the sports fields"),
    _("during assembly"),
    _("in the gym"),
    _("in the library"),
    _("in english class"),
    _("in math class"),
    _("in science class"),
    _("on the way home from school"),
    _("on the way to school"),
]
#   You passed {FLIRT_VERB_NOTE} note to your classmate, {name}, in class.
FLIRT_VERB_NOTE = [
    _("a"),
    _("an awkward"),
    _("a charmingly funny"),
    _("a flirtatious"),
]

# Middle School flirts:
#   You awkwardly bumped into your classmate, {name}, so that {he_she} had to talk to you.
#   You stared at your classmate, {name}, for 22 straight minutes today during an assembly, just so she would notice that you are interested in {him_her}.
#   You passed an awkward note to your classmate, {name}, in class.
#-   You said "Why, hello there!" Every time you saw your classmate, {name}, at school today.
#   You winked confidently at your classmate, {name}, while the teacher was discussing the sexual reproductive system.
#   You laughed at everything your classmate, {name}, said, with the hope that {he_she} would embrace the attention from you.


# You stared at your classmate, {name}, for {FLIRT_STARE_TIME_MIDDLE_SCHOOL} straight minutes today during {FLIRT_STARE_CLASSES_MIDDLE_SCHOOL} class, just so she would notice that you are interested in {him_her}.
#FLIRT_STARE_TIME_MIDDLE_SCHOOL = randint(5, 25)
# ^ TODO: Move this ^ out of const.py into the string format itself so the number isn't the same if generated multiple times while the game is open

# LIST ORDERED: Alphabetical
FLIRT_STARE_CLASSES_MIDDLE_SCHOOL = [
    _("Art"),
    _("Careers"),
    _("Computer Science"),
    _("Drama"),
    _("English"),
    _("Geography"),
    _("History"),
    _("Math"),
    _("Music"),
    _("Physical Eduacation"),
    _("Science"),
    _("Social Studies"),
]


# High School flirts:
#-   You stared at your classmate, {name}, for 55 straight minutes today during science class, just so she would notice that you are interested in {him_her}.
#-   You said "Why, hello there!" Every time you saw your classmate, {name}, at school today.
#   You clumsily blew a kiss to your classmate, {name}, while the teacher wasn't looking.
#   You meekly blew a kiss to your classmate, {name}, while the teacher wasn't looking.
#   You ran your fingers through your hair as you takled with your classmate, {name}, so that {he_she} would realise you have a crush on her.
#   You proudly showed your classmate, {name}, how hard you've been working on your twerking form.
#   You mimicked your classmate, {name}'s, body language so that she would feel like she relates to you.


# You stared at your classmate, {name}, for {FLIRT_STARE_TIME_HIGH_SCHOOL} straight minutes today during {FLIRT_STARE_CLASSES_HIGH_SCHOOL} class, just so she would notice that you are interested in {him_her}.
#FLIRT_STARE_TIME_HIGH_SCHOOL = randint(10, 55)
# LIST ORDERED: Business > CompSci/IT > English > Family/Consumer Science > Languages > Math > Performing Arts > Physical Ed > Science > Social Studies > Visual Arts > Vocational Ed
FLIRT_STARE_CLASSES_HIGH_SCHOOL = [
    _("Accounting"),
    _("Business law"),
    _("Business management"),
    _("Consumer education"),
    _("Entrepreneurial skills"),
    _("Introduction to business"),
    _("Marketing"),
    _("Personal finance"),
    _("Animation"),
    _("App development"),
    _("Audio production"),
    _("Computer programming"),
    _("Computer repair"),
    _("Film production"),
    _("Graphic design"),
    _("Media technology"),
    _("Music production"),
    _("Typing"),
    _("Video game development"),
    _("Web design"),
    _("Web programming"),
    _("Word processing"),
    _("American literature"),
    _("British literature"),
    _("Contemporary literature"),
    _("Creative writing"),
    _("Communication skills"),
    _("Debate"),
    _("English language and composition"),
    _("English literature and composition"),
    _("Humanities"),
    _("Journalism"),
    _("Literary analysis"),
    _("Modern literature"),
    _("Poetry"),
    _("Popular literature"),
    _("Rhetoric"),
    _("Technical writing"),
    _("Works of Shakespeare"),
    _("World literature"),
    _("Written and oral communication"),
    _("Chemistry of foods"),
    _("CPR training"),
    _("Culinary arts"),
    _("Early childhood development"),
    _("Early childhood education"),
    _("Family studies"),
    _("Fashion and retail merchandising"),
    _("Fashion construction"),
    _("Home economics"),
    _("Interior design"),
    _("Nutrition"),
    _("American Sign Language"),
    _("Ancient Greek Language"),
    _("Arabic Language"),
    _("Chinese Language"),
    _("French Language"),
    _("German Language"),
    _("Hebrew Language"),
    _("Italian Language"),
    _("Japanese Language"),
    _("Korean Language"),
    _("Latin Language"),
    _("Portuguese Language"),
    _("Russian Language"),
    _("Spanish Language"),
    _("Algebra 1"),
    _("Algebra 2"),
    _("Calculus"),
    _("Computer math"),
    _("Consumer math"),
    _("Fundamentals of math"),
    _("Geometry"),
    _("Integrated math"),
    _("Math applications"),
    _("Multivariable calculus"),
    _("Practical math"),
    _("Pre-algebra"),
    _("Pre-calculus"),
    _("Probability"),
    _("Quantitative literacy"),
    _("Statistics"),
    _("Trigonometry"),
    _("Choir"),
    _("Concert band"),
    _("Dance"),
    _("Drama"),
    _("Guitar"),
    _("Jazz band"),
    _("Marching band"),
    _("Music theory"),
    _("Orchestra"),
    _("Percussion"),
    _("Piano"),
    _("Theater technology"),
    _("World music"),
    _("Aerobics"),
    _("Dance"),
    _("Gymnastics"),
    _("Health"),
    _("Lifeguard training"),
    _("Pilates"),
    _("Racket sports"),
    _("Specialized sports"),
    _("Swimming"),
    _("Weight training"),
    _("Yoga"),
    _("Agriculture"),
    _("Astronomy"),
    _("Biology"),
    _("Botany"),
    _("Chemistry"),
    _("Earth science"),
    _("Electronics"),
    _("Environmental science"),
    _("Environmental studies"),
    _("Forensic science"),
    _("Geology"),
    _("Marine biology"),
    _("Oceanography"),
    _("Physical science"),
    _("Physics"),
    _("Zoology"),
    _("Cultural anthropology"),
    _("Current events"),
    _("European history"),
    _("Geography"),
    _("Global studies"),
    _("Human geography"),
    _("International relations"),
    _("Law"),
    _("Macroeconomics"),
    _("Microeconomics"),
    _("Modern world studies"),
    _("Physical anthropology"),
    _("Political studies"),
    _("Psychology"),
    _("Religious studies"),
    _("Sociology"),
    _("National government"),
    _("National history"),
    _("Women's studies"),
    _("World history"),
    _("World politics"),
    _("World religions"),
    _("3-D art"),
    _("Art history"),
    _("Ceramics"),
    _("Digital media"),
    _("Drawing"),
    _("Film production"),
    _("Jewelry design"),
    _("Painting"),
    _("Photography"),
    _("Printmaking"),
    _("Sculpture"),
    _("Auto body repair"),
    _("Auto mechanics"),
    _("Building construction"),
    _("Computer-aided drafting"),
    _("Cosmetology"),
    _("Criminal justice"),
    _("Driver education"),
    _("Electronics"),
    _("FFA (Future Farmers of America)"),
    _("Fire science"),
    _("Heating and cooling systems"),
    _("Hospitality and tourism"),
    _("JROTC (Junior Reserve Officers' Training Corps)"),
    _("Metalworking"),
    _("Networking"),
    _("Plumbing"),
    _("Production technology"),
    _("Refrigeration fundamentals"),
    _("Robotics"),
    _("Woodworking"),
]
#   You said "{FLIRT_SAID_SAW}" Every time you saw your classmate, {name}, at school today.
FLIRT_SAID_SAW = [
    _("Ooh La La!"),
    _("Why, hello there!"),
]


# Tertiary (University/Community College etc) Flirts:


# Adult flirts
# General
# Workplace

#------------------------------------------------------------------
# Hook Up

# {Relation}
# Things are getting hot with your {relation}, {name}, and you're thinking about safe sex.
# What will you do? > Use a condom (Make him_her use a condom) || Don't use a condom
# No condoms are available. What will you do? > Oh well, keep going || Pull out (Tell him to pull out) || Never mind, I can't do it

# You had a one night stand with your {relation}, {name}. {hook_up_yes_female}
HOOK_UP_YES_FEMALE = [
    _("You have a hard time walking straight the next day"),
    _("You left your underwear behind"),
]
HOOK_UP_NO_FEMALE = [
    _(""),
]
# If your character is male
HOOK_UP_YES_MALE = [
    _("You left your underwear behind"),
]
HOOK_UP_NO_MALE = [
    _(""),
]

# {Random NPC}
# {A dude} named {name} {invites you to exchange nude pics}. > Take him to bed || Absolutely not
# If take him to bed:
# Things are getting hot with {name}, and you're thinking about safe sex.
# What will you do? > Use a condom (Make him_her use a condom) || Don't use a condom
# No condoms are available. What will you do? > Oh well, keep going || Pull out (Tell him to pull out) || Never mind, I can't do it
HOOK_UP_MALE_TYPES = [
    _("A dude"),
    _("A guy"),
    _("An interesting guy"),
]
HOOK_UP_MALE_TEXTS = [
    _("invites you to exchange nude pics"),
]
# You have an opportunity to have a one night stand with a young man named {name}.
# What will you do? > Hit that (/ Sleep with him_her / Get at it / Give it to him_her) || No, I'm not into that

# No condoms are available and it looks like he_she's got some craziness going on down below.
# What will you do? > Keep going worry later || Pull out (/Tell him to pull out) || Nevermind, I can't do it

# You {got up and left}. He respected your decision (/He called you {insults})
HOOK_UP_CRAZINESS_NO = [
    _("got up and left"),
]

#------------------------------------------------------------------
# Jobs lists for NPC

# Teacher Jobs (for school faculty):

# Primary School Teachers
FACULTY_JOBS_PRIMARY = [
    _(""),
]
STAFF_JOBS_PRIMARY = [
    _("Principal"),
    _("Assistant Principal"),
    _("Administrator"),
    _("Cleaner"),
    _("Executive Assistant"),
    _("Food Service"),
    _("Groundskeeper"),
    _("Substitute Teacher"),
]
# Middle School Teachers
FACULTY_JOBS_MIDDLE = [
    _("Art Teacher"),
    _("Careers Teacher"),
    _("IT Teacher"),
    _("Drama Teacher"),
    _("English Teacher"),
    _("Geography Teacher"),
    _("History Teacher"),
    _("Math Teacher"),
    _("Music Teacher"),
    _("P.E. Teacher"),
    _("Science Teacher"),
    _("Social Studies Teacher"),
]
STAFF_JOBS_MIDDLE = [
    _("Principal"),
    _("Assistant Principal"),
    _("Administrator"),
    _("Cleaner"),
    _("Executive Assistant"),
    _("Food Service"),
    _("Groundskeeper"),
    _("Substitute Teacher"),
]
# High School / Secondary Teachers
FACULTY_JOBS_SECONDARY = [
    _("Accounting Teacher"),
    _("Art Teacher"),
    _("Chemistry Teacher"),
    _("Computer Science Teacher"),
    _("Drama Teacher"),
    _("Economics Teacher"),
    _("English Teacher"),
    _("Foreign Language"),
    _("Math Teacher"),
    _("Music Teacher"),
    _("P.E. Teacher"),
    _("Physics Teacher"),
]
STAFF_JOBS_SECONDARY = [
    _("Principal"),
    _("Assistant Principal"),
    _("Administrator"),
    _("Cleaner"),
    _("Careers Counsellor"),
    _("Executive Assistant"),
    _("Food Service"),
    _("Groundskeeper"),
    _("Substitute Teacher"),
]
# Community College Teachers
FACULTY_JOBS_COMMUNITY_COLLEGE = [
    _("Associate Professor"),
    _("Professor"),
    _("Researcher")
]
STAFF_JOBS_COMMUNITY_COLLEGE = [
    _("Dean"),
    _("Food Service"),
    _("Groundskeeper"),
]
# University teachers (for each degree)
FACULTY_JOBS_UNIVERSITY = [
    _("Associate Professor"),
    _("Professor"),
    _("Researcher")
]
STAFF_JOBS_UNIVERSITY = [
    _("Dean"),
    _("Associate Dean"),
    _("Chancellor"),
    _("Director of Education"),
    _("Food Service"),
    _("Groundskeeper"),
    _("Librarian"),
    _("President"),
    _("Vice Chancellor"),
    _("Vice President"),
]

# World NPC Jobs (For dating app, love interest/find a date, parent's jobs, other {relation}'s jobs):
# School Love Interest (ages under 18)
JOBS_HIGH_SCHOOL = [
    _("High School Dropout"),
    _("High School Student"),
    _("High School Student, Part-time Arcade Assistant"),
    _("High School Student, Part-time Armpit Sniffer"),
    _("High School Student, Part-time Barista"),
    _("High School Student, Part-time Bike Shop Mechanic"),
    _("High School Student, Part-time Boutique Associate"),
    _("High School Student, Part-time Bowling Alley Assistant"),
    _("High School Student, Part-time Camp Counsellor"),
    _("High School Student, Part-time Car Wash Attendant"),
    _("High School Student, Part-time Dance Instructor"),
    _("High School Student, Part-time Doorman"),
    _("High School Student, Part-time Fitness Instructor"),
    _("High School Student, Part-time Gym Receptionist"),
    _("High School Student, Part-time Hotel Concierge"),
    _("High School Student, Part-time Ice Cream Scooper"),
    _("High School Student, Part-time Lifeguard"),
    _("High School Student, Part-time Mall Kiosk Worker"),
    _("High School Student, Part-time Personal Trainer"),
    _("High School Student, Part-time Usher"),
    _("High School Student, Part-time Valet"),
    _("High School Student, Part-time Window Cleaner"),
]

JOBS_NPC = [
    _("Unemployed"),
    _(""),
]
#------------------------------------------------------------------
# Jobs
JOBS_FREELANCE_GIGS = [
    _("Handyman"),
    _("Tutor"),
    _("Caretaker"),
    _("Lawn Mower"),
    _("Babysitter"),
    _("Dog Walker"),
    _("Pet Sitter"),
    _("Lemonade Stand"),
    _("Kissing booth"),
]
JOBS_PART_TIME = [
    _("Arcade Assistant"),
    _("Armpit Sniffer"),
    _("Barista"),
    _("Bellhop"),
    _("Bike Shop Mechanic"),
    _("Bookkeeper"),
    _("Boutique Associate"),
    _("Bowling Alley Assistant"),
    _("Camp Counsellor"),
    _("Car Wash Attendant"),
    _("Caterer"),
    _("Collections Specialist"),
    _("Concessions Attendant"),
    _("Dance Instructor"),
    _("Delivery Driver"),
    _("Doorman"),
    _("Fitness Instructor"),
    _("Gym Receptionist"),
    _("Hotel Concierge"),
    _("Hotel Front Desk Clerk"),
    _("Ice Cream Scooper"),
    _("Lifeguard"),
    _("Mall Kiosk Worker"),
    _("Mall Santa"),
    _("Office Assistant"),
    _("Personal Trainer"),
    _("Pool Towel Attendant"),
    _("Sandwich Maker"),
    _("School Bus Driver"),
    _("Sign Holder"),
    _("Street Sweeper"),
    _("Swim Instructor"),
    _("Usher"),
    _("Valet"),
    _("Window Cleaner"),
    _("Yoga Receptionist"),
]
# Part time job categories
JOBS_PART_TIME_CAR_WASH = [ 
    _("Car Wash Attendant"),
    _(""),
]
JOBS_PART_TIME_GYM = [
    _("Yoga Receptionist"),
]
JOBS_PART_TIME_HOTEL = [
    _("Pool Towel Attendant"),
]
JOBS_PART_TIME_MALL = [
    _("Arcade Assistant"),
]
JOBS_PART_TIME_MOVIE_THEATRE = [
    _("Concessions Attendant"),
]
JOBS_PART_TIME_MUNICIPAL = [
    _(""),
    _("Street Sweeper"),
]



# Full time jobs arranged into job categories. E.g. Junior Financial Analyst (Corporate) comes under CORPORATE =, or FINANCE =
# Junior Corporate jobs for age/qualification reasons. {JOBS_CORPORATE_JUNIOR} (Corporate).
# Nb. These will probably need to be re-categorised once they're all down. The in-app classification system isn't very good
JOBS_ADULT_FILM_STUDIO = [
    _("Fluffer"),
    _("Porn Actor"),
    _("Porn Cameraman"),
    _("Porn Star"),
    _("Porn Writer"),
    _("Porn Director"),
]
JOBS_APP_DEVELOPER_JUNIOR = [
    _("Junior App Developer"),
    _(""),
]
JOBS_APP_DEVELOPER = [
    _("App Developer"),
    _(""),
]
JOBS_AIRLINE_JUNIOR = [
    _("Baggage Handler"),
    _("Junior Flight Attendant"),
]
JOBS_AIRLINE = [
    _("Baggage Handler"),
    _(""),
]
JOBS_ARCHITECTURAL_FIRM_JUNIOR = [
    _("Junior Architect"),
    _(""),
]
JOBS_ARCHITECTURAL_FIRM = [
    _("Architect"),
    _(""),
]
JOBS_CAR_DEALER_JUNIOR = [
    _("Apprentice Auto Mechanic"),
    _("Apprentice Auto Electrician"),
    _(""),
]
JOBS_CAR_DEALER = [
    _("Auto Mechanic"),
    _("Auto Electrician"),
    _(""),
]
JOBS_CHURCH = [
    _("Deacon"),
    _(""),
]
JOBS_CIRCUS = [
    _("Acrobat"),
    _("Clown"),
    _("Dancer"),
    _("Fire Breather"),
    _("Fire Eater"),
    _("Horse Rider"),
    _("Juggler"),
    _("Lion Tamer"),
    _("Magician"),
    _("Magician's Assistant"),
    _("Plate Spinner"),
    _("Sword Eater"),
    _("Tightrope Walker"),
    _("Trapeze Artist"),
    _("Unicyclist"),
]
JOBS_CORPORATE_JUNIOR = [
    _("Administrative Assistant"),
    _("Janitor"),
    _("Junior Computer Programmer"),
    _("Junior Database Administrator"),
    _("Junior Financial Advisor"),
    _("Junior Financial Analyst"),
    _("Junior Internal Auditor"),
    _("Junior Lobbyist"),
    _(""),
]
JOBS_CORPORATE = [
    _("Administrative Assistant"),
    _("Computer Programmer"),
    _("Janitor"),
    _("Financial Advisor"),
    _("Financial Analyst"),
    _("Internal Auditor"),
    _("Lobbyist"),
    _("Receptionist"),
    _(""),
]
JOBS_DENTAL_OFFICE = [
    _("Dental Hygenist"),
    _("Dental Receptionist"),
    _("Dentist"),
]
JOBS_ENGINEERING_FIRM_JUNIOR = [
    _("Junior Microbiologist"),
]
JOBS_ENGINEERING_FIRM = [
    _("Engineer I"),
    _("Environmental Scientist"),
]
JOBS_ESCORT_AGENCY = [
    _("Escort"),
    _(""),
]
JOBS_FAST_FOOD = [
    _("Crew Member"),
    _("Manager"),
    _("Team Leader"),
]
JOBS_FILM_STUDIO = [
    _("Dancer"),
    _(""),
]
JOBS_GROCERY_STORE_JUNIOR = [
    _("Apprentice Grocer"),
    _(""),
]
JOBS_GROCERY_STORE = [
    _("Grocer"),
    _(""),
]
JOBS_HOSPITAL = [
    _("Brain Surgeon"),
    _(""),
]
JOBS_INDUSTRIAL = [
    _("Factory Worker"),
    _(""),
]
JOBS_INSURANCE_AGENCY = [
    _("Insurance Agent"),
    _(""),
]
JOBS_JEWELLER = [
    _("Sales Associate"),
    _("Jeweller"),
]
JOBS_LAW_FIRM_JUNIOR = [
    _("Junior Associate"),
    _(""),
]
JOBS_LAW_FIRM = [
    _("Legal Secretary"),
    _(""),
]
JOBS_MALL = [
    _("Mall Cop"),
    _("Facilities Manager"),
]
JOBS_MODEL_AGENCY = [
    _("Catalogue Model"),
    _("Foot Model"),
    _("Hand Model"),
    _("Fit Model"),
    _("Lingerie Model"),
    _("Model Scout"),
    _("Modelling Agent"),
    _("Photo Model"),
    _("Runway Model"),
]
JOBS_MOVIES = [
    _("Cameraman"),
    _("Director"),
    _("Key Grip"),
]
JOBS_MUNICIPAL = [
    _("Junior Policy Analyst"),
    _("Junior Mail Carrier"),
]
JOBS_MUNICIPAL = [
    _("Bus Driver"),
    _("Magistrate"),
    _("Mail Carrier"),
]
JOBS_MUSEUM = [
    _("Museum Docent"),
    _("Gallery Associate"),
]
JOBS_NIGHTCLUB = [
    _("Bartender"),
    _("DJ"),
    _("Host"),
    _("Manager"),
    _("Security"),
]
JOBS_REAL_ESTATE = [
    _("Real Estate Agent"),
    _(""),
]
JOBS_RETAILER = [
    _("Retail Salesperson"),
    _(""),
]
JOBS_RIDE_SHARING_APP = [
    _("Driver"),
    _(""),
]
JOBS_RESTAURANT = [
    _("Bartender"),
    _("Server"),
    _("Host"),
]
JOBS_SCHOOL = [
    _("Assistant Principal"),
]
JOBS_SALON = [
    _("Massage Therapist"),
    _(""),
]
JOBS_SMALL_BUSINESS_JUNIOR = [
    _("Apprentice Moonshiner"),
    _("Apprentice Tailor"),
    _("Junior Animator"),
    _("Junior Graphic Designer"),
    
]
JOBS_SMALL_BUSINESS = [
    _("Construction Worker"),
    _("Housekeeper"),
    _("Junior Animator"),
    _("Road Kill Remover"),
    _("Water Slide Tester"),
]
JOBS_STOCK_EXCHANGE_JUNIOR = [
    _("Junior Stockbroker"),
    _(""),
    _(""),
]
JOBS_STOCK_EXCHANGE = [
    _("Stockbroker"),
    _(""),
    _(""),
]
JOBS_STRIP_CLUB = [
    _("Exotic Dancer"),
    _("Pole Cleaner"),
    _(""),
]
JOBS_SUPERMARKET_JUNIOR = [
    _("Apprentice Baker"),
    _("Apprentice Butcher"),
    _("Apprentice Grocer"),
    _(""),
]
JOBS_SUPERMARKET = [
    _("Baker"),
    _("Butcher"),
    _("Grocer"),
    _(""),
]
JOBS_TELEVISION_JUNIOR = [
    _("Junior Cameraman"),
    _("Junior Reporter"),
]
JOBS_TELEVISION = [
    _("Animator"),
    _("Cameraman"),
    _("Cinematographer"),
    _("Casting Director"),
    _("Comedian"),
    _("Costume Designer"),
    _("Director"),
    _("Director of Photography"),
    _("Editor"),
    _("Key Grip"),
    _("Music Director"),
    _("News Reporter"),
    _("Production Designer and Art Director"),
    _("Sound Editor"),
    _("Talkshow Host"),
    _("Writer"),
]
JOBS_TRAVEL_AGENCY = [
    _("Tour Operator"),
    _("Travel Associate"),
]
JOBS_TRUCKING_COMPANY_JUNIOR = [
    _("Apprentice Trucker"),
    _(""),
]
JOBS_TRUCKING_COMPANY = [
    _("Trucker"),
    _(""),
]
JOBS_UNIVERSITY = [
    _("Archaeologist"),
    _("Professor"),
    _(""),
]
JOBS_VETERINARY_CLINIC_JUNIOR = [
    _("Junior Veterinarian"),
    _(""),
]
JOBS_VETERINARY_CLINIC = [
    _("Junior Veterinarian"),
    _("Veterinarian"),
]

# Jobs and their relevant qualifications
NO_QUALIFICATION_JOBS = [
    _("Bartender"),
]
HIGH_SCHOOL_QUALIFICATION_JOBS = [
    _("Apprentice Cameraman"),
]
# Temporary 'University' Cover-all
UNIVERSITY_QUALIFICATION_JOBS = [
    _("Engineer I"),
]
GRADUATE_SCHOOL_QUALIFICATION_JOBS = [
    _("Professor"),
]
LAW_SCHOOL_QUALIFICATION_JOBS = [
    _("Magistrate"),
]

# Careers and their relevant jobs
# I.e. Job for Engineering I is published as:
# Title: Engineer I
# Career: Chemical Engineer
# Employer: Sunbeam Consulting
# Salary: $49,140
# Education: University
## Potentially, these lists could be good for salaries as 'if career_chemical_engineer == Engineer I then base_salary = randint(47000, 52000)'
### or potentially if base_salary were years_in_job then automatic raises and requested raises could work off 'if years_in_job = > 2 then random chance increase current_salary by randint(2, 7) %'. and raise requests could directly call increase current_salary by randint(2, 7)% dependant on work performance
CAREER_ADULT_MEDIA = [
    _("Porn Actor"),
    _("Porn Cameraman"),
    _("Porn Star"),
    _("Porn Writer"),
    _("Porn Director"),
]
CAREER_AGENCY_MODEL = [
    _("Catalogue Model"),
    _("Foot Model"),
    _("Hand Model"),
    _("Fit Model"),
    _("Lingerie Model"),
    _("Photo Model"),
    _("Runway Model"),
]
CAREER_CAMERAMAN = [
    _("Apprentice Cameraman"),
    _("Cameraman"),
]
CAREER_CHEMICAL_ENGINEER = [
    _("Engineer I"),
]
CAREER_DENTISTRY = [
    _("Dental Hygenist"),
    _("Dentist"),
]
CAREER_FINANCIAL_ADVISOR = [
    _("Financial Advisor"),
    _("Junior Financial Advisor"),
]
CAREER_FINANCIAL_ANALYST = [
    _("Financial Analyst"),
    _("Junior Financial Analyst"),
]
CAREER_HOSPITALITY = [
    _("Bartender"),
    _("Host"),
    _("Waiter"),
]
CAREER_INTERNAL_AUDITOR = [
    _("Internal Auditor"),
    _("Junior Internal Auditor"),
]
CAREER_LAW = [
    _("Junior Associate"),
    _("Magistrate"),
]
CAREER_LOBBYIST = [
    _("Junior Lobbyist"),
    _("Lobbyist"),
]
CAREER_PROFESSOR = [
    _("Professor"),
]
CAREER_SCHOOL_ADMINISTRATOR = [
    _("Assistant Principal"),
    _("Principal"),
]
CAREER_VETERINARIAN = [
    _("Junior Veterinarian"),
    _("Veterinarian"),
]

# Hashed out while working on a better system design.
# No need for a Veterinary School when Veterinary medicine is your degree.
# Suggest something along the lines of either 'University' is renamed 'Undergraduate University' and 'Postgraduate University' is introduced for Masters / PhD level jobs. Or, 'University' leads you to an undergrad and postgrad selection.
#
# University Degrees
#   MAJORS = [
#       _("Arts"),
#       _("Business and Management"),
#       _("Computer Science"),
#       _("Economics"),
#       _("Education and Teaching"),
#       _("Engineering"),
#       _("Gender Studies"),
#       _("Music"),
#       _("Humanities"),
#       _("Law"),
#       _("Marketing"),
#       _("Mathematics and Statistics"),
#       _("Medicine"),
#       _("Political Science"),
#       _("Veterinary Medicine"),
#       _(""),
#   ]
#   # Student Outcomes. These jobs need one of the above Degrees
#   ARTS_JOBS = [
#       _(""),
#   ]
#   ENGINEERING_JOBS = [
#       _("Engineer I"),
#   ]


#----
# Special Jobs

# Actor
ACTOR_MENU = [
    _("Talent Manager"),
    _("Talent Agent"),
    _("Audition"),
    _("Extra"),
]
# Look for a talent agent. "A chick named {names} has offered to represent you as an agent. She said {if she could get a Carrot Top cast in a film, she could get you in one too}"
TALENT_AGENT_REPRESENTATION_OFFERS_FEMALE = [
    _("if she could get a Carrot Top cast in a film, she could get you in one too"),
]
TALENT_AGENT_REPRESENTATION_OFFERS_MALE = [
    _("he basically runs the industry and swears anyone would be lucky to work with him"),
]
# Audition
ACTING_AUDITION_TYPE = [
    _("Movie Roles"),
    _("Television Roles"),
]
# Movie Roles
MOVIE_ROLES = [
    _("Bit Role"),
    _("Lead Role"),
    _("Supporting Role"),
]
# Television Roles
TV_ROLES = [
    _("Ensemble Role"),
    _("Lead Role"),
    _("Recurring Role"),
    _("Regular Role"),
]
# Extra
EXTRA_ROLES_FEMALE = [
    _("A Businessman's daughter"),
    _("A Bridesmaid"),
]
EXTRA_ROLES_MALE = [
    _("A Businessman's son"),
    _("A Handyman"),
]
# E.g. "Producer: Compass Broadcasting Service". Nb. in the original game, Production companies are mislabelled as Producers. A producer is a job role
TV_PRODUCTION_COMPANIES = [
    _("A&E Televison Network"),
    _("ABC Studios"),
    _("ACME Communications"),
    _("Alloy Entertainment"),
    _("American Movie Classics"),
    _("Anonymous Content"),
    _("Bad Robot"),
    _("BBC America"),
    _("Beacon Pictures"),
    _("Bunim-Murray Productions"),
    _("CBS"),
    _("Defined Productions"),
    _("Dick Clark Productions"),
    _("eOne Television"),
    _("Eyeboogie, Inc."),
    _("Filmation"),
    _("FremantleMedia"),
    _("Global Broadcasting"),
    _("LIN TV Corporation"),
    _("Lions Gate Entertainment"),
    _("Lorimar"),
    _("Metro-Goldwyn-Mayer"),
    _("Raycom Media"),
    _("Shine America"),
    _("Sony Pictures Television"),
    _("Tribune Entertainment"),
    _("Universal Television"),
    _("Walt Disney Television"),
]
TV_SHOWS = [
    _(""),
]
# "You served as an extra playing {extra_roles_male or female} in the TV show {TV_shows}"


# Run your own business
BUSINESS_OWNER_START_TYPE = [
    _("Acquisition"),
    _("Startup"),
]
BUSINESS_TYPES = [
    _("Food Truck"),
    _("Gift Shop"),
    _("Health Food Store"),
    _("Brewery"),
    _("Adult Toys"),
    _("Marijuana Dispensary"),
    _("Lingerie Boutique"),
    _("Novelty"),
    _("Coffeehouse"),
    _("Beauty Supply"),
    _("Pet Supply"),
    _("Kitchenware"),
    _("Musical Instrument"),
    _("Jewellery"),
    _("Clothing Outlet"),
    _("Sporting Goods"),
    _("Footware"),
    _("Distillery"),
    _("Dairy Farm"),
    _("Winery"),
    _("Consumer Electronics"),
    _("Robotics"),
    _("Pharmaceutical"),
    _("Semiconductor"),
    _("Car Manufacturer"),
]


# Organised Crime Jobs
CRIMINAL_ORGANISATION = [
    _("Biker"),
    _("Irish Mob"),
    _("Latin Mafia"),
    _("Mafia"),
    _("Russian Mafia"),
    _("Triad"),
    _("Yakuza"),
]
ORGANISED_CRIME_JOIN_METHOD = [
    _("Relay messages"),
    _("Chauffeur them around town"),
    _("Wait tables"),
    _("Offer to do favours"),
    _("Do yard work"),
    _("Hang out at their club"),
]
# Biker
BIKER_SYNDICATE = [
    _("Bandidos"),
    _("Hell's Angels"),
]
# Irish mob
IRISH_MOB_SYNDICATE = [

]
# Latin Mafia
LATIN_MAFIA_SYNDICATE = [
    
]
# Mafia
MAFIA_SYNDICATE = [
    
]
# Russian Mafia
RUSSIAN_MAFIA_SYNDICATE = [
    
]
# Triad
TRIAD_SYNDICATE = [
    
]
# Yakuza
YAKUZA_SYNDICATE = [
    
]



# Model
MODEL_MENU = [
    _("Model Manager"),
    _("Model Agent"),
    _("Audition"),
    _("Freelance"),
]
# Look for a modelling agent. "A chick named {names} has offered to represent you as an agent. She said {if she could get Ugly Betty on the cover of Vogue, she could get you there too}"
MODEL_AGENT_REPRESENTATION_OFFERS_FEMALE = [
    _("if she could get Ugly Betty on the cover of Vogue, she could get you there too"),
]
MODEL_AGENT_REPRESENTATION_OFFERS_MALE = [
    _("he basically runs the industry and swears anyone would be lucky to work with him"),
]
# Modelling Audition Job types
MODEL_AUDITION_JOBS = [
    _("Art"),
    _("Artistic Nude"),
    _("Catwalk Roles"),
    _("Commercial Roles"),
    _("Editorial Roles"),
    _("Fit Model Roles"),
    _("Fitness Model Roles"),
    _("Foot Model Roles"),
    _("Glamour Roles"),
    _("Hand Model Roles"),
    _("High Fashion Roles"),
    _("Lingerie Roles"),
    _("Parts Model Roles"),
    _("Print Roles"),
    _("Promotional Roles"),
    _("Sportswear Roles"),
    _("Swimwear Roles"),
]
# Freelance model work types
MODEL_FREELANCE_JOBS = [
    _("Art"),
    _("Artistic Nude"),
    _("Catwalk"),
    _("Commercial"),
    _("Editorial"),
    _("Fit"),
    _("Fitness"),
    _("Foot"),
    _("Glamour"),
    _("Hand"),
    _("High"),
    _("Instagram"),
    _("Lingerie"),
    _("OnlyFans"),
    _("Parts"),
    _("Print"),
    _("Promotional"),
    _("Sportswear"),
    _("Swimwear"),
]
# Fashion Magazines
FASHION_MAGAZINES = [

]
# Modelling job types
MODELLING_JOBS_ART = [
    _("Life Modelling Class"),
    _("Painter's Studio"),
    _("Photographer's Studio"),
    _("Sculpturer's Studio"),
]
MODELLING_JOBS_ARTISTIC_NUDE = [

]
MODELLING_JOBS_CATWALK = [
    
]
MODELLING_JOBS_COMMERCIAL = [
    
]
# E.g. "Fashion Brand: Balenciaga"
FASHION_BRANDS = [
    _("A.P.C."),
    _("Adidas"),
    _("Aldo"),
    _("Alexander McQueen"),
    _("Alexander Wang"),
    _("Amélie Pichard"),
    _("American Eagle Outfitters"),
    _("Armani"),
    _("Asics"),
    _("ASOS"),
    _("Audemars Piguet"),
    _("Ba&sh"),
    _("Balenciaga"),
    _("Balmain"),
    _("Banana Republic"),
    _("Berluti"),
    _("Bogner"),
    _("Bottega Veneta"),
    _("Breguet"),
    _("Brioni"),
    _("Brunello Cucinelli"),
    _("Bulgari"),
    _("Burberry"),
    _("C&A"),
    _("Calvin Klein"),
    _("Cartier"),
    _("Celine"),
    _("Chanel"),
    _("Chinti and Parker"),
    _("Chloé"),
    _("Chopard"),
    _("Chow Tai Fook"),
    _("Christian Dior"),
    _("Christian Louboutin"),
    _("Christopher Kane"),
    _("Claudie Pierlot"),
    _("Clergerie"),
    _("Coach"),
    _("Cole Haan"),
    _("Comme Des Garçons"),
    _("DELPOZO"),
    _("Desigual"),
    _("Diesel"),
    _("Dior"),
    _("DKNY"),
    _("Dolce & Gabbana"),
    _("Elie Saab"),
    _("Elie Tahari"),
    _("Emilio Pucci"),
    _("Eres"),
    _("Ermenegildo Zegna"),
    _("ESCADA"),
    _("Faith Connexion"),
    _("Fendi"),
    _("Fenty"),
    _("Fila"),
    _("Foot Locker Inc."),
    _("Forever 21"),
    _("Fossil"),
    _("Franck Muller"),
    _("Furla"),
    _("G-star"),
    _("GAP"),
    _("Giorgio Armani"),
    _("Givenchy"),
    _("Goyard"),
    _("Gucci"),
    _("H&M"),
    _("Hermès"),
    _("Hugo Boss"),
    _("Iro"),
    _("Isabel Marant"),
    _("IWC Schaffhausen"),
    _("Jacquemus"),
    _("Jaeger-Le Coultre"),
    _("Jérôme Dreyfuss"),
    _("Jil Sander"),
    _("Jimmy Choo"),
    _("Kate Spade"),
    _("Kenzo"),
    _("Lacoste"),
    _("Lanvin"),
    _("Lao Feng Xiang"),
    _("Lemaire"),
    _("Levi’s"),
    _("Loewe"),
    _("Longchamp"),
    _("Longines"),
    _("Loro Piana"),
    _("Louis Vuitton"),
    _("Lululemon"),
    _("Macy’s"),
    _("Maison Michel"),
    _("Manolo Blahnik"),
    _("Marc Jacobs"),
    _("Marcelo Burlon"),
    _("Margaret Howell"),
    _("Marni"),
    _("Max Mara"),
    _("MCM"),
    _("Michael Kors"),
    _("Missoni"),
    _("Miu Miu"),
    _("Moncler"),
    _("Moschino"),
    _("Moynat"),
    _("Net-a-Porter"),
    _("New Balance"),
    _("New Look"),
    _("Next"),
    _("Nicholas Kirkwood"),
    _("Nike"),
    _("Nine West"),
    _("Nordstrom"),
    _("Oakley"),
    _("Off White"),
    _("Old Navy"),
    _("Omega"),
    _("Oscar de la Renta"),
    _("Paco Rabanne"),
    _("Patagonia"),
    _("Patek Philippe"),
    _("Patou"),
    _("Paul Smith"),
    _("Paul Stuart"),
    _("Pink Shirtmaker"),
    _("Prada"),
    _("Primark"),
    _("Puma"),
    _("Ralph Lauren"),
    _("Ray-Ban"),
    _("Rimowa"),
    _("Rolex"),
    _("Rouje"),
    _("Salvatore Ferragamo"),
    _("Sisley"),
    _("Skechers"),
    _("Stella McCartney"),
    _("Steve Madden"),
    _("Stuart Weitzman"),
    _("Sunnei"),
    _("Swarovski"),
    _("Swatch"),
    _("Tag Heuer"),
    _("Ted Baker"),
    _("Temperley London"),
    _("The Kooples"),
    _("The North Face"),
    _("Thom Browne"),
    _("Tiffany & Co."),
    _("Tissot"),
    _("TJ Maxx"),
    _("TOD’s"),
    _("Tom Ford"),
    _("Tommy Hilfiger"),
    _("Topshop"),
    _("Tory Burch"),
    _("Under Armour"),
    _("UNIQLO"),
    _("Urban Outfitters"),
    _("Vacheron Constantin"),
    _("Valentino"),
    _("Vera Wang"),
    _("Victoria’s Secret"),
    _("Vivienne Westwood"),
    _("Yohji Yamamoto"),
    _("Yves Saint Laurent"),
    _("Zalando"),
    _("Zara"),
]
# Probably needs a better ranking classification
FASHION_WEEK_LOCATIONS_BIG_FOUR = [
    _("London"),
    _("Milan"),
    _("New York"),
    _("Paris"),
]
FASHION_WEEK_LOCATIONS_LARGE = [
    _("Australian"),
    _("Berlin"),
    _("India"),
    _("Seoul"),
    _("Shanghai"),
    _("Tokyo"),
    _("Venice"), 
]
FASHION_WEEK_LOCATIONS_MID = [
    _("Accra"),
    _("Alta Roma"),
    _("Arab"),
    _("Bangalore"),
    _("Barcelona"),
    _("Bulgarian"),
    _("Colombiamoda"),
    _("Columbus"),
    _("Copenhagen"),
    _("Dubai International"),
    _("Fiji"),
    _("Frankfurt"),
    _("Hong Kong"),
    _("Lagos"),
    _("MTC Windhoek"),
    _("New Zealand"),
    _("Nigeria"),
    _("Port of Spain"),
    _("Portland"),
    _("Stockholm"),
    _("Swahili"),
    _("Ukrainian"),   
]
# "You served as a {model_type} for {fashion_brand_or_client}"



# Musician Jobs
MUSICIAN_JOB_TYPE = [
    _("Band"),
    _("Solo Artist"),
]
# Band musician
MUSICIAN_BAND_ROLE = [
    _("Bassist"),
    _("Drummer"),
    _("Guitarist"),
    _("Keyboardist"),
    _("Singer"),
]
# Solo artist musician
MUSICIAN_SOLO_ARTIST_ROLE = [
    _("Cellist"),
    _("Guitarist"),
    _("Pianist"),
    _("Saxophonist"),
    _("Singer"),
    _("Violinist"),
]
MUSICIAN_SOLO_ARTIST_RECORD_LABEL = [
    _("Atrium Records"),
    _("Falcon Records"),
    _("United Beats"),
]


# Politician Jobs
POLITICIAN_COUNTRY = [
    _("United States"),
]
# - United States -
POLITICIAN_UNITED_STATES = [
    _("School Board Director"),
    _("Mayor"),
    _("Governor"),
    _("President"),
]
UNITED_STATES_SCHOOL_BOARD_DIRECTOR_PLATFORM = [
    _("Economy"),
    _("Education"),
    _("Environment"),
    _("Social Issues"),
]



# Professional Athlete Jobs
PROFESSIONAL_SPORTS_TYPES = [
    _("American Football"),
    _("Association Football"),
    _("Australian Rules Football"),
    _("Baseball"),
    _("Basketball"),
    _("Boxing"),
    _("Canadian Football"),
    _("Cricket"),
    _("Gaelic Football"),
    _("Golf"),
    _("Ice Hockey"),
    _("Rugby League"),
    _("Rugby Union"),
    _("Surfing"),
    _("Tennis"),
    _("Volleyball"),
]
# - American Football -
# American Football Teams
AMERICAN_FOOTBALL_TEAMS_NFC = [
    _("Arizona Cardinals"),
    _("Atlanta Falcons"),
    _("Carolina Panthers"),
    _("Chicago Bears"),
    _("Dallas Cowboys"),
    _("Detroit Lions"),
    _("Green Bay Packers"),
    _("Los Angeles Rams"),
    _("Minnesota Vikings"),
    _("New Orleans Saints"),
    _("New York Giants"),
    _("Philadelphia Eagles"),
    _("San Francisco 49ers"),
    _("Seattle Seahawks"),
    _("Tampa Bay Buccaneers"),
    _("Washington Commanders"),
]
AMERICAN_FOOTBALL_TEAMS_AFC = [
    _("Baltimore Ravens"),
    _("Buffalo Bills"),
    _("Cincinnati Bengals"),
    _("Cleveland Browns"),
    _("Denver Broncos"),
    _("Houston Texans"),
    _("Indianapolis Colts"),
    _("Jacksonville Jaguars"),
    _("Kansas City Chiefs"),
    _("Las Vegas Raiders"),
    _("Los Angeles Chargers"),
    _("Miami Dolphins"),
    _("New England Patriots"),
    _("New York Jets"),
    _("Pittsburgh Steelers"),
    _("Tennessee Titans"),
]
# Positions
AMERICAN_FOOTBALL_POSITIONS = [
    _("Safety"),
    _("Cornerback"),
    _("Outside Linebacker"),
    _("Middle Linebacker"),
    _("End"),
    _("Defensive Tackle"),
    _("Wide Receiver"),
    _("Offensive Tackle"),
    _("Offensive Guard"),
    _("Center"),
    _("Tight End"),
    _("Quarterback"),
    _("Wide Receiver"),
    _("Fullback / Running Back"),
    _("Halfback / Running Back"),
]
# - Association Football -
# Association Football Teams
ASSOCIATION_FOOTBALL_TEAMS = [
    _("Arsenal"),
    _("Aston Villa"),
    _("Bournemouth"),
    _("Brentford"),
    _("Brighton & Hove Albion"),
    _("Chelsea"),
    _("Crystal Palace"),
    _("Everton"),
    _("Fulham"),
    _("Leeds United"),
    _("Leicester City"),
    _("Liverpool"),
    _("Manchester City"),
    _("Manchester United"),
    _("Newcastle United"),
    _("Nottingham Forest"),
    _("Southampton"),
    _("Tottenham Hotspur"),
    _("West Ham United"),
    _("Wolverhampton Wanderers"),
]
# Positions
ASSOCIATION_FOOTBALL_POSITIONS = [
    _("Goalkeeper"),
    _("Full-Back"),
    _("Centre-Back"),
    _("Sweeper"),
    _("Wing-Back"),
    _("Defensive Midfielder"),
    _("Central Midfielder"),
    _("Attacking Midfielder"),
    _("Winger"),
    _("Forward"),
    _("Striker"),
]
# - Australian Rules Football -
# Australian Rules Football Teams
AUSTRALIAN_RULES_FOOTBALL_TEAMS = [
    _("Adelaide Crows"),
    _("Brisbane Lions"),
    _("Carlton Blues"),
    _("Collingwood Magpies"),
    _("Essendon Bombers"),
    _("Fremantle Dockers"),
    _("Geelong Cats"),
    _("Gold Coast Suns"),
    _("Greater Western Sydney Giants"),
    _("Hawthorn Hawks"),
    _("Melbourne Demons"),
    _("North Melbourne Kangaroos"),
    _("Port Adelaide Power"),
    _("Richmond Tigers"),
    _("St Kilda Saints"),
    _("Sydney Swans"),
    _("West Coast Eagles"),
    _("Western Bulldogs"),
]
# Positions
AUSTRALIAN_RULES_FOOTBALL_POSITIONS = [
    _("Left Forward Pocket"),
    _("Full Forward"),
    _("Right Forward Pocket"),
    _("Left Forward Flank"),
    _("Centre Half Forward"),
    _("Right Forward Flank"),
    _("Left Wing"),
    _("Centre"),
    _("Ruck Rover"),
    _("Ruck"),
    _("Rover"),
    _("Right Wing"),
    _("Left Back Flank"),
    _("Centre Half Back"),
    _("Right Back Flank"),
    _("Left Back Pocket"),
    _("Full Back"),
    _("Right Back Pocket"),
]
# - Baseball -
# Baseball Teams
BASEBALL_TEAMS = [

]
# Positions
BASEBALL_POSITIONS = [
    _("Pitcher"),
    _("Catcher"),
    _("First Base"),
    _("Second Base"),
    _("Third Base"),
    _("Shortstop"),
    _("Left Field"),
    _("Center Field"),
    _("Right Field"),
    _("Outfield"),
    _("Designated Hitter"),
]
# - Basketball -
# Basketball Teams
BASKETBALL_TEAMS = [

]
# Positions
BASKETBALL_POSITIONS = [
    _("Point Guard"),
    _("Shooting Guard"),
    _("Small Forward"),
    _("Power Forward"),
    _("Center"),
]
# - Boxing -
# Male Boxers
BOXERS_MALE = [

]
# Female Boxers
BOXERS_FEMALE = [

]
# - Canadian Football -
# Canadian Football Teams
CANADIAN_FOOTBALL_TEAMS = [

]
# Positions
CANADIAN_FOOTBALL_POSITIONS = [

]
# - Cricket -
# Cricket Teams
CRICKET_TEAMS = [

]
# Positions
CRICKET_POSITIONS = [

]
# - Gaelic Football -
# Gaelic Football Teams
GAELIC_FOOTBALL_TEAMS = [

]
# Positions
GAELIC_FOOTBALL_POSITIONS = [

]
# - Golf -
# Male Golfers
GOLFERS_MALE = [

]
# Female Golfers
GOLFERS_FEMALE = [

]
# - Ice Hockey -
# Ice Hockey Teams
ICE_HOCKEY_TEAMS = [

]
# Positions
ICE_HOCKEY_POSITIONS = [

]
# - Rugby League -
# Rugby League Teams
RUGBY_LEAGUE_TEAMS = [

]
# Positions
RUGBY_LEAGUE_POSITIONS = [

]
# - Rugby Union -
# Rugby Union Teams
RUGBY_UNION_TEAMS = [

]
# Positions
RUGBY_UNION_POSITIONS = [

]
# - Surfing -
# Male Surfers
SURFERS_MALE_PRO = [
    _("Filipe Toledo"),
    _("Italo Ferreira"),
    _("Jack Robinson"),
    _("Ethan Ewing"),
    _("Kanoa Igarashi"),
    _("Miguel Pupo"),
    _("Griffin Colapinto"),
    _("Caio Ibelli"),
    _("Connor O'Leary"),
    _("Callum Robson"),
    _("Samuel Pupo"),
    _("John John Florence"),
    _("Matthew McGillivray"),
    _("Jordy Smith"),
    _("Kelly Slater"),
    _("Barron Mamiya"),
    _("Nat Young"),
    _("Jake Marshall"),
    _("Yago Dora"),
    _("Kolohe Andino"),
    _("Jadson Andre"),
    _("Seth Moniz"),
    _("Jackson Baker"),
    _("Gabriel Medina"),
]
SURFERS_MALE_CHALLENGER = [

]
SURFERS_MALE_QUALIFYING = [

]
SURFERS_MALE_JUNIOR = [

]
# Female Surfers
SURFERS_FEMALE_PRO = [
    _("Stephanie Gilmore"),
    _("Carissa Moore"),
    _("Johanne Defay"),
    _("Tatiana Weston-Webb"),
    _("Brisa Hennessy"),
    _("Lakey Peterson"),
    _("Courtney Conlogue"),
    _("Tyler Wright"),
    _("Gabriela Bryan"),
    _("Isabella Nichols"),
    _("Caroline Marks"),
    _("Sally Fitzgibbons"),
]
SURFERS_FEMALE_CHALLENGER = [

]
SURFERS_FEMALE_QUALIFYING = [

]
SURFERS_FEMALE_JUNIOR = [

]

# - Tennis -
# Male Tennis players
TENNIS_PLAYERS_MALE = [
    _("Carlos Alcaraz"),
    _("Rafael Nadal"),
    _("Casper Ruud"),
    _("Daniil Medvedev"),
    _("Stefanos Tsitsipas"),
    _("Alexander Zverev"),
    _("Novak Djokovic"),
    _("Andrey Rublev"),
    _("Felix Auger-Aliassime"),
    _("Taylor Fritz"),
    _("Hubert Hurkacz"),
    _("Jannik Sinner"),
    _("Cameron Norrie"),
    _("Matteo Berrettini"),
    _("Pablo Carreno Busta"),
    _("Marin Čilić"),
    _("Frances Tiafoe"),
    _("Karen Khachanov"),
    _("Denis Shapovalov"),
    _("Nick Kyrgios"),
    _("Diego Schwartzman"),
    _("Roberto Bautista Agut"),
    _("Lorenzo Musetti"),
    _("Alex De Minaur"),
    _("Holger Rune"),
    _("Daniel Evans"),
    _("Borna Coric"),
    _("Miomir Kecmanovic"),
    _("Francisco Cerundolo"),
    _("Tommy Paul"),
    _("Alejandro Davidovich Fokina"),
    _("Grigor Dimitrov"),
    _("Sebastian Korda"),
    _("Maxime Cressy"),
    _("Botic Van De Zandschulp"),
    _("Reilly Opelka"),
    _("Yoshihito Nishioka"),
    _("Alexander Bublik"),
    _("Sebastian Baez"),
    _("Albert Ramos-Vinolas"),
    _("Gael Monfils"),
    _("Adrian Mannarino"),
    _("Emil Ruusuvuori"),
    _("Brandon Nakashima"),
    _("Jack Draper"),
    _("Alex Molcan"),
    _("John Isner"),
    _("Lorenzo Sonego"),
    _("Andy Murray"),
    _("Jenson Brooksby"),
    _("Arthur Rinderknech"),
    _("Filip Krajinovic"),
    _("David Goffin"),
    _("Oscar Otte"),
    _("Pedro Cachin"),
    _("J.J. Wolf"),
    _("Jaume Munar"),
    _("Marcos Giron"),
    _("Fabio Fognini"),
    _("Aslan Karatsev"),
    _("Pedro Martinez"),
    _("Marc-Andrea Huesler"),
    _("Benjamin Bonzi"),
    _("Corentin Moutet"),
    _("Mackenzie McDonald"),
    _("Thiago Monteiro"),
    _("Constant Lestienne"),
    _("Daniel Elahi Galan"),
    _("Quentin Halys"),
    _("João Sousa"),
    _("Tallon Griekspoor"),
    _("Ilya Ivashka"),
    _("Federico Coria"),
    _("Richard Gasquet"),
    _("Laslo Djere"),
    _("Mikael Ymer"),
    _("Alejandro Tabilo"),
    _("Jiri Lehecka"),
    _("Bernabe Zapata Miralles"),
    _("Roberto Carballes Baena"),
    _("Radu Albot"),
    _("Kamil Majchrzak"),
    _("Hugo Gaston"),
    _("SoonWoo Kwon"),
    _("Jordan Thompson"),
    _("Cristian Garin"),
    _("Dusan Lajovic"),
    _("Chun-Hsin Tseng"),
    _("Tomas Martin Etcheverry"),
    _("Taro Daniel"),
    _("Thanasi Kokkinakis"),
    _("Hugo Dellien"),
    _("Roman Safiullin"),
    _("Nikoloz Basilashvili"),
    _("Nuno Borges"),
    _("Pavel Kotov"),
    _("Zhizhen Zhang"),
    _("Alexei Popyrin"),
    _("Facundo Bagnis"),
    _("Christopher O'Connell"),
]
# Female Tennis players
TENNIS_PLAYERS_FEMALE = [
    _("Iga Swiatek"),
    _("Ons Jabeur"),
    _("Jessica Pegula"),
    _("Coco Gauff"),
    _("Maria Sakkari"),
    _("Caroline Garcia"),
    _("Aryna Sabalenka"),
    _("Daria Kasatkina"),
    _("Veronika Kudermetova"),
    _("Simona Halep"),
    _("Madison Keys"),
    _("Paula Badosa"),
    _("Belinda Bencic"),
    _("Danielle Collins"),
    _("Beatriz Haddad Maia"),
    _("Petra Kvitova"),
    _("Anett Kontaveit"),
    _("Jelena Ostapenko"),
    _("Liudmila Samsonova"),
    _("Ekaterina Alexandrova"),
    _("Barbora Krejcikova"),
    _("Elena Rybakina"),
    _("Amanda Anisimova"),
    _("Shuai Zhang"),
    _("Qinwen Zheng"),
    _("Martina Trevisan"),
    _("Victoria Azarenka"),
    _("Marie Bouzkova"),
    _("Kaia Kanepi"),
    _("Elise Mertens"),
    _("Aliaksandra Sasnovich"),
    _("Karolina Pliskova"),
    _("Irina-Camelia Begu"),
    _("Ajla Tomljanovic"),
    _("Jil Teichmann"),
    _("Alize Cornet"),
    _("Sloane Stephens"),
    _("Sorana Cirstea"),
    _("Petra Martic"),
    _("Leylah Fernandez"),
    _("Alison Riske-Amritraj"),
    _("Shelby Rogers"),
    _("Naomi Osaka"),
    _("Anastasia Potapova"),
    _("Bernarda Pera"),
    _("Bianca Andreescu"),
    _("Anhelina Kalinina"),
    _("Ana Bogdan"),
    _("Katerina Siniakova"),
    _("Mayar Sherif"),
    _("Madison Brengle"),
    _("Xiyu Wang"),
    _("Yulia Putintseva"),
    _("Daria Saville"),
    _("Magda Linette"),
    _("Alison Van Uytvanck"),
    _("Garbine Muguruza"),
    _("Diane Parry"),
    _("Anna Bondar"),
    _("Claire Liu"),
    _("Lucia Bronzetti"),
    _("Lin Zhu"),
    _("Anna Kalinskaya"),
    _("Maryna Zanevska"),
    _("Marta Kostyuk"),
    _("Jule Niemeier"),
    _("Sara Sorribes Tormo"),
    _("Danka Kovinic"),
    _("Camila Giorgi"),
    _("Tatjana Maria"),
    _("Donna Vekic"),
    _("Rebecca Marino"),
    _("Nuria Parrizas Diaz"),
    _("Linda Fruhvirtova"),
    _("Tereza Martincova"),
    _("Emma Raducanu"),
    _("Viktorija Golubic"),
    _("Jasmine Paolini"),
    _("Elisabetta Cocciaretto"),
    _("Panna Udvardy"),
    _("Anna Blinkova"),
    _("Lauren Davis"),
    _("Yue Yuan"),
    _("Dalma Galfi"),
    _("Julia Grabher"),
    _("Camila Osorio"),
    _("Harriet Dart"),
    _("Kaja Juvan"),
    _("Tamara Zidansek"),
    _("Tamara Korpatsch"),
    _("Linda Noskova"),
    _("Viktoriya Tomova"),
    _("Qiang Wang"),
    _("Varvara Gracheva"),
    _("Oceane Dodin"),
    _("Elena-Gabriela Ruse"),
    _("Aleksandra Krunic"),
    _("Dayana Yastremska"),
    _("Angelique Kerber"),
    _("Kamilla Rakhimova"),
]
# - Volleyball -
# Volleyball Teams
VOLLEYBALL_TEAMS = [

]
# Positions
VOLLEYBALL_POSITIONS = [

]


# Street Hustler Jobs:
# Streets
STREET_HUSTLE_STREET_NAMES = [
    _("Taylor Street"),
    _("Wall Street"),
    _("Woodland Drive"),
    _("8th Street"),
    _("Bridle Court"),
    _("Adams Avenue"),
    _("5th Street South"),
    _("East Street"),
    _("Valley View Road"),
    _("Jones Street"),
    _("Sycamore Drive"),
    _("Chestnut Street"),
    _("Cedar Street"),
    _("Jackson Avenue"),
    _("Lincoln Avenue"),
    _("Inverness Drive"),
    _("Fieldstone Drive"),
    _("Cross Street"),
    _("Westminster Drive"),
    _("Primrose Lane"),
    _("Canal Street"),
    _("Grove Street"),
    _("8th Street West"),
    _("Hill Street"),
    _("Route 4"),
    _("Locust Street"),
    _("3rd Street West"),
    _("Buttonwood Drive"),
    _("Pearl Street"),
    _("B Street"),
    _("Fairview Road"),
    _("Bridge Street"),
    _("Orange Street"),
    _("Holly Drive"),
    _("William Street"),
    _("Clark Street"),
    _("Jackson Street"),
    _("Garfield Avenue"),
    _("Sycamore Street"),
    _("Somerset Drive"),
    _("Bridle Lane"),
    _("North Avenue"),
    _("Lexington Court"),
    _("6th Street North"),
    _("Park Drive"),
    _("Walnut Street"),
    _("Dogwood Drive"),
    _("Highland Drive"),
    _("Cottage Street"),
    _("9th Street"),
]
# Hustles
STREET_HUSTLES = [
    _("Busker"),
    _("Panhandler"),
    _("Scam Artist"),
    _("Street Performer"),
]
# - Busker -
# Instruments
BUSKER_INSTRUMENTS = [
    _("Ash Guitar"),
    _("Silver Plastic Keyboard"),
]
# Music type
BUSKER_MUSIC_TYPES = [
    _("Classic Rock"),
    _("Reggae"),
    _("Romantic"),
    _("Pop"),
    _("Funk"),
    _("Polka"),
    _("Country"),
    _("Bluegrass"),
    _("Renaissance"),
    _("New age"),
    _("Adult contemporary"),
    _("House music"),
    _("Synth-pop"),
    _("World music"),
    _("Funk carioca"),
    _("Bossa nova"),
    _("Indie"),
    _("Elevator music"),
    _("Worship"),
    _("Kawaii metal"),
    _("Grunge"),
    _("Punk rock"),
    _("Screamo"),
    _("Emo pop"),
    _("Disco"),
    _("Peaceful"),
    _("Classical"),
    _("Peruvian"),
    _("Jazz"),
    _("Folk"),
    _("Blues"),
]
# Attire
BUSKER_ATTIRE_MALE = [
    _(""),
]
BUSKER_ATTIRE_FEMALE = [
    _("Petticoat skirt"),
    _("Trenchcoat"),
    _("Angel costume"),
    _("Black turtleneck"),
    _("Dirndl dress"),
    _("Lingerie"),
    _("Mask"),
    _("Devil costume"),
    _("Poncho"),
    _("Swimwear"),
    _("Evening dress"),
    _("Business suit"),
]
# Collection box
BUSKER_COLLECTION_BOXES = [
    _("Top hat"),
    _("Raggedy knit cap"),
    _("Shoe box"),
    _("Tip jar"),
    _("Music instrument case"),
    _("Gas station soda cup"),
    _("Glass fishbowl"),
    _("Crusty tupperware container"),
    _("Rusty bucket"),
    _("Baseball cap"),
    _("Coffee tin"),
    _("Backpack"),
    _("Hobo stick"),
]
# - Panhandler - 
# Props
PANHANDLER_PROPS = [
    _("Hazmat suit"),
    _("Straw hat"),
    _("Hobo sack"),
    _("Tattered suit and tie"),
    _("Walker"),
    _("Eviction notice"),
    _("Plaster cast"),
    _("Arm sling"),
    _("Matted fur coat"),
]
# Signs. > call these between quotation marks "{panhandler_signs}"
PANHANDLER_SIGNS = [
    _("Let's do lunch, U buy"),
    _("Will take insults for money"),
    _("Free Hugs!"),
    _("Need money for food"),
    _("I'm too sober for this"),
    _("Will picket your boss' house..."),
    _("I'll let you spank me for $1"),
    _("Saving up for a better life"),
    _("Psychiatric help: $1"),
    _("I need tree fiddy..."),
]
# Collection box
PANHANDLER_COLLECTION_BOXES = [
    _("Garbage can lid"),
    _("Paper bag"),
    _("Red Solo cup"),
    _("Tattered picnic basket"),
    _("Coffee canister"),
    _("Empty MacBook Pro box"),
    _("Cast-iron skillet"),
    _("Duffel bag"),
    _("Plastic shopping bag"),
]
# Strategy
PANHANDLER_STRATEGIES = [
    _("Hang outside a halfway house"),
    _("Go to a packed convention centre"),
    _("Hang around the entrance to a mall"),
    _("Rush up to pedestrians"),
    _("Sit outside a train station"),
    _("Walk around a farmers market"),
    _("Pass out on the street"),
    _("Sit in front of a church on Sunday"),
    _("Approach people leaving a concert hall"),
    _("Stand on a corner known for drug dealing"),
]



#------------------------------------------------------------------
# Suck-ups
# School suck-ups:
#   You left a gift card for Massage Envy on your {teacher_job}, {teacher_name}'s desk.
#   You let your teacher, {teacher_name}, know how much you enjoy being {his_her} pet.
#   You passed out papers for your teacher, {teacher_name}.
#   You volunteered to stay after school to clean your {teacher_job (history teacher etc)}, {teacher name}'s, classroom.
#   You told your {teacher_job}, {teacher_name}, about some classmates who you know cheated on their homework
#   You told your {teacher_job}, {teacher_name}, that you truly hope {he_she} has an amazing weekend.
#   You added your {teacher_job}, {teacher_name}, on Snapchat.
#   You drew a portrait of your {teacher_job}, {teacher_name}, and gave it to {him_her}.

#------------------------------------------------------------------
# Sexualities

SEXUALITY = [
    _("Straight"),
    _("Bi"),
    _("Gay"),
]

#------------------------------------------------------------------
# Identity Genders
IDENTITY_GENDER_FEMALE = [
    _("Cisgender"),
    _("Genderqueer"),
    _("Non-Binary"),
    _("Transgender Male"),
]
IDENTITY_GENDER_MALE = [
    _("Cisgender"),
    _("Genderqueer"),
    _("Non-Binary"),
    _("Transgender Female"),
]

#------------------------------------------------------------------
# Social media

# Social media posts:
# Nb. There seems to be an issue in the original where the number of new followers from a viral post can be unrealistically low. E.g. Over 20,000 likes but 11 follows. suggest having a minimum percentage, otherwise it's not 'viral' its just bot likes 

# Instagram
# Challenges = 'You recorded a video of yourself doing the '{challenges}' and posted it on Instagram. 
CHALLENGES = [
    _("Ice Bucket Challenge"),
    _(""),
]
# Dance videos = 'You recorded a video of yourself {dance_video_dances} to {dance_video_songs} and posted it to Instagram.
DANCE_VIDEO_DANCES = [
    _("tap dancing"),
]
DANCE_VIDEO_SONGS = [
    _("a P!nk song"),
]
# Family photos = 'You posted {family_photos} family photo on Instagram.
FAMILY_PHOTOS = [
    _("a cute"),
    _("an embarrasing"),
]
# Food photos = 'You posted a picture of {food_photos} on Instagram.
FOOD_PHOTOS = [
    _("a photo of a cake you found on the internet"),
    _("your nasty snack"),
]
# Memes = 'You shared {memes} meme on Instagram.
MEMES = [
    _("a ridiculous"),
]
# Motivational Quotes = 'You posted {quotes_adjective} quote about {quotes_topic}
QUOTES_ADJECTIVE = [
    _("an inspirational"),
]
QUOTES_TOPIC = [
    _("relationships"),
]
# Political Video = 'You posted on Instagram {political_videos}.
POLITICAL_VIDEOS = [
    _("promoting your political ideology"),
    _("campaigning for your political ideology"),
    _("supporting your favourite political candidate"),
]
# Poll = 'You posted a poll on Instagram asking your followers "{polls}".
POLLS = [
    _("Which social media platform is the best?"),
    _("What is the best song?"),
]
# Random Video = 'You recorded {random_video_adjectives} video of {random_video_topics} and posted it on Instagram.
RANDOM_VIDEO_ADJECTIVES = [
    _("an outlandish"),
]
RANDOM_VIDEO_TOPICS = [
    _("yourself talking with accents"),
]
# Reshare Celebrity = 'You shared {reshare_celebrity_media} that {celebrity} posted on Instagram. Use a random choice between all the celebrity name lists in place of {celebrity}
RESHARE_CELEBRITY_MEDIA = [
    _("a meme"),
    _("a photo"),
    _("a picture"),
    _("a reel"),
    _("a story"),
    _("a video"),
]
# Reshare Friend = 'You shared {reshare_friend_media} that your friend posted on Instagram. 
RESHARE_FRIEND_MEDIA = [
    _("a meme"),
    _("a photo"),
    _("a picture"),
    _("a reel"),
    _("a story"),
    _("a video"),
]
# Reshare Celebrity = 'You shared {reshare_musician_media} that {celebrity_musician} posted on Instagram. Use a random choice between the {celebrity_musician_male}, {celebrity_musician_female}, and {celebrity_band} lists in the celebrity section
RESHARE_MUSICIAN_MEDIA = [
    _("a meme"),
    _("a photo"),
    _("a picture"),
    _("a recording session"),
    _("a reel"),
    _("a song"),
    _("a story"),
    _("a video"),
    _("their latest album cover"),  
]
# Selfies = 'You posted {selfies} on Instagram.
SELFIES = [
    _("a duck face selfie"),
    _("a selfie pulling a funny face"),
    _("a professional looking selfie"),
]
# Sexy Pics = 'You posted {sexy_pics_male} on Instagram.
SEXY_PICS_MALE = [
    _("a risqué selfie of yourself"),
    _("a photo of yourself clearly showing your muscles"),
    _("a selfie gazing through the lens dreamily"),
    _("a gym selfie while working out"),
]
# Sexy Pics = 'You posted {sexy_pics_female} on Instagram.
SEXY_PICS_FEMALE = [
    _("a risqué selfie of yourself"),
    _("a side-on mirror selfie emphasising your tight dress"),
    _("an over-the-shoulder bikini selfie showing your bum in the background"),
    _("a gym selfie while working out"),
]
# Skit Video = 'You {and your friend made a slapstick skit} video and posted it on Instagram.
SKIT_VIDEOS = [
    _("and your friend made a slapstick skit"),
]
# Social Justice Video = 'You posted on Instagram {social_justice_videos}.
SOCIAL_JUSTICE_VIDEOS = [
    _("supporting social justice"),
]
# Stories = 'You posted a story {social_stories} on Instagram.
SOCIAL_STORIES = [
    _("about your weird day"),
]
# Thirst Traps = 'You posted a photo on Instagram of yourself {thirst_traps}.
THIRST_TRAPS = [
    _("holding a water pistol and wearing white underwear"),
    _("looking off into the distance and only wearing a towel"),
    _("taking a shower through half-fogged glass"),
    _("wearing a sexy bathing suit while taking a shower"),
    _("wearing just a pair of jeans while mowing the lawn"),
    _("wearing just a t-shirt"),
    _("wearing just a t-shirt while laying on the dinner table"),
    _("wearing nothing while making a duck face"),
    _("wearing nothing while riding an inflatable Orca in the swimming pool"),
    _("wearing only sushi while reading a book"),
    _("wearing practically nothing while laying in bed"),
    _("wearing practically nothing while posing in the bathroom mirror"),
    _("wearing your birthday suit while pretending to sleep"), 
      
]
THIRST_TRAPS_FEMALE = [
    _("not wearing your bikini bottoms while laying by the pool"),
    _("wearing a thong while eating a cucumber"),
    _("wearing a thong while sprawled out on the floor"),
    _("wearing edible underwear while dancing at home"),
    _("wearing edible underwear while laying on the dinner table"),
    _("wearing just a t-shirt while eating a cucumber"),     
]
THIRST_TRAPS_MALE = [
    _("as 'The Naked Chef'"),
    _("wearing a suit while eating a cherry"),
    _("wearing just a pair of jeans while mowing the lawn"),
    _("flexing your muscles while shaving your beard"),   
]
# Your Travels = 'You posted {social_travel_media} {social_travel} on Instagram
SOCIAL_TRAVEL_MEDIA = [
    _("some magnificent art photos"),
    _("a stunning night video"),
    _("a video of yourself walking through markets"),
]
SOCIAL_TRAVEL = [
    _("from your last vacation"),
    _("from your trip to Paris"),
    _("you took on your Hawaiian trip"),
]
# Vlog = 'You recorded {vlog} and posted it on Instagram.
VLOG_POSTS = [
    _("your daily life shenanigans as a vlog"), 
    _("a vlog of your morning routine"),
]

# Social media handles: (for when 'someone called {@offensivebeavis} replied to your post, saying {you look sinister})

SOCIAL_HANDLES = [
   _("@2OldForThis"),
   _("@TheTroubleMakers"),
   _("@joe_not_exotic"),
   _("@shaquille.oatmeal"),
   _("@RenegadeMaster"),
   _("@viewer_discretion_advised"),
   _("@FunnyCatVidz"),
   _("@CharliDamelioForPresident"),
   _("@everythingbagelwithvegancreamcheese"),
   _("@name_is_in_use"),
   _("@i_dont_dance"),
   _("@builtdifferent"),
   _("@shadowbanned"),
   _("@not_my_idea"),
   _("@down_with_the_kids"),
   _("@amicoolyet"),
   _("@Addison_Rae_Of_Sunshine"),
   _("@im_an_accountant"),
   _("@IYELLALOT"),
   _("@FrostedCupcake"),
   _("@Avocadorable"),
   _("@MrsDracoMalfoy"),
   _("@MrsChalamet"),
   _("@MrsStyles"),
   _("@CourtesyFlush"),
   _("@MomsSpaghetti"),
   _("@just_a_teen"),
   _("@GenZWarrior"),
   _("@what_does_this_button_do"),
   _("@not_funny"),
   _("@DestinysGrandchild"),
   _("@champain"),
   _("@AspiringInfluencer"),
   _("@ClassyBadassy"),
   _("@severusvape"),
   _("@RuleFollower"),
   _("@Lizzos_Flute"),
   _("@urcutejeans"),
   _("@guess_who"),
   _("@insert_name_here"),
   _("@InstagramM0del"),
   _("@baeconandeggz"),
   _("@look_mom"),
   _("@botaccount"),
   _("@QuarQueen"),
   _("@Reese_Withoutaspoon"),
   _("@ReeseWithafork"),
   _("@ImageNotUploaded"),
   _("@No_Feet_Pics"),
   _("@wherearethetomatoes"),
   _("@TequilaMockingbird"),
   _("@the_other_name_were_taken"),
   _("@not_my_first_choice"),
   _("@PaintMeLikeOneOfYourFrenchGirls"),
   _("@Hot_Name_Here"),
   _("@InstagramHubby"),
   _("@BasicBeach"),
   _("@thot_patrol"),
   _("@my_anaconda_does"),
   _("@kim_chi"),
   _("@username_copied"),
   _("@Ariana_Grandes_Ponytail"),
   _("@definitely_not_an_athlete"),
   _("@will_pay_extra_for_guac"),
   _("@not_my_1st_rodeo"),
   _("@coolshirtbra"),
   _("@DMmeforcompliments"),
   _("@baecon"),
   _("@boneappleteeth"),
   _("@valid8me"),
   _("@personallyvictimizedbyreginageorge"),
   _("@been_there_done_that"),
   _("@hi_future_employers"),
   _("@chalametbmybae"),
   _("@NorthWestsAssistant"),
   _("@hotgirlbummer"),
]

# Negative social responses: (E.g. 'someone called {@offensivebeavis} replied to your post, saying {you look sinister})
NEGATIVE_SOCIAL_RESPONSES = [
    _("you look sinister"),
    _("your thoughts are absurd"),
]

# If you choose to meet someone from social media and they agree
# E.g. {@offensivebeavis} has agreed to meet you at {a campsite}; use random choice {urban_locations}, {rural_locations}, {natural_locations} lists in place of {a campsite}




#------------------------------------------------------------------
# Instruments

# Accordian
# Banjo
# Bass Guitar
# Cello
# Didgeridoo
# Drums
# Flute
# Guitar
# Harmonica
# Harp
# Kazoo
# Keyboard
# Organ
# Pan Flute
# Piano
# Recorder
# Saxophone
# Steel Drum
# Tambourine
# Triangle
# Trombone
# Trumpet
# Tuba
# Violin

#------------------------------------------------------------------
# Middle School and High School cliques:

# Artsy Kids
# Band Geeks
# Brainy Kids
# Drama Kids
# Gamers
# Goths
# Hipsters
# Loners
# Mean Girls
# Nerds
# Normals
# Popular Kids
# Skaters
# Social Floaters
# Talented Kids
# Troublemakers
# Weebs

#------------------------------------------------------------------
# Middle School activities:

# Animal Rights Club
# Basketball Team
# Cheerleading Team
# Choir
# Creative Writing Club
# Cross Country Team
# Diving Team
# Drama Club
# Field Hockey Team
# Gymnastics Team
# History Club
# Lacrosse Team
# Math Club
# Recycling Club
# Science Club
# Soccer Team
# Swim Team
# Tennis Team
# Track Team
# Video Games Club
# Volleyball Team
# Yearbook Club


# High School activities:

# Baking Club
# Basketball Team
# Cheerleading Team
# Computer Science Club
# Concert Band
# Cross Country Team
# Diving Team
# Drama Club
# Golf Team
# Gymnastics Team
# Handball Team
# Skateboarding Club
# Soccer Team
# Student Council
# Swim Team
# Tennis Team
# Track Team
# Tutoring Club
# Video Games Club
# Volleyball Team
# Woodworkers Club
# Yearbook Club

#------------------------------------------------------------------

# Books
BOOKS = [
    _("The Dictionary"),
]
BOOKS_CHILD = [
    _("Where the Wild Things Are"),
    _("Goodnight Moon"),
    _("Brown Bear, Brown Bear, What Do You See?"),
    _("The Snowy Day"),
    _("If You Give A Mouse A Cookie"),
    _("Stellaluna"),
    _("The Very Hungry Caterpillar"),
]
BOOKS_TEEN = [
    _(""),
]

#------------------------------------------------------------------

# Movies

MOVIES = [
    _("20,000 Leagues Under the Sea"),
    _("2001: A Space Odyssey"),
    _("Aladdin"),
    _("Alice in Wonderland"),
    _("All Quiet on the Western Front"),
    _("Aquaman"),
    _("Armageddon"),
    _("Avatar"),
    _("Avengers: Age of Ultron"),
    _("Avengers: Endgame"),
    _("Avengers: Infinity War"),
    _("Back to the Future"),
    _("Bambi"),
    _("Beauty and the Beast"),
    _("Ben-Hur"),
    _("Black Panther"),
    _("Boom Town"),
    _("Butch Cassidy and the Sundance Kid"),
    _("Captain America: Civil War"),
    _("Captain Marvel"),
    _("Cavalcade"),
    _("Cinderella"),
    _("Cinerama Holiday"),
    _("City Lights"),
    _("Cleopatra"),
    _("Demon Slayer: Mugen Train"),
    _("Despicable Me 3"),
    _("Diamonds Are Forever"),
    _("Die Hard with a Vengeance"),
    _("Douglas Fairbanks in Robin Hood"),
    _("Duel in the Sun"),
    _("E.T. the Extra-Terrestrial"),
    _("Easter Parade"),
    _("Fatal Attraction"),
    _("Fiddler on the Roof"),
    _("Finding Dory"),
    _("For Heaven's Sake"),
    _("For Whom the Bell Tolls"),
    _("Forever Amber"),
    _("Frankenstein"),
    _("From Russia with Love"),
    _("Frozen"),
    _("Frozen II"),
    _("Funny Girl"),
    _("Furious 7"),
    _("Ghost"),
    _("Going My Way"),
    _("Goldfinger"),
    _("Gone with the Wind"),
    _("Grease"),
    _("Harry Potter and the Deathly Hallows – Part 2"),
    _("Harry Potter and the Goblet of Fire"),
    _("Harry Potter and the Philosopher's Stone"),
    _("Hawaii"),
    _("How the West Was Won"),
    _("I'm No Angel"),
    _("Incredibles 2"),
    _("Independence Day"),
    _("Indiana Jones and the Last Crusade"),
    _("Indiana Jones and the Temple of Doom"),
    _("Intolerance"),
    _("Iron Man 3"),
    _("It Happened One Night"),
    _("Jaws"),
    _("Joker"),
    _("Jurassic Park"),
    _("Jurassic World"),
    _("Jurassic World Dominion"),
    _("Jurassic World: Fallen Kingdom"),
    _("King Kong"),
    _("King Solomon's Mines"),
    _("Lady and the Tramp"),
    _("Lawrence of Arabia"),
    _("Love Story"),
    _("Mary Poppins"),
    _("Mickey"),
    _("Minions"),
    _("Mission: Impossible 2"),
    _("Mister Roberts"),
    _("Mom and Dad"),
    _("Moonraker"),
    _("Mrs. Miniver"),
    _("Mutiny on the Bounty"),
    _("My Fair Lady"),
    _("One Hundred and One Dalmatians"),
    _("Peter Pan"),
    _("Pinocchio"),
    _("Pirates of the Caribbean: At World's End"),
    _("Pirates of the Caribbean: Dead Man's Chest"),
    _("Pirates of the Caribbean: On Stranger Tides"),
    _("Psycho"),
    _("Quo Vadis"),
    _("Raiders of the Lost Ark"),
    _("Rain Man"),
    _("Rear Window"),
    _("Return of the Jedi"),
    _("Rocky"),
    _("Rocky II"),
    _("Rogue One: A Star Wars Story"),
    _("Samson and Delilah"),
    _("San Francisco"),
    _("Sergeant York"),
    _("She Done Him Wrong"),
    _("Shrek 2"),
    _("Skyfall"),
    _("Snow White and the Seven Dwarfs"),
    _("Song of the South"),
    _("South Pacific"),
    _("Spartacus"),
    _("Spider-Man: Far From Home"),
    _("Spider-Man: No Way Home"),
    _("Star Wars"),
    _("Star Wars: Episode I – The Phantom Menace"),
    _("Star Wars: The Force Awakens"),
    _("Star Wars: The Last Jedi"),
    _("Star Wars: The Rise of Skywalker"),
    _("Sunny Side Up"),
    _("Swiss Family Robinson"),
    _("Terminator 2: Judgment Day"),
    _("The Avengers"),
    _("The Bells of St. Mary's"),
    _("The Best Years of Our Lives"),
    _("The Bible: In the Beginning"),
    _("The Big Parade"),
    _("The Birth of a Nation"),
    _("The Bridge on the River Kwai"),
    _("The Broadway Melody"),
    _("The Covered Wagon"),
    _("The Dark Knight"),
    _("The Dark Knight Rises"),
    _("The Empire Strikes Back"),
    _("The Exorcist"),
    _("The Fate of the Furious"),
    _("The Four Horsemen of the Apocalypse"),
    _("The French Connection"),
    _("The Godfather"),
    _("The Godfather: Part II"),
    _("The Godfather: Part III"),
    _("The Graduate"),
    _("The Greatest Show on Earth"),
    _("The Hobbit: An Unexpected Journey"),
    _("The Jungle Book"),
    _("The Lion King"),
    _("The Longest Day"),
    _("The Lord of the Rings: The Return of the King"),
    _("The Lord of the Rings: The Two Towers"),
    _("The Merry Widow"),
    _("The Miracle Man"),
    _("The Red Shoes"),
    _("The Robe"),
    _("The Sea Hawk"),
    _("The Sign of the Cross"),
    _("The Singing Fool"),
    _("The Snake Pit"),
    _("The Sound of Music"),
    _("The Sting"),
    _("The Ten Commandments"),
    _("The Towering Inferno"),
    _("This Is Cinerama"),
    _("This Is the Army"),
    _("Titanic"),
    _("Top Gun"),
    _("Top Gun: Maverick"),
    _("Toy Story"),
    _("Toy Story 3"),
    _("Toy Story 4"),
    _("Transformers: Age of Extinction"),
    _("Transformers: Dark of the Moon"),
    _("Unconquered"),
    _("Way Down East"),
    _("West Side Story"),
    _("White Christmas"),
    _("Who's Afraid of Virginia Woolf?"),
    _("Wings"),
    _("You Can't Take It With You"),
    _("Zootopia"),
]
MOVIES_CHILD = [
    _("Big Boy's Little Adventure"),
]
MOVIES_TEEN = [
    _(""),
]
# Movies by category / genre (with year in the list) for 'we watched a comedy movie called {movie-name, from movie-year}, it {made me laugh}/{made us cry}/{was hilarious!}
MOVIES_ANIMATED = [
    _("Big Hero 6, from 2014"),
    _("Brave, from 2012"),
    _("Cars 2, from 2011"),
    _("Coco, from 2017"),
    _("Despicable Me, from 2010"),
    _("Despicable Me 2, from 2013"),
    _("Despicable Me 3, from 2017"),
    _("Finding Dory, from 2016"),
    _("Finding Nemo, from 2003"),
    _("Frozen, from 2013"),
    _("Frozen II, from 2019"),
    _("Hotel Transylvania 3: Summer Vacation, from 2018"),
    _("How to Train Your Dragon 2, from 2014"),
    _("How to Train Your Dragon: The Hidden World, from 2019"),
    _("Ice Age: Continental Drift, from 2012"),
    _("Ice Age: Dawn of the Dinosaurs, from 2009"),
    _("Ice Age: The Meltdown, from 2006"),
    _("Incredibles 2, from 2018"),
    _("Inside Out, from 2015"),
    _("Kung Fu Panda, from 2008"),
    _("Kung Fu Panda 2, from 2011"),
    _("Madagascar, from 2005"),
    _("Madagascar 3: Europe's Most Wanted, from 2012"),
    _("Madagascar: Escape 2 Africa, from 2008"),
    _("Minions, from 2015"),
    _("Minions: The Rise of Gru , from 2022"),
    _("Moana, from 2016"),
    _("Monsters University, from 2013"),
    _("Monsters, Inc., from 2001"),
    _("Ne Zha, from 2019"),
    _("Puss in Boots, from 2011"),
    _("Ralph Breaks the Internet, from 2018"),
    _("Ratatouille, from 2007"),
    _("Shrek 2, from 2004"),
    _("Shrek Forever After, from 2010"),
    _("Shrek the Third, from 2007"),
    _("Sing, from 2016"),
    _("Tangled, from 2010"),
    _("The Boss Baby, from 2017"),
    _("The Croods, from 2013"),
    _("The Incredibles, from 2004"),
    _("The Lion King , from 1994"),
    _("The Lion King , from 2019"),
    _("The Secret Life of Pets, from 2016"),
    _("The Simpsons Movie, from 2007"),
    _("Toy Story 3, from 2010"),
    _("Toy Story 4, from 2019"),
    _("Up, from 2009"),
    _("WALL-E, from 2008"),
    _("Zootopia, from 2016"),
]
MOVIES_CHRISTMAS = [
    _("A Bad Moms Christmas, from 2017"),
    _("A Christmas Carol, from 2009"),
    _("A Madea Christmas, from 2015"),
    _("Almost Christmas, from 2016"),
    _("Arthur Christmas, from 2011"),
    _("Bad Santa, from 2003"),
    _("Christmas with the Kranks, from 2004"),
    _("Daddy's Home 2, from 2017"),
    _("Deck the Halls, from 2006"),
    _("Dr. Seuss' How the Grinch Stole Christmas!, from 2000"),
    _("Elf, from 2003"),
    _("Four Christmases, from 2008"),
    _("Fred Claus, from 2007"),
    _("Home Alone, from 1990"),
    _("Home Alone 2: Lost in New York, from 1992"),
    _("Jingle All the Way, from 1996"),
    _("Krampus, from 2015"),
    _("Last Christmas, from 2019"),
    _("Love Actually, from 2003"),
    _("Love the Coopers, from 2016"),
    _("Miracle on 34th Street, from 1994"),
    _("National Lampoon's Christmas Vacation, from 1989"),
    _("Office Christmas Party, from 2016"),
    _("Scrooged, from 1988"),
    _("The Best Man Holiday, from 2013"),
    _("The Grinch, from 2018"),
    _("The Holiday, from 2006"),
    _("The Nightmare Before Christmas, from 1993"),
    _("The Nutcracker and the Four Realms, from 2018"),
    _("The Polar Express, from 2004"),
    _("The Santa Clause, from 1994"),
    _("The Santa Clause 2, from 2002"),
    _("The Santa Clause 3: The Escape Clause, from 2006"),
    _("The Star, from 2017"),
    _("This Christmas, from 2007"),
]
MOVIES_COMEDY = [
    _("Bruce Almighty, from 2003"),
    _("Cars, from 2006"),
    _("Cars 2, from 2011"),
    _("Deadpool, from 2016"),
    _("Deadpool 2, from 2018"),
    _("Despicable Me, from 2010"),
    _("Despicable Me 2, from 2013"),
    _("Despicable Me 3, from 2017"),
    _("Detective Chinatown 2, from 2018"),
    _("Detective Chinatown 3, from 2021"),
    _("Hi, Mom, from 2021"),
    _("Home Alone, from 1990"),
    _("Hotel Transylvania 2, from 2015"),
    _("Hotel Transylvania 3: Summer Vacation, from 2018"),
    _("Incredibles 2, from 2018"),
    _("Inside Out, from 2015"),
    _("Madagascar, from 2005"),
    _("Madagascar 3: Europe's Most Wanted, from 2012"),
    _("Madagascar: Escape 2 Africa, from 2008"),
    _("Meet the Fockers, from 2004"),
    _("Men in Black, from 1997"),
    _("Men in Black 3, from 2012"),
    _("Men in Black II, from 2002"),
    _("Minions, from 2015"),
    _("Monsters University, from 2013"),
    _("Monsters, Inc., from 2001"),
    _("Mrs. Doubtfire, from 1993"),
    _("Puss in Boots, from 2011"),
    _("Ralph Breaks the Internet, from 2018"),
    _("Ratatouille, from 2007"),
    _("Sex and the City, from 2008"),
    _("Shrek, from 2001"),
    _("Shrek 2, from 2004"),
    _("Shrek Forever After, from 2010"),
    _("Shrek the Third, from 2007"),
    _("Tangled, from 2010"),
    _("Ted, from 2012"),
    _("The Hangover, from 2009"),
    _("The Hangover Part II, from 2011"),
    _("The Incredibles, from 2004"),
    _("The Intouchables, from 2011"),
    _("The Lego Movie, from 2014"),
    _("The Mermaid, from 2016"),
    _("The Secret Life of Pets, from 2016"),
    _("The Secret Life of Pets 2, from 2019"),
    _("The Simpsons Movie, from 2007"),
    _("Toy Story 2, from 1999"),
    _("Toy Story 3, from 2010"),
    _("Toy Story 4, from 2019"),
    _("Wreck-It Ralph, from 2012"),
]
MOVIES_FANTASY = [
    _("Aladdin, from 2019"),
    _("Aladdin, from 1992"),
    _("Alice in Wonderland, from 2010"),
    _("Beauty and the Beast, from 2017"),
    _("Cinderella, from 2015"),
    _("Clash of the Titans, from 2010"),
    _("Coco, from 2017"),
    _("Demon Slayer: Kimetsu no Yaiba the Movie: Mugen Train, from 2020"),
    _("Fantastic Beasts and Where to Find Them, from 2016"),
    _("Fantastic Beasts: The Crimes of Grindelwald, from 2018"),
    _("Frozen, from 2013"),
    _("Frozen II, from 2019"),
    _("Harry Potter and the Chamber of Secrets, from 2002"),
    _("Harry Potter and the Deathly Hallows – Part 1, from 2010"),
    _("Harry Potter and the Deathly Hallows – Part 2, from 2011"),
    _("Harry Potter and the Goblet of Fire, from 2005"),
    _("Harry Potter and the Half-Blood Prince, from 2009"),
    _("Harry Potter and the Order of the Phoenix, from 2007"),
    _("Harry Potter and the Philosopher's Stone, from 2001"),
    _("Harry Potter and the Prisoner of Azkaban, from 2004"),
    _("How to Train Your Dragon, from 2010"),
    _("How to Train Your Dragon 2, from 2014"),
    _("Indiana Jones and the Last Crusade, from 1989"),
    _("Jumanji: The Next Level, from 2019"),
    _("Jumanji: Welcome to the Jungle, from 2017"),
    _("Maleficent, from 2014"),
    _("Maleficent: Mistress of Evil, from 2019"),
    _("Night at the Museum, from 2006"),
    _("Oz the Great and Powerful, from 2013"),
    _("Pirates of the Caribbean: At World's End, from 2007"),
    _("Pirates of the Caribbean: Dead Man's Chest, from 2006"),
    _("Pirates of the Caribbean: Dead Men Tell No Tales, from 2017"),
    _("Pirates of the Caribbean: On Stranger Tides, from 2011"),
    _("Pirates of the Caribbean: The Curse of the Black Pearl, from 2003"),
    _("Shrek 2, from 2004"),
    _("Shrek Forever After, from 2010"),
    _("Shrek the Third, from 2007"),
    _("The Chronicles of Narnia: The Lion, the Witch and the Wardrobe, from 2006"),
    _("The Hobbit: An Unexpected Journey, from 2012"),
    _("The Hobbit: The Battle of the Five Armies, from 2014"),
    _("The Hobbit: The Desolation of Smaug, from 2013"),
    _("The Jungle Book, from 2016"),
    _("The Lord of the Rings: The Fellowship of the Ring, from 2001"),
    _("The Lord of the Rings: The Return of the King, from 2003"),
    _("The Lord of the Rings: The Two Towers, from 2002"),
    _("The Twilight Saga: Breaking Dawn – Part 1, from 2011"),
    _("The Twilight Saga: Breaking Dawn – Part 2, from 2012"),
    _("The Twilight Saga: Eclipse, from 2010"),
    _("The Twilight Saga: New Moon, from 2009"),
    _("Up, from 2009"),
]
# There may be some issues with this list, it was taken from wikipedia's top grossing horror films list. 'scary movie' for instance is a teen comedy, and 'the mummy' is an action adventure
MOVIES_HORROR = [
    _("A Quiet Place, from 2018"),
    _("A Quiet Place Part II, from 2021"),
    _("Alien: Covenant, from 2017"),
    _("Annabelle, from 2014"),
    _("Annabelle Comes Home, from 2019"),
    _("Annabelle: Creation, from 2017"),
    _("Bram Stoker's Dracula, from 1992"),
    _("Constantine, from 2005"),
    _("Dark Shadows, from 2012"),
    _("Get Out, from 2017"),
    _("Glass, from 2019"),
    _("Halloween, from 2018"),
    _("Hannibal, from 2001"),
    _("I Am Legend, from 2007"),
    _("Interview with the Vampire, from 1994"),
    _("It, from 2017"),
    _("It Chapter Two, from 2019"),
    _("Jaws, from 1975"),
    _("Jaws 2, from 1978"),
    _("Paranormal Activity 3, from 2011"),
    _("Prometheus, from 2012"),
    _("Resident Evil: Afterlife, from 2010"),
    _("Resident Evil: Retribution, from 2012"),
    _("Resident Evil: The Final Chapter, from 2017"),
    _("Scary Movie, from 2000"),
    _("Shutter Island, from 2010"),
    _("Signs, from 2002"),
    _("Sleepy Hollow, from 1999"),
    _("Split, from 2017"),
    _("The Blair Witch Project, from 1999"),
    _("The Conjuring, from 2013"),
    _("The Conjuring 2, from 2016"),
    _("The Conjuring: The Devil Made Me Do It, from 2021"),
    _("The Exorcist, from 1973"),
    _("The Meg, from 2018"),
    _("The Mummy, from 1999"),
    _("The Mummy, from 2017"),
    _("The Mummy Returns, from 2001"),
    _("The Mummy: Tomb of the Dragon Emperor, from 2008"),
    _("The Nun, from 2018"),
    _("The Others, from 2001"),
    _("The Ring, from 2002"),
    _("The Silence of the Lambs, from 1991"),
    _("The Sixth Sense, from 1999"),
    _("The Village, from 2004"),
    _("Unbreakable, from 2000"),
    _("Us, from 2019"),
    _("Van Helsing, from 2004"),
    _("War of the Worlds, from 2005"),
    _("World War Z, from 2013"),
]
MOVIES_MUSICAL = [
    _("A Star Is Born, from 2018"),
    _("Aladdin, from 2019"),
    _("Aladdin, from 1992"),
    _("Alvin and the Chipmunks, from 2007"),
    _("Alvin and the Chipmunks: Chipwrecked, from 2011"),
    _("Alvin and the Chipmunks: The Squeakquel, from 2009"),
    _("Baahubali 2: The Conclusion, from 2017"),
    _("Beauty and the Beast, from 2017"),
    _("Beauty and the Beast, from 1991"),
    _("Bohemian Rhapsody, from 2018"),
    _("Charlie and the Chocolate Factory, from 2005"),
    _("Chicago, from 2002"),
    _("Cinderella, from 1950"),
    _("Encanto, from 2021"),
    _("Enchanted, from 2007"),
    _("Frozen II, from 2019"),
    _("Frozen, from 2013"),
    _("Grease, from 1978"),
    _("Happy Feet, from 2006"),
    _("Hercules, from 1997"),
    _("High School Musical 3: Senior Year, from 2008"),
    _("Home, from 2015"),
    _("La La Land, from 2016"),
    _("Les Misérables, from 2012"),
    _("Mamma Mia: Here We Go Again!, from 2018"),
    _("Mamma Mia!, from 2008"),
    _("Mary Poppins Returns, from 2018"),
    _("Moana, from 2016"),
    _("Mulan, from 1998"),
    _("Pitch Perfect 2, from 2015"),
    _("Pocahontas, from 1995"),
    _("Rio, from 2011"),
    _("Rio 2, from 2014"),
    _("Saturday Night Fever, from 1977"),
    _("Sing, from 2016"),
    _("Sing 2, from 2021"),
    _("Snow White and the Seven Dwarfs, from 1937"),
    _("Tangled, from 2010"),
    _("Tarzan, from 1999"),
    _("The Greatest Showman, from 2017"),
    _("The Hunchback of Notre Dame, from 1996"),
    _("The Jungle Book, from 2016"),
    _("The Jungle Book, from 1967"),
    _("The Lion King, from 2019"),
    _("The Lion King, from 1994"),
    _("The Lorax, from 2012"),
    _("The Polar Express, from 2004"),
    _("The Princess and the Frog, from 2009"),
    _("The Sound of Music, from 1965"),
    _("Trolls, from 2016"),
]
MOVIES_ADULT = [
    _("9 Lives of a Wet Pussy, from 1976. It starred Pauline LaMonde and was about the erotic escapades of a young New York heiress"),
    _("A Dirty Western, from 1975"),
    _("A Perfect Ending, from 2012"),
    _("A Taste of Joy, from 2012"),
    _("Alice in Wonderland: An X-Rated Musical Comedy, from 1976"),
    _("Animal Instincts, from 1992"),
    _("Aphrodesia's Diary, from 1983"),
    _("Babylon Pink, from 1979. It starred several leads and was about the sexual fantasies of several women; a bored housewife, a business woman, an older woman, and a sexually curious teenager"),
    _("Barbara Broadcast, from 1977"),
    _("Behind the Green Door, from 1972"),
    _("Bend Over Boyfriend, from 1998"),
    _("Bijou, from 1972. It starred Bill Harrison and was a gay film about a construction worker discovering an invitation to a sex club"),
    _("Black Emmanuelle, from 1975"),
    _("Blue Movie, from 1969. It was directed by Andy Warhol and starred Viva, and Louis Waldon"),
    _("Bound, from 2015"),
    _("Cabaret Desire, from 2011"),
    _("Chemistry, from 2006"),
    _("Dangerous Liaisons, from 2005"),
    _("Debbie Does Dallas, from 1978"),
    _("Deep Throat, from 1972"),
    _("El Paso Wrecking Corp., from 1978"),
    _("Emmanuelle, from 1974"),
    _("Flashpoint, from 1998"),
    _("Flesh Gordon, from 1974"),
    _("Harlot, from 1971"),
    _("High Test Girls, from 1980"),
    _("Hotel Erotica, from 2002"),
    _("Insatiable, from 1980"),
    _("I am Curious (Blue), from 1968"),
    _("I am Curious (Yellow), from 1967"),
    _("Infidelity: Sex Stories 2, from 2011"),
    _("Last Tango, from 2011"),
    _("Love Toy, from 1968"),
    _("Maraschino Cherry, from 1978"),
    _("Missing: A Lesbian Crime Story, from 2016"),
    _("Mona the Virgin Nymph, from 1970"),
    _("Nothing Personal, from 1990. It starred Moana Pozzi and was about a personal quest to improve her sex life"),
    _("Once Upon a Girl, from 1976"),
    _("Perspective, from 2019"),
    _("Pink Prison, from 1999"),
    _("Pink Velvet 3: A Lesbian Odyssey, from 2005"),
    _("Pirates, from 2005"),
    _("Pirates II: Stagnetti’s Revenge, from 2008"),
    _("Red Shoe Diaries, from 1992"),
    _("Reel People, from 1984. It starred Juliet Anderson and was about real people performing their sexual desires on film for the first time"),
    _("Rendez-vous, from 2015"),
    _("School Girl, from 1971"),
    _("Score, from 1974"),
    _("Sensational Janine, from 1976"),
    _("Sex Pursuits, from 1971. It starred Rene Bond"),
    _("Sex Stories, from 2009. It starred multiple leads and was about two dinner parties simultaneously unfolding. Each sharing stories of their recent escapades"),
    _("Sexual Chronicles of a French Family, from 2012"),
    _("Snapshot, from 2016"),
    _("Taboo, from 1980"),
    _("Taboo II, from 1982"),
    _("The Bare Wench Project, from 2000"),
    _("The Bi Apple, from 2007"),
    _("The Bite, from 1977"),
    _("The Cheerleaders, from 1973"),
    _("The Devil in Miss Jones, from 1973. It starred Georgina Spelvin and was about a woman who commits suicide. Where, instead of going to Heaven, she returns to life to embody lust"),
    _("The Dreamers, from 2003"),
    _("The Fashionistas, from 2002"),
    _("The Friend Zone, from 2012. It starred Riley Reid"),
    _("The Good Girl, from 2004"),
    _("The Grafenberg Spot, from 1985"),
    _("The Jade Pussycat, from 1977"),
    _("The Obsession, from 2017. It starred Abella Danger"),
    _("The Opening of Misty Beethoven, from 1976"),
    _("The Submission of Emma Marx, from 2013"),
    _("The Ultimate Pleasure, from 1977. It starred Kristine Heller and was about a cab driver who finds a suitcase full of money and realises he now has the means to fulfil all of his wife’s sexual fantasies"),
    _("The Walking Dead: A Hardcore Parody, from 2013"),
    _("The Xterminator, from 1986"),
    _("Through the Looking Glass, from 1976"),
    _("Tonight for Sure, from 1962"),
    _("Xana and Dax: When Opposites Attract, from 2005"),
    _("XConfessions Vol. 3, from 2014. It starred Maria Agrado, Samantha Bentley and Samia Duarte, and was a compilation of 10 erotic stories"),
]
MOVIES_SCI_FI = [
    _("Armageddon, from 1998"),
    _("Avatar, from 2009"),
    _("Bumblebee, from 2018"),
    _("Dawn of the Planet of the Apes, from 2014"),
    _("E.T. the Extra-Terrestrial , from 1982"),
    _("Godzilla, from 2014"),
    _("Gravity, from 2013"),
    _("I Am Legend, from 2007"),
    _("Inception, from 2010"),
    _("Independence Day, from 1996"),
    _("Interstellar, from 2014"),
    _("Jurassic Park, from 1993"),
    _("Jurassic World, from 2015"),
    _("Jurassic World Dominion , from 2022"),
    _("Jurassic World: Fallen Kingdom, from 2018"),
    _("Men in Black, from 1997"),
    _("Men in Black 3, from 2012"),
    _("Ready Player One, from 2018"),
    _("Rise of the Planet of the Apes, from 2011"),
    _("Rogue One: A Star Wars Story, from 2016"),
    _("Star Trek Into Darkness, from 2013"),
    _("Star Wars, from 1977"),
    _("Star Wars: Episode I – The Phantom Menace, from 1999"),
    _("Star Wars: Episode II – Attack of the Clones, from 2002"),
    _("Star Wars: Episode III – Revenge of the Sith, from 2005"),
    _("Star Wars: Episode V – The Empire Strikes Back, from 1980"),
    _("Star Wars: Episode VI – Return of the Jedi, from 1983"),
    _("Star Wars: The Force Awakens, from 2015"),
    _("Star Wars: The Last Jedi, from 2017"),
    _("Star Wars: The Rise of Skywalker, from 2019"),
    _("Terminator 2: Judgment Day, from 1991"),
    _("The Day After Tomorrow, from 2004"),
    _("The Hunger Games, from 2012"),
    _("The Hunger Games: Catching Fire, from 2013"),
    _("The Hunger Games: Mockingjay – Part 1, from 2014"),
    _("The Hunger Games: Mockingjay – Part 2, from 2015"),
    _("The Lost World: Jurassic Park, from 1997"),
    _("The Martian, from 2015"),
    _("The Matrix, from 1999"),
    _("The Matrix Reloaded, from 2003"),
    _("The Wandering Earth, from 2019"),
    _("Transformers, from 2007"),
    _("Transformers: Age of Extinction, from 2014"),
    _("Transformers: Dark of the Moon, from 2011"),
    _("Transformers: Revenge of the Fallen, from 2009"),
    _("Transformers: The Last Knight, from 2017"),
    _("WALL-E, from 2008"),
    _("War for the Planet of the Apes, from 2017"),
    _("War of the Worlds, from 2005"),
]



#------------------------------------------------------------------
# Conversations section:
# This section is broken into basic conversation depths. It may be useful in future to e.g. not have a heart-to-heart with your {enemy}, {boss}, {whoever}.
# It might also be useful for age / job dependent topics, or to facilitate 'you spoke to your {relation} about which is better {movie} or {movie}' / 'you spoke with your {relation} about {sport} and how {team} will beat {team} this year'

# Casual chats, small-talk, etc. (can take words like 'chatted with your {relation} about' or 'talked about' prior to calling)
CHATS = [
    _("the hierarchy of licorice"),
    _("which is better, Star Wars or Star Trek"),
    _("which is better, Coke or Pepsi"),
    _("which is better, Lord of the Rings or Harry Potter"),
    _("who is better, the Red Sox or Yankees"),
    _("who will win the Monaco Grand Prix"),
    _("how it's illegal to masturbate in Indonesia"),
    _("whether you would rather live without music or television"),
    _("why mannequins have erect nipples"),
    _("Angleina Jolie's lips"),
]
CHATS_INFANT = [
	_("choo-choo trains, and then both made baby noises at each other"),
	_("why 'A' is for 'Apple'"),
	_("the fluffy pussy cat"),
	_("Thomas the Tank Engine"),
	_("Dinosaur Train"),
	_("Alphablocks"),
	_("Sesame street"),
	_("Mickey Mouse"),
	_("'O' is for 'Owl'"),
	_("'O' is for 'Octopus'"),
	_("'O' is for 'Orange'"),
    _("three blind mice"),
]
CHATS_CHILD = [
    _("how much you hate vegetables"),
    _("how scary the toilet is when it gets flushed"),
    _("the meaning of life"),
    _("which super power you would most like to have"),
    _("which super power they would most like to have"),
    _("what they want to be when they grow up"),
    _("where water goes when the toilet gets flushed"),
    _("why the sky is blue"),
    _("your favourite movie character"),
    _("your least favourite chore"),
]
CHATS_TEEN = [
    _(""),
]
CHATS_ADULT = [
    _(""),
]
CHATS_CLASSMATES_PRIMARY = [
    _(""),
]
CHATS_CLASSMATES_SECONDARY = [
    _(""),
]
CHATS_CLASSMATES_TERTIARY = [
    _(""),
]
CHATS_CO_WORKERS = [
    _(""),
]


# Academic / debatable topics, topics that are contentious etc. (can take words like 'discussed' prior to calling)
DISCUSSIONS = [
    _("why cats are better than dogs"),
    _("why dogs are better than cats"),
    _("the Russia-Ukraine War"),
    _("High Fuel Prices"),
    _("the Metaverse"),
    _("the Economic crisis of Sri Lanka"),
    _("Moonlighting"),
    _("the Pros and Cons of working from home"),
    _("whether people should invest in cryptocurrency"),
    _("the Biomedical waste crisis"),
    _("the impact of 5G on the global economy"),
    _("how to prevent the next pandemic"),
    _("the impact of COVID-19 on the global economy"),
    _("the pros and cons of block chain technology"),
    _("the role of social media in international politics"),
    _("how to end the threat of nuclear war"),
    _("the impact of COVID-19 on the education sector"),
    _("Taliban rule in Afghanistan"),
    _("the rise of the gig economy"),
    _("the harms of passive smoking"),
    _("the advantages and disadvantages of having a credit card"),
    _("whether software should be free for everyone"),
    _("whether gambling should be allowed from the age of 16"),
    _("problems caused by the economic boycott in Cuba"),
    _("how international trade barriers work"),
    _("how the United Nations is based on diplomacy and strengthening relationships"),
    _("whether or not public schools are safe enough"),
    _("whether it is necessary to hold value in what you argue"),
    _("why drink driving is dangerous"),
    _("how India became such a large milk producer"),
    _("how to make money with recycling"),
    _("the decreasing productivity of the Japanese workforce"),
    _("a business model to help health-conscious customers"),
    _("what the best technologies are to safeguard the right of free speech on the internet"),
    _("what the best technologies are to safeguard the right of privacy on the internet"),
    _("how to check for the signs of burnout"),
    _("how to overcome the coal crisis in India"),
    _("the causes of bullying in schools"),
    _("why we should have a minimum wage"),
    _("whether universal basic income is a good idea"),
    _("the leadership changes needed in our country"),
    _("whether empowering women is the solution to violence against women"),
    _("the effects of communalism on social cohesion"),
    _("whether we're becoming too sensitive in society"),
    _("lessons for the world from the COVID-19 pandemic"),
    _("whether crime rates increase because of unemployment"),
    _("causes of poverty around the world"),
    _("the effects of the Internet of Things on our lives"),
    _("whether drug abuse is rampant among teenagers"),
    _("whether anemia effects urban society"),
    _("gender equality in the workplace"),
    _("whether the wealthy should be taxed more"),
    _("whether the poor should be given more assistance"),
    _("whether it is possible to maintain a work-life balance"),
    _("whether saying 'women make good managers' is sexist like saying 'asians are good at maths' is racist"),
    _("whether job creators are needed more than job seekers"),
    _("whether a borderless world is a myth or a reality"),
    _("what would happen if Bitcoin crashed to zero and whether it is possible"),
    _("business ethics in today's market compared with the past and the potential future"),
    _("whether patience is important in business and management"),
    _("whether the family-run business is relevant in today's market"),
    _("whether E-commerce discounts are harmful in the long run and is it the business or customer being harmed"),
    _("whether globalisation is an opportunity or a threat"),
    _("how markets are found and not created"),
    _("whether the world is ready for a cashless society"),
    _("whether physical infrastructure is the answer to social equality"),
    _("whether the public sector being a guarantor of job security is a myth"),
    _("whether a circular economy is key to sustainable development"),
    _("the contribution of the Indian IT industry to the US and global economy"),
    _("whether democracy is a hindrance to economic reforms in India"),
    _("the technology behind Zero Budget Natural Farming"),
    _("the effects of technological change on jobs"),
    _("whether pervasive technology is creating a generation of cyber zombies"),
    _("whether the IT industry will create more or less jobs in the future"),
    _("whether artificial intelligence can replace human intelligence"),
    _("the effects of big data on information privacy"),
    _("whether automation will create more or less jobs"),
    _("the benefits and challenges of data localisation"),
    _("whether artifical intelligence will change the future"),
    _("how technology can be used to tackle financial crimes"),
    _("whether polythene bags should be completely banned"),
    _("how to control air pollution levels"),
    _("whether green jobs are essential for sustainable development"),
    _("how to manage natural disasters"),
    _("how to manage financial disasters"),
    _("methods of disaster recovery"),
    _("the effects of Coronaviruses on the environment"),
    _("whether smart farming is the future of agriculture"),
    _("whether genetic engineering in agriculture is good or bad"),
    _("the effects of climate on the farming system and food supply"),
    _("whether automation in farming is good"),
    _("whether collective farming is a boon or a bane"),
    _("our views on natural versus factory farming"),
    _("our views on conventional farming and organic farming"),
    _("the role of women in agriculture"),
    _("whether agroforestry destroys the environment"),
    _("gay marriage and your views on it"),
    _("whether war is the best option to solve international disputes"),
    _("whether primary school children should be allowed to own mobile phones"),
    _("whether using animals for medical research should be allowed"),
    _("whether men and women will ever be equal, if they already are, and whether equality will last"),
    _("whether you can have a happy family life and a successful career at the same time"),
    _("whether marriage is an outdated institution"),
    _("whether citizens should be allowed to carry guns and other weapons"),
    _("whether the death penalty is acceptable for any reasons"),
    _("whether non-citizens and tourists should be allowed to vote in their country of residence"),
    _("whether sex education should be taught to children under 12"),
    _("whether or not women are paid the same as men"),
    _("whether bribery and corruption is acceptable in government"),
    _("whether bribery and corruption is acceptable in private business"),
    _("whether music that glorifies violence should be banned"),
    _("whether condoms should be distributed for free in primary schools"),
    _("whether nuclear weapons are necessary weapons"),
    _("whether teachers should be allowed to carry guns"),
    _("whether professional sports people earn too much money"),
    _("our views on whether or not beauty contests should be banned"),
    _("our views on whether or not cosmetic surgery should be outlawed"),
    _("our views on whether or not abortions are okay"),
    _("our views on whether or not social deprivation causes crime"),
    _("our views on whether or not military service should be compulsory"),
    _("our views on whether or not war is ever an option for solving international disputes"),
    _("our views on whether or not torture can be acceptable in some cases"),
    _("our views on whether or not curfews keep teens out of trouble"),
    _("our views on whether or not we're becoming too dependent on computers"),
    _("our views on whether or not smoking should be banned worldwide"),
    _("our views on whether or not it should be illegal to ride a bicycle without a helmet"),
    _("our views on whether or not single sex schools are bad for childhood development and lead to unhealthy views of the opposite sex"),
    _("our views on whether or not homework is harmful"),
    _("our views on whether or not the United Nations is a failed organisation"),
    _("our views on whether or not intelligence tests should be given before couples can have children"),
    _("our views on whether or not a woman's place is in the home"),
    _("our views on whether or not it's a man's world"),
    _("our views on whether or not money makes you happy"),
    _("our views on whether or not money can buy you happiness"),
    _("our views on whether or not the internet must be censored to protect society"),
    _("our views on whether or not genetically modified foods have no ill health effects"),
    _("our views on whether a man should have a wife for the family and a paramour for pleasure"),
    _("our views on whether a woman should have a husband for the family and a paramour for pleasure"),
    _("our views on whether soft drugs should be legalised"),
    _("our views on whether or not electric cars help the environment"),
    _("our views on whether or not staying unmarried leads to a happier life"),
    _("our views on whether or not software piracy is a real crime"),
    _("our views on whether or not religion is needed"),
    _("our views on whether veganism is the key to solving climate change"),
    _("our views on whether the police force is institutionally racist"),
    _("our views on whether democracy must be imposed on nations"),
    _("our views on whether the war in Iraq was justified"),
    _("our views on whether your race affects your intelligence"),
    _("our views on whether your race affects your sporting ability"),
    _("our views on whether the world is over populated and steps must be taken to reduce births"),
    _("whether or not euthanasia should be illegal"),
    _("whether or not cloning is a valuable scientific pursuit"),
    _("whether obesity is a disease and not a lifestyle choice"),
    _("whether or not video games contribute to youth violence"),
    _("whether the drinking age should be lowered"),
    _("whether the drinking age should be raised"),
    _("whether the smoking age should be lowered"),
    _("whether the smoking age should be raised"),
    _("whether the age of consent should be lowered"),
    _("whether the age of consent should be raised"),
    _("whether the voting age should be lowered"),
    _("whether the voting age should be raised"),
    _("whether the driving age should be lowered"),
    _("whether the driving age should be raised"),
    _("whether the gambling age should be lowered"),
    _("whether the gambling age should be raised"),
    _("whether the military service age should be lowered"),
    _("whether the military service age should be raised"),
    _("whether drugs should be accepted in sports"),
    _("whether self driving cars are going to make our lives easier"),
    _("whether climate change exists"),
    _("whether carbohydrates are more damaging than fats"),
    _("whether terrorism can be justifed"),
    _("whether or not street prostitution should be illegal"),
    _("whether or not prostitution in a brothel should be illegal"),
    _("whether or not prostituting yourself in your own home should be illegal"),
    _("whether prisoners should be allowed to vote"),
    _("whether prenuptual agreements make families stronger"),
    _("whether corporal punishment should be allowed in schools"),
]
DISCUSSIONS_INFANT = [
    _(""),
]
DISCUSSIONS_CHILD = [
    _("if it is better to scrunch or fold"),
    _("if it is better to squat or sit"),
    _("if it is better to shower or bath"),
    _("if it is better to wipe from the front or back"),
    _("if it is better to "),
    _("your favourite movie character"),
    _("your imaginary friend"),
    _("your most prized posession"),
]
DISCUSSIONS_TEEN = [
    _(""),
]
# Important 'life' talks
TALKS = [
    _("not spending enough time with your family"),
]
TALKS_INFANT = [
    _("the importance of not sucking your thumb"),
]
TALKS_CHILD = [
    _("not drawing on the kitchen table"),
]
TALKS_TEEN = [
    _("the importance of cleaning up after yourself"),
]
TALKS_ADULT = [_("the importance of saving for retirement")]

# Emotionally sincere, serious, or personal conversations
HEART_TO_HEARTS = [
    _("the best gift you ever received"),
    _("your most bizarre pet peeves"),
    _("why you love your closest friends"),
    _("your favourite books to read at the beach"),
    _("your favourite foods to eat on a cold night"),
    _("your biggest turn offs in other people"),
    _("remembering the times when you've felt closest together"),
    _("what you would do if you knew you couldn't fail"),
    _("your favourite summertime memory"),
    _("something you've always wanted to try"),
    _("things you've always wanted to try"),
    _("a moment in history you would have liked to have been a part of"),
    _("how to manage money better"),
    _("where you would go if you could time travel"),
    _("what superpower you would have if you could have one"),
    _("what you're feeling thankful for today"),
    _("how much they mean to you"),
    _("something that you know you don't need but you're really grateful you have"),
    _("your fears of not accomplishing your New Year resolutions"),
    _("how silly New Year's resolutions are"),
    _("the best part of your day"),
]
HEART_TO_HEARTS_TEEN = [
    _("what happens when we die"),
]

#------------------------------------------------------------------
# Spending time together section:

SPEND_TIME = [
    _(""),
]
# For use in situations like 'Your {relation} took you {to build a sandcastle in a sandbox at the park} 
# If you are the parent/older sibling then 'You took your {relation} {spend_time_child}
SPEND_TIME_CHILD = [
    _("birdwatching"),
    _("to a cake baking class"),
    _("to a comic book store"),
    _("to a music festival"),
    _("to a yoga class"),
    _("to attend a juggling class"),
    _("to bring donuts to the police station"),
    _("to build a sandcastle in a sandbox at the park"),
    _("to get cornrow braids"),
    _("to get henna tattoos"),
    _("to listen to a punk band"),
    _("to participate in a neighbourhood cleanup"),
    _("to the park to feed the ducks"),
]
SPEND_TIME_TEEN = [
    _("to practice sumo wrestling"),
    _("to play in the rain"),
    _("to toilet paper the neighbour's house"),
    _("to scare random people by jumping out of the bushes at a local park"),
    _("to make a wish while throwing a coing in a fountain"),
    _("to watch toy unboxing videos"),
    _("to a café to play cards"),
    _("to watch a movie under the stars in the park"),
    _("to perform in a flash mob at the grocery store"),
    _("to fly a kite"),
    _("to a rugby game"),
    _("to the circus"),
    _("longboarding"),
    _("to a Hindu temple"),
    _("to build a sandcastle in a sandbox at the park"),
    _("to an escape room"),
    _("antiquing"),
    _("to write haikus"),
    _("to play in the sprinklers at the local park"),
    _("to play bingo at the community centre"),
    _("to an arcade"),
    _("to throw paper aeroplanes off the bleachers at the local high school"),
    _("to the water park"),
    _("to the aquarium to look at sharks"),
    _("to sing P!nk songs at karaoke night"),
    _("to the movies"),
    _("axe throwing"),
    _("to make home made mini pizzas"),
    _("to a painting class"),
    _("to have a random dance party in a public plaza"),
    _("to plant trees in the forest"),
    _("whale watching"),
    _("to make and pass out balloon animals at the park"),
    _("snowboarding"),
    _("to the park"),
    _("to graffiti train cars"),
    _("to learn origami at the community centre"),
    _("birdwatching"),
    _("to the shooting range"),
    _("to do caricature drawings of random people in a public place"),
    _("yodelling"),
    _("deep sea fishing"),
    _("to a carnival"),
    _("to ding dong ditch the neighbours"),
    _("to parkour hardcore"),
    _("to watch a random trial at the municipal court"),
    _("to a rugby game"),
    _("to make selfies for Instagram"),
    _("to the museum"),
    _("to walk along a scenic vista"),
    _("to watch toy unboxing videos"),
    _("to fly a drone"),
    _("to make a safety evacuation map"),
    _("horseback riding in the countryside"),
    _("to dinner"),
    _("to a puppet-making seminar"),
    _("to the symphony"),
]

# E.g. You {spend_time_pet_x)} {pet_type}, {pet_name} = You listened to music with your cat, Pip.
# All pets
SPEND_TIME_PET_CAT = [
    _("listened to hip-hop music with your"),
    _("listened to classical music with your"),
    _("played with your"),
]
# Pet type specific
SPEND_TIME_PET_CAT = [
    _("curled up and watched a movie with your"),
    _("let a motorised weasel ball loose for your"),
    _("made an obstacle course for your"),
    _("used a cucumber to take prank videos of your"),
    _("used a laser pointer to play with your"),
    _("rolled a ball or yarn across the floor for your"),
]
SPEND_TIME_PET_DOG = [
    _("curled up and watched a movie with your"),
    _("did the 'What The Fluff' challenge with your"),
    _("gave belly rubs, pats and scratches to your"),
    _("jingled some keys loudly, and went out to walk your"),
    _("made a breadcrumb trail of dog biscuits for your"),
    _("made a breadcrumb trail of dog biscuits leading to a bone for your"),
    _("made an obstacle course for your"),
    _("loudly announced walk time, and went walking with your"),
    _("said 'Walkies!', and went walking with your"),
    _("went swimming at the beach with your"),
    _("went to the park and threw a ball for your"),
    _("went to the river and threw sticks in it for your"),
    
]

# Events section:
# Random year events. positive events in _POSITIVE. negative, neutral, and choice based to separate lists 

NEWS_EVENT = [
    _("The Dominican Republic's forces have been withdrawn from Haiti, indicating an end to the war. In total, there were more than 10,000 casualties as a result of the conflict"),
]

# Age 3 to end of primary
CHILD_EVENT_POSITIVE = [
    _("You weren't doing anything fun, but then your friend came over wanting to go out and play. You both had a blast!"),
]
CHILD_EVENT_NEGATIVE = [
    _(""),
]
CHILD_EVENT_NEUTRAL = [
    _(""),
]
# E.g. 'Your {Mother_Father} wants to buy you {and your siblings_if any} a pet {cat} named {names}. (cat age, gender, colour, health, happiness, smarts, looks, craziness): 
# choice = "Yes, I want {him_her}!" > "I don't want {name}" > "Surprise me!"'
# Or, 'While trick-or-treating in your neighbourhood, you come upon a bowl full of candy with an attached sign that reads, "Please help yourself to one piece."
# What will you do? = "Grab a handful" > "Empty the bowl" > "Take one piece and move on" > "Surprise me!"'
CHILD_EVENT_CHOICE = [
    _(""),
]
# E.g. 'While in your teacher, {teacher_name}'s class, your classmate, {classmate_name}, all of a sudden begins ripping pages out of the class textbook one-at-a-time, yelling "Toodle-oo!" with each new page tear.
# What will you do? = "Attack {him_her}" > "Ignore {his_her} antics" > "Laugh at {him_her}" > "Report {him_her} to the principal" > "Surprise me!"
CHILD_EVENT_CHOICE_SCHOOL = [
    _(""),
]

# Pet types:
PET_TYPE = [
    _("cat"),
    _("dog"),
    _("fish"),    
]
# Pet breeds: (for use in the pet shop)
PET_BREEDS_CAT = [
    _("Abyssinian Cat"),
    _("America Shorthair Cat"),
    _("House Cat"),
    _("Tabby Cat"),
]
PET_BREEDS_DOG = [
    _("Cairn Terrier"),
    _("German Shepherd"),
    _("Mutt"),
]
PET_BREEDS_FISH = [
    _("Betta Fish"),
]
#Pet names:
PET_NAMES_CAT_MALE = [
    _("Oliver"),
    _("Leo"),
    _("Milo"),
    _("Charlie"),
    _("Max"),
    _("Simba"),
    _("Jack"),
    _("Loki"),
    _("Ollie"),
    _("Jasper"),
    _("Buddy"),
    _("Smokey"),
    _("Oscar"),
    _("Toby"),
    _("Tiger"),
    _("Finn"),
    _("Simon"),
    _("Binx"),
    _("Louie"),
    _("Henry"),
    _("Oreo"),
    _("Winston"),
    _("Salem"),
    _("Gus"),
    _("Felix"),
    _("Tigger"),
    _("Rocky"),
    _("Kitty"),
    _("Sam"),
    _("Teddy"),
    _("Apollo"),
    _("Blu"),
    _("Gizmo"),
    _("Archie"),
    _("Jax"),
    _("Bear"),
    _("Boots"),
    _("Frankie"),
    _("Chester"),
    _("Bandit"),
    _("Beau"),
    _("Pumpkin"),
    _("Cosmo"),
    _("Lucky"),
    _("Thor"),
    _("Frank"),
    _("Midnight"),
    _("Benny"),
    _("Tom"),
    _("Boo"),
    _("Ash"),
    _("Romeo"),
    _("Goose"),
    _("Joey"),
    _("Mochi"),
    _("Ozzy"),
    _("Merlin"),
    _("Prince"),
    _("Pepper"),
    _("Bruce"),
    _("Otis"),
    _("Harry"),
    _("Percy"),
    _("Peanut"),
    _("Bean"),
    _("Tucker"),
    _("Murphy"),
    _("Moose"),
    _("Mac"),
    _("Kevin"),
    _("Casper"),
    _("Buster"),
    _("Bob"),
    _("Thomas"),
    _("Jackson"),
    _("Sylvester"),
    _("Jake"),
    _("Fred"),
    _("Mango"),
    _("Sunny"),
    _("Hank"),
    _("Bubba"),
    _("Calvin"),
    _("Marley"),
    _("Coco"),
    _("Louis"),
    _("Tony"),
    _("Bagheera"),
    _("Duke"),
    _("Clyde"),
    _("Hunter"),
    _("Mittens"),
    _("Luke"),
    _("Nugget"),
    _("Ace"),
    _("Scout"),
    _("Tito"),
    _("Monty"),
    _("Wally"),
    _("Alex"),
]
PET_NAMES_CAT_FEMALE = [
    _("Luna"),
    _("Bella"),
    _("Lily"),
    _("Lucy"),
    _("Nala"),
    _("Kitty"),
    _("Chloe"),
    _("Stella"),
    _("Zoe"),
    _("Lola"),
    _("Cleo"),
    _("Daisy"),
    _("Sophie"),
    _("Willow"),
    _("Olive"),
    _("Penny"),
    _("Pepper"),
    _("Rosie"),
    _("Molly"),
    _("Kiki"),
    _("Ellie"),
    _("Phoebe"),
    _("Coco"),
    _("Lulu"),
    _("Princess"),
    _("Maggie"),
    _("Piper"),
    _("Millie"),
    _("Ginger"),
    _("Nova"),
    _("Hazel"),
    _("Pumpkin"),
    _("Ruby"),
    _("Penelope"),
    _("Fiona"),
    _("Oreo"),
    _("Baby"),
    _("Charlie"),
    _("Winnie"),
    _("Minnie"),
    _("Abby"),
    _("Mittens"),
    _("Poppy"),
    _("Cookie"),
    _("Ivy"),
    _("Boo"),
    _("Roxy"),
    _("Belle"),
    _("Ella"),
    _("Zelda"),
    _("Mochi"),
    _("Alice"),
    _("Angel"),
    _("Emma"),
    _("Salem"),
    _("Bean"),
    _("Freya"),
    _("Bailey"),
    _("Midnight"),
    _("Peanut"),
    _("Leia"),
    _("Peaches"),
    _("Gigi"),
    _("Frankie"),
    _("Honey"),
    _("Violet"),
    _("Charlotte"),
    _("Olivia"),
    _("Sage"),
    _("Stormy"),
    _("Kiwi"),
    _("Bonnie"),
    _("Smokey"),
    _("Scout"),
    _("Arya"),
    _("Sushi"),
    _("Sugar"),
    _("Blu"),
    _("Josie"),
    _("Gypsy"),
    _("Mocha"),
    _("Binx"),
    _("Trixie"),
    _("Snickers"),
    _("Boots"),
    _("Iris"),
    _("Lucky"),
    _("Lady"),
    _("Elsa"),
    _("Pixie"),
    _("Tiger"),
    _("Ava"),
    _("Holly"),
    _("Tilly"),
    _("Grace"),
    _("Opal"),
    _("Peach"),
    _("Muffin"),
    _("Maple"),
    _("Sally"),
]
PET_NAMES_DOG_MALE = [
   _("Max"),
   _("Charlie"),
   _("Milo"),
   _("Buddy"),
   _("Rocky"),
   _("Bear"),
   _("Leo"),
   _("Duke"),
   _("Teddy"),
   _("Tucker"),
   _("Beau"),
   _("Oliver"),
   _("Jack"),
   _("Winston"),
   _("Ollie"),
   _("Toby"),
   _("Jax"),
   _("Blue"),
   _("Finn"),
   _("Louie"),
   _("Murphy"),
   _("Loki"),
   _("Moose"),
   _("Gus"),
   _("Bruno"),
   _("Ace"),
   _("Apollo"),
   _("Hank"),
   _("Archie"),
   _("Kobe"),
   _("Henry"),
   _("Thor"),
   _("Simba"),
   _("Bailey"),
   _("Scout"),
   _("Diesel"),
   _("Jake"),
   _("Lucky"),
   _("Buster"),
   _("Otis"),
   _("Jackson"),
   _("Benny"),
   _("Chewy"),
   _("Jasper"),
   _("Oscar"),
   _("Bandit"),
   _("Rex"),
   _("Oreo"),
   _("Riley"),
   _("Baxter"),
   _("Cody"),
   _("Coco"),
   _("Rocco"),
   _("Tank"),
   _("Prince"),
   _("Ranger"),
   _("King"),
   _("Marley"),
   _("Roscoe"),
   _("Sam"),
   _("Oakley"),
   _("Copper"),
   _("Gizmo"),
   _("Chase"),
   _("Luke"),
   _("Boomer"),
   _("Bruce"),
   _("Frankie"),
   _("Chance"),
   _("Rusty"),
   _("Hunter"),
   _("Ozzy"),
   _("Tyson"),
   _("Romeo"),
   _("Rudy"),
   _("Mac"),
   _("Bubba"),
   _("Peanut"),
   _("Kai"),
   _("Chico"),
   _("Joey"),
   _("Atlas"),
   _("Goose"),
   _("Samson"),
   _("Chief"),
   _("Levi"),
   _("Titan"),
   _("Frank"),
   _("Axel"),
   _("Brutus"),
   _("Ghost"),
   _("Brady"),
   _("Cosmo"),
   _("Scooby"),
   _("Chip"),
   _("Chester"),
   _("Wally"),
   _("Rufus"),
   _("Dash"),
   _("Louis"),
]
PET_NAMES_DOG_FEMALE = [
   _("Bella"),
   _("Luna"),
   _("Lucy"),
   _("Daisy"),
   _("Lola"),
   _("Sadie"),
   _("Molly"),
   _("Bailey"),
   _("Stella"),
   _("Maggie"),
   _("Chloe"),
   _("Penny"),
   _("Nala"),
   _("Zoey"),
   _("Lily"),
   _("Coco"),
   _("Sophie"),
   _("Rosie"),
   _("Ellie"),
   _("Ruby"),
   _("Piper"),
   _("Mia"),
   _("Roxy"),
   _("Gracie"),
   _("Millie"),
   _("Willow"),
   _("Lulu"),
   _("Pepper"),
   _("Ginger"),
   _("Harley"),
   _("Abby"),
   _("Winnie"),
   _("Nova"),
   _("Kona"),
   _("Riley"),
   _("Zoe"),
   _("Lilly"),
   _("Dixie"),
   _("Lady"),
   _("Izzy"),
   _("Hazel"),
   _("Layla"),
   _("Olive"),
   _("Charlie"),
   _("Sasha"),
   _("Maya"),
   _("Honey"),
   _("Athena"),
   _("Lexi"),
   _("Cali"),
   _("Annie"),
   _("Belle"),
   _("Princess"),
   _("Phoebe"),
   _("Emma"),
   _("Ella"),
   _("Cookie"),
   _("Marley"),
   _("Callie"),
   _("Scout"),
   _("Roxie"),
   _("Remi"),
   _("Minnie"),
   _("Maddie"),
   _("Dakota"),
   _("Leia"),
   _("Poppy"),
   _("Josie"),
   _("Harper"),
   _("Mila"),
   _("Angel"),
   _("Holly"),
   _("Ava"),
   _("Ivy"),
   _("Mocha"),
   _("Gigi"),
   _("Paisley"),
   _("Koda"),
   _("Cleo"),
   _("Penelope"),
   _("Bonnie"),
   _("Missy"),
   _("Frankie"),
   _("Sugar"),
   _("Aspen"),
   _("Xena"),
   _("Shelby"),
   _("Fiona"),
   _("Dolly"),
   _("Georgia"),
   _("Shadow"),
   _("Delilah"),
   _("Peanut"),
   _("Grace"),
   _("Rose"),
   _("Skye"),
   _("Pearl"),
   _("Jasmine"),
   _("Juno"),
   _("Trixie"),
]
PET_NAMES_FISH = [
   _("Finneaus"),
   _("Fishy McFish"),
   _("Swimster"),
   _("Chips"),
   _("Caspian"),
   _("Ripley"),
   _("Bob"),
   _("Bubbles"),
   _("Bigmouth"),
   _("Swimzell"),
   _("Swim Shady"),
   _("Bigmouth Billy"),
   _("Squirtle"),
   _("Long John Silver"),
   _("Mr. Ray"),
   _("Captain Morgan"),
   _("Betta White"),
   _("Small Fry"),
   _("Tuna Piano"),
   _("Harvey"),
]

#------------------------------------------------------------------
# Celebrity list
# For use in situations like '{celebrity} followed you on instagram'; or "you were talking with your {relation} about {adam brody}'s {left ankle}"; "while you were working at {chicken shop} you noticed {seth rogan} stuck in traffic outside. You waved, {he} didn't wave back." etc
# Rough alphabetical order only so far

CELEBRITY_MALE_ACTOR = [
    _("Alex Pettyfer"),
    _("Ashton Kutcher"),
    _("Adam Brody"),
    _("Andrew Garfield"),
    _("Alexander Skarsgård"),
    _("Austin Nichols"),
    _("Allan Hyde"),
    _("Adam Garcia"),
    _("Arnold Schwarzenegger"),
    _("Ben McKenzie"),
    _("Bryan Greenberg"),
    _("Brad Pitt"),
    _("Bradley Cooper"),
    _("Channing Tatum"),
    _("Clive Owen"),
    _("Chace Crawford"),
    _("Cam Gigandet"),
    _("Chris Brown"),
    _("Chris Pine"),
    _("Chad Michael Murray"),
    _("Columbus Short"),
    _("Christian Bale"),
    _("Casey Affleck"),
    _("Cillian Murphy"),
    _("Daniel Craig"),
    _("David Beckham"),
    _("Ed Westwick"),
    _("Eric Bana"),
    _("Emile Hirsch"),
    _("Eric Dane"),
    _("Gerard Butler"),
    _("Garrett Hedlund"),
    _("Hayden Christensen"),
    _("Hugh Jackman"),
    _("Hugh Laurie"),
    _("Hugh Dancy"),
    _("Heath Ledger"),
    _("Ian Somerhalder"),
    _("James Lafferty"),
    _("James Marsden"),
    _("John Mayer"),
    _("Jude Law"),
    _("Jensen Ackles"),
    _("Jake Gyllenhaal"),
    _("Justin Chambers"),
    _("Jesse Metcalfe"),
    _("Justin Timberlake"),
    _("Javier Bardem"),
    _("Joe Manganiello"),
    _("Johnny Depp"),
    _("James Franco"),
    _("Jack O'Connell"),
    _("Kellan Lutz"),
    _("Josh Hartnett"),
    _("Jason Segel"),
    _("Jared Padalecki"),
    _("Joseph Gordon-Levitt"),
    _("Liam Hemsworth"),
    _("Leonardo DiCaprio"),
    _("Luke Pasqualino"),
    _("Milo Ventimiglia"),
    _("Mark Salling"),
    _("Matthew Goode"),
    _("Mads Mikkelsen"),
    _("Marshall Mathers"),
    _("Mekhi Phifer"),
    _("Matt Lanter"),
    _("Mike Vogel"),
    _("Nick Zano"),
    _("Orlando Bloom"),
    _("Patrick Swayze"),
    _("Penn Badgley"),
    _("Peter Facinelli"),
    _("Paul Walker"),
    _("Ryan Gosling"),
    _("Ryan Reynolds"),
    _("Robbie Jones"),
    _("Robert Pattinson"),
    _("Rick Malambri"),
    _("Ryan Kwanten"),
    _("Ryan Phillippe"),
    _("Rafi Gavron"),
    _("Sam Worthington"),
    _("Sean Faris"),
    _("Sylvester Stallone"),
    _("Seth Rogan"),
    _("Shia LaBeouf"),
    _("Stephen Colletti"),
    _("Shane West"),
    _("Simon Rex"),
    _("Taylor Lautner"),
    _("Tom Hardy"),
    _("Tupac Shakur"),
    _("Tristan Mack Wilds"),
    _("Timothy Olyphant"),
    _("Tom Welling"),
    _("Travis Barker"),
    _("Wentworth Miller"),
    _("Zac Efron"),
]
CELEBRITY_MALE_ATHLETE = [
    _("Arnold Schwarzenegger"),
    _("David Beckham"),
]
CELEBRITY_MALE_AUTHOR = [
    _("Joe Manganiello"),
]
CELEBRITY_MALE_BUSINESS = [
    _("Elon Musk"),
]
CELEBRITY_MALE_DANCER = [
    _("Justin Timberlake"),
]
CELEBRITY_MALE_DIRECTOR = [
    _("Joe Manganiello"),
]
CELEBRITY_MALE_FASHION_DESIGNER = [
    _("Michael Kors"),
    _("Tom Ford"),
]
CELEBRITY_MALE_MODEL = [
    _("David Gandy"),
    _("Sean O'Pry"),
]
CELEBRITY_MALE_MUSICIAN = [
    _("Eminem"),
    _("Jared Followill"),
    _("John Mayer"),
    _("Justin Timberlake"),
    _("Tupac Shakur"),
]
CELEBRITY_MALE_POLITICIAN = [
    _("Arnold Schwarzenegger"),
]
CELEBRITY_MALE_PORNSTAR = [
    _("James Deen"),
]
CELEBRITY_MALE_PRODUCER = [
    _("Arnold Schwarzenegger"),
    _("Brad Pitt"),
    _("Joe Manganiello"),
]
CELEBRITY_MALE_ROYAL = [
    _("Prince Carl Philip of Sweden, Duke of Värmland"),
]
CELBRITY_MALE_SCREENWRITER = [
    _("Sylvester Stallone"),
    _("Seth Rogan"),
]
CELEBRITY_MALE_SELF = [
    _("Arnold Schwarzenegger"),
]
CELEBRITY_MALE_SOCIAL_MEDIA = [
    _("Zach King"),
]
CELEBRITY_MALE_WRESTLER = [
    _("Randy Orton"),
]
CELEBRITY_MALE_WRITER = [
    _("Stan Lee"),
]

CELEBRITY_FEMALE_ACTOR = [
    _("Adriana Lima"),
    _("Aishwarya Rai Bachchan"),
    _("Alessandra Ambrosio"),
    _("Amber Heard"),
    _("Ana Beatriz Barros"),
    _("Anna Paquin"),
    _("AnnaSophia Robb"),
    _("Anne Vyalitsyna"),
    _("Angelina Jolie"),
    _("Ashley Benson"),
    _("Ashley Greene"),
    _("Bar Refaeli"),
    _("Behati Prinsloo"),
    _("Beyoncé Knowles"),
    _("Blake Lively"),
    _("Brooklyn Decker"),
    _("Candice Swanepoel"),
    _("Cassie Ventura"),
    _("Charlize Theron"),
    _("Cheryl Cole"),
    _("Chloë Grace Moretz"),
    _("Cindy Crawford"),
    _("Demi Lovato"),
    _("Denise Richards"),
    _("Diane Kruger"),
    _("Doutzen Kroes"),
    _("Elisha Cuthbert"),
    _("Emilia Clarke"),
    _("Emily Blunt"),
    _("Emma Stone"),
    _("Emma Watson"),
    _("Erin Heatherton"),
    _("Eva Green"),
    _("Eva Longoria"),
    _("Eva Mendes"),
    _("Freida Pinto"),
    _("Gisele Bündchen"),
    _("Hilary Duff"),
    _("Indiana Evans"),
    _("Irina Shayk"),
    _("Isabel Lucas"),
    _("Izabel Goulart"),
    _("Jenna Dewan"),
    _("Jennifer Lawrence"),
    _("Jessica Alba"),
    _("Jessica Biel"),
    _("Jordana Brewster"),
    _("Josie Maran"),
    _("Karolina Kurkova"),
    _("Kate Beckinsale"),
    _("Kate Upton"),
    _("Katie Holmes"),
    _("Keira Knightley"),
    _("Kelly Brook"),
    _("Kendall Jenner"),
    _("Kim Kardashian"),
    _("Kristen Stewart"),
    _("Kristin Kreuk"),
    _("Laetitia Casta"),
    _("Lauren Conrad"),
    _("Lily Aldridge"),
    _("Lucy Hale"),
    _("Marion Cotillard"),
    _("Nikki Reed"),
    _("Nina Dobrev"),
    _("Olivia Wilde"),
    _("Malin Akerman"),
    _("Marisa Miller"),
    _("Megan Fox"),
    _("Minka Kelly"),
    _("Mila Kunis"),
    _("Miranda Kerr"),
    _("Monica Bellucci"),
    _("Natalia Vodianova"),
    _("Natalie Portman"),
    _("Nicole Scherzinger"),
    _("Olivia Culpo"),
    _("Penélope Cruz"),
    _("Rachel Bilson"),
    _("Rachel McAdams"),
    _("Rachael Taylor"),
    _("Rachel Weisz"),
    _("Rihanna Fenty"),
    _("Roselyn Sanchez"),
    _("Rosie Huntington-Whiteley"),
    _("Salma Hayek"),
    _("Sara Carbonero"),
    _("Scarlett Johansson"),
    _("Selena Gomez"),
    _("Shanina Shaik"),
    _("Shay Mitchell"),
    _("Sienna Miller"),
    _("Sofía Vergara"),
    _("Stacy Keibler"),
    _("Tyra Banks"),
    _("Vanessa Hudgens"),
    _("Ximena Navarrete"),
    _("Zoe Saldana"),
]
CELEBRITY_FEMALE_ATHLETE = [
    _("Serena Williams"),
]
CELEBRITY_FEMALE_BUSINESS = [
    _("Sofía Vergara"),
]
CELEBRITY_FEMALE_CHEERLEADER = [
    _("Demi Lovato"),
    _("Stacy Keibler"),
]
CELEBRITY_FEMALE_DANCER = [
    _("Ashley Benson"),
    _("Cassie Ventura"),
    _("Jenna Dewan"),
    _("Roselyn Sanchez"),
    _("Stacy Keibler"),
]
CELEBRITY_FEMALE_FASHION_DESIGNER = [
    _("Kim Kardashian"),
    _("Rihanna Fenty"),
]
CELEBRITY_FEMALE_MODEL = [
    _("Adriana Lima"),
    _("Aishwarya Rai Bachchan"),
    _("Alessandra Ambrosio"),
    _("Ana Beatriz Barros"),
    _("Anne Vyalitsyna"),
    _("Bar Refaeli"),
    _("Behati Prinsloo"),
    _("Brooklyn Decker"),
    _("Candice Swanepoel"),
    _("Cassie Ventura"),
    _("Cindy Crawford"),
    _("Denise Richards"),
    _("Doutzen Kroes"),
    _("Elisha Cuthbert"),
    _("Eva Green"),
    _("Gisele Bündchen"),
    _("Irina Shayk"),
    _("Izabel Goulart"),
    _("Jenna Dewan"),
    _("Josie Maran"),
    _("Karolina Kurkova"),
    _("Kate Upton"),
    _("Kelly Brook"),
    _("Kendall Jenner"),
    _("Laetitia Casta"),
    _("Lily Aldridge"),
    _("Malin Akerman"),
    _("Marisa Miller"),
    _("Miranda Kerr"),
    _("Monica Bellucci"),
    _("Natalia Vodianova"),
    _("Olivia Culpo"),
    _("Rachael Taylor"),
    _("Roselyn Sanchez"),
    _("Rosie Huntington-Whiteley"),
    _("Shay Mitchell"),
    _("Sienna Miller"),
    _("Sofía Vergara"),
    _("Stacy Keibler"),
    _("Tyra Banks"),
    _("Ximena Navarrete"),
]
CELEBRITY_FEMALE_MUSICIAN = [
    _("Ashley Benson"),
    _("Beyoncé Knowles"),
    _("Cassie Ventura"),
    _("Cheryl Cole"),
    _("Demi Lovato"),
    _("Indiana Evans"),
    _("Minka Kelly"),
    _("Rihanna Fenty"),
    _("Roselyn Sanchez"),
    _("Selena Gomez"),
]
CELEBRITY_FEMALE_POLITICIAN = [
    _("Hillary Clinton"),
]
CELEBRITY_FEMALE_PORNSTAR = [
    _("Jenna Jameson"),
]
CELEBRITY_FEMALE_PRODUCER = [
    _("Charlize Theron"),
    _("Cindy Crawford"),
    _("Marion Cotillard"),
    _("Roselyn Sanchez"),
    _("Selena Gomez"),
    _("Tyra Banks"),
]
CELEBRITY_FEMALE_ROYAL = [
    _("Catherine Middleton, Princess of Wales"),
]
CELBRITY_FEMALE_SCREENWRITER = [
    _("Nikki Reed"),
]
CELEBRITY_FEMALE_SELF = [
    _("Catherine Middleton, Princess of Wales"),
    _("Natalia Vodianova"),
    _("Pippa Middleton"),
]
CELEBRITY_FEMALE_SOCIAL_MEDIA = [
    _("Olivia Culpo"),
]
CELEBRITY_FEMALE_WRESTLER = [
    _("Stacy Keibler"),
]
CELEBRITY_FEMALE_WRITER = [
    _("Kim Kardashian"),
    _("Roselyn Sanchez"),
    _("Shay Mitchell"),
    _("Tyra Banks"),
]
CELEBRITY_BAND = [
    _("The Backstreet Boys"),
    _("The Beatles"), 
    _("Pink Floyd"),
    _("The Rolling Stones"),
]

# List of Urban locations (a park, a bank etc.) called after 'to' or 'at' "we went to {urban_location}", "we spent time at {urban_location}"
# terms like 'downtown' arent in this list. you cant write 'spent time at downtown' over 'spent time downtown', or 'went to downtown' over 'went downtown'
# 'downtown' and other similar terms are in URBAN_DIRECTIONAL below

URBAN_LOCATION = [
	_("an abandoned building"),
	_("an abandoned factory"),
	_("an abandoned house"),
	_("an abandoned office building"),
	_("an abandoned school"),
	_("an airport"),
	_("an airfield"),
	_("an alleyway"),
	_("an ambulance station"),
	_("an apartment building"),
	_("an aquarium"),
	_("an arcade"),
	_("an art gallery"),
	_("an avenue"),
	_("a bakery"),
	_("a bank"),
	_("a bar"),
	_("a barber shop"),
	_("a beauty salon"),
	_("a bed & breakfast"),
	_("a bicycle rental stand"),
	_("a billboard"),
	_("a bookstore"),
	_("a boulevard"),
	_("a bowling alley"),
	_("a bridge"),
	_("a bus stop"),
	_("a butcher's shop"),
	_("a cafe"),
	_("a canal"),
	_("the central business district"),
	_("a church"),
	_("City Hall"),
	_("a clinic"),
	_("a coffee shop"),
	_("a college"),
	_("a community centre"),
	_("a community gardens"),
	_("a concert hall"),
	_("a condominium"),
	_("a construction site"),
	_("a convenience store"),
	_("a court"),
	_("a cycle highway"),
	_("a daycare centre"),
	_("a dentist"),
	_("a department store"),
	_("a dock"),
	_("the docks"),
	_("a doctor's office"),
	_("some drainage infrastructure"),
	_("a dry cleaner"),
	_("an embassy"),
	_("a factory"),
	_("a fire hydrant"),
	_("a fire station"),
	_("a flower shop"),
	_("a garbage facility"),
	_("a garden"),
	_("a gardens"),
	_("a government building"),
	_("a green-roof"),
	_("a grocery store"),
	_("a greengrocer"),
	_("a gym"),
	_("a gymnasium"),
	_("a harbour"),
	_("the harbour"),
	_("a highway"),
	_("a historical building"),
	_("a historical site"),
	_("a hospital"),
	_("a hotel"),
	_("a house"),
	_("a jail"),
	_("a karaoke bar"),
	_("a karaoke lounge"),
	_("a landmark"),
	_("a laundromat"),
	_("a library"),
	_("a linear park"),
	_("a market"),
	_("the markets"),
	_("a mixed-use building"),
	_("a mixed-use street"),
	_("a monument"),
	_("a movie theatre"),
	_("a museum"),
    _("a music festival"),
	_("a nature reserve"),
	_("a newspaper office"),
	_("some night architecture"),
	_("a nightclub"),
	_("a nursery school"),
	_("a nursing home"),
	_("an observatory"),
	_("an office building"),
	_("an opera house"),
	_("some outdoor seating"),
	_("an overpass"),
	_("a park"),
	_("a patisserie"),
	_("some pedestrian infrastructure"),
	_("a performance theatre"),
	_("a pharmacist"),
	_("a place of worship"),
	_("a play street"),
	_("a playground"),
	_("a police station"),
	_("a pond"),
	_("a port"),
	_("the port"),
	_("a post office"),
	_("a prison"),
	_("a product showroom"),
	_("a pub"),
	_("a public bath"),
	_("a public pool"),
	_("a public square"),
	_("a public toilet"),
	_("a radio station"),
	_("a railway line"),
	_("a railway station"),
	_("a recreation centre"),
	_("a recreation facility"),
	_("some remarkable architecture"),
	_("a restaurant"),
	_("a river"),
	_("a school"),
	_("the sewers"),
    _("a shoe store"),
	_("a shopping centre"),
	_("a shopping mall"),
	_("a shop"),
	_("a skating rink"),
	_("a skyscraper"),
	_("a spa"),
	_("a sports facility"),
	_("a sports shop"),
	_("a sports stadium"),
	_("a sports store"),
	_("a stadium"),
	_("a stream"),
	_("a street"),
	_("some street art"),
	_("a street food vendor"),
	_("a street vendor"),
	_("a street light"),
	_("some street lights"),
	_("a strip of shops"),
	_("a subway station"),
	_("a swimming pool"),
	_("a synagogue"),
	_("a taxi stand"),
	_("a technology centre"),
	_("some tech infrastructure"),
	_("a television station"),
	_("a tennis court"),
	_("a temple"),
	_("a temple complex"),
	_("a theme park"),
	_("a tower"),
	_("a traffic light"),
	_("some traffic lights"),
	_("a train line"),
	_("a train station"),
	_("a tree"),
	_("some trees"),
	_("the underground"),
	_("an underpass"),
	_("a university"),
	_("an urban farm"),
	_("an urban forest"),
	_("a vending machine"),
	_("some vending machines"),
	_("a vertical park"),
	_("a visitor centre"),
	_("a void deck"),
	_("a water pipe"),
	_("some water pipes"),
	_("a water tower"),
	_("a waterfront"),
	_("the waterfront"),
	_("a waterfront tower"),
	_(""),
	_(""),
]

# List of urban story building directional movement terms.
# E.g. for 'we went {downtown} to {an urban forest}', or 'we spent time {across town} at {a void deck}

URBAN_DIRECTIONAL = [
	_("across the river"),
	_("across town"),
	_("downtown"),
	_("down the road"),
	_("over the road"),
	_("up the road"),
	_("up the street"),
	_(""),
]

# List of past tense urban movement terms
# Use for 'We {took the train} {downtown} to {an urban forest}

URBAN_MOVEMENT = [
	_("caught the bus"),
	_("hiked"),
	_("hitch-hiked"),
	_("jogged"),
	_("knocked about"),
	_("legged it"),
	_("meandered"),
	_("ran"),
	_("rode"),
	_("rowed a boat"),
	_("skated"),
	_("took a bus"),
	_("took a cab"),
	_("took a taxi"),
	_("took the train"),
	_("took a water taxi"),
	_("walked"),
	_("went jogging"),
]

# List of rural locations

RURAL_LOCATION = [
	_("a barn"),
    _("a campsite"),
	_("a country lane"),
    _("a country music festival"),
	_("a dam"),
	_("a farm"),
	_("a field"),
	_("a fish farm"),
	_("a paddock"),
	_("a hay shed"),
    _("a wildlife preserve"),
	_("a windmill"),
]

# List of Natural locations (a mountain, a forest etc.)

NATURAL_LOCATION = [
	_("an alluvial fan"),
	_("an archipelago"),
	_("the archipelago"),
	_("an atoll"),
	_("a sand bar"),
	_("a barchan"),
	_("a basin"),
	_("the bay"),
	_("a coastal bay"),
	_("the bayside"),
	_("a beach"),
	_("the beach"),
	_("a butte"),
	_("the buttes"),
	_("a cape"),
	_("a canyon"),
	_("the canyon"),
	_("a cave"),
	_("the caves"),
	_("a channel"),
	_("a cliff"),
	_("the cliffs"),
	_("the coast"),
	_("a desert"),
	_("the desert"),
	_("a divide"),
	_("a dune"),
	_("a crescent dune"),
	_("a sand dune"),
	_("a geyser"),
	_("the geysers"),
	_("a glacier"),
	_("a gorge"),
	_("the gorge"),
	_("the grasslands"),
	_("the gulf"),
	_("a gully"),
	_("a dry gully"),
	_("a hill"),
	_("the hills"),
	_("an iceberg"),
	_("an ice sheet"),
	_("an inselberg"),
	_("an island"),
	_("the islands"),
	_("an isthmus"),
	_("a jungle"),
	_("the jungle"),
	_("a lagoon"),
	_("a moraine"),
	_("a mountain"),
	_("the mountains"),
	_("the base of a mountain"),
	_("the foot of a mountain"),
	_("a mountain peak"),
	_("a mountain range"),
	_("the mountain range"),
	_("the top of a mountain"),
	_("a fjord"),
	_("a forest"),
	_("the forest"),
	_("a deciduous forest"),
	_("a temperate forest"),
	_("a lake"),
	_("the lake"),
	_("the edge of a lake"),
	_("a salt lake"),
	_("the salt lakes"),
	_("a marsh"),
	_("the marshes"),
	_("a mesa"),
	_("the mouth of the river"),
	_("an oasis"),
	_("the ocean"),
	_("a salt pan"),
	_("a peninsula"),
	_("the peninsula"),
	_("a plain"),
	_("the plains"),
	_("a flood plain"),
	_("the flood plains"),
	_("a pediment"),
	_("the plateau"),
	_("a pond"),
	_("a prairie"),
	_("the quays"),
	_("a rainforest"),
	_("a subtropical rainforest"),
	_("a tropical rainforest"),
	_("a ravine"),
	_("the ravine"),
	_("a reef"),
	_("a coral reef"),
	_("the coral reef"),
	_("a river"),
	_("the river"),
	_("a river basin"),
	_("the river basin"),
	_("a river delta"),
	_("the river delta"),
	_("the source of a river"),
	_("a savanna"),
	_("the sea"),
	_("the seaside"),
	_("the shrublands"),
	_("the sound"),
	_("a coastal sound"),
	_("a steppe"),
	_("the steppes"),
	_("a strait"),
	_("a stream"),
	_("a swamp"),
	_("the swamp"),
	_("a tributary"),
	_("a tundra"),
	_("the tundra"),
	_("a valley"),
	_("a river valley"),
	_("a volcano"),
	_("an active volcano"),
	_("a dormant volcano"),
	_("an extinct volcano"),
	_("a wadi"),
	_("some wadis"),
	_("a waterfall"),
	_("the waterfalls"),
	_("a wetland"),
	_("the wetlands"),
	_("some yardangs"),
	_("some zeugens"),
]

# List of Environmental locations. E.g. 'You practiced writing a story, you chose comic sans and began with "It was {a dark and stormy night}', or "You {beat the meat} while thinking of {margaret thatcher} on {a hot sunny day}"

ENVIRONMENTAL_LOCATION = [
    _("a hot night"),
    _("a cold night"),
    _("a dark and stormy night"),
    _("a windy night"),
    _("a clear and starry night"),
    _("a hot sunny day"),
    _("a hot day"),
    _("a cold day"),
    _("a wet and windy day"),
    _("a windy day"),
    _("a cool, overcast evening"),
    _("a wet windy evening"),
    _("a hot sweaty evening"),
    _("a brisk early morning"),
    _("a warm overcast morning"),
    _(""),
]

# Body parts for squabbles, fights etc.
# E.g. 'you squabbled with your {sibling} for not sharing {his_her} candy.' -> 'your {sibling} stormed you! {he_she} ripped your nipple.' 

BODYPART = [
    _("arm"),
    _("head"),
    _("leg"),
    _("foot"),
    _("knee"),
]

# Fighting words
# Same gist as above, e.g. for when you get attacked in a park and someone gouges your belly button or bites your pinky toe

ATTACK_WORD = [
	_("punched"),
	_("hit"),
	_("kicked"),
	_("attacked"),
	_("bit"),
]

# Insults: does what it says on the box. opposite list of compliments. (can be premised with 'called you {insults}')
INSULTS = [
    _("a dimwit"),
    _("a dork"),
    _("a douchebag"),
    _("a dummy"),
    _("a dunce"),
    _("a fatty"),
    _("a freak"),
    _("a goblin"),
    _("a jerk"),
    _("a jumpoff"),
    _("a lamebrain"),
    _("a loser"),
    _("a maniac"),
    _("a mouth-breather"),
    _("a pig"),
    _("a pumpkinhead"),
    _("a punk"),
    _("a scallywag"),
    _("a simpleton"),
    _("a snake"),
    _("a tool"),
    _("a tramp"),
    _("a triple-chin"),
    _("a twat"),
    _("a twit"),
    _("a villain"),
    _("a vulture"),
    _("a weasel"),
    _("an abomination to mankind"),
    _("an airhead"),
    _("an idiot"),
    _("an imbecile"),
    _("awful"),
    _("brainless"),
    _("careless"),
    _("dumb"),
    _("evil"),
    _("foolhardy"),
    _("mediocre at best"),
    _("mentally defective"),
    _("nasty"),
    _("obtuse"),
    _("psycho"),
    _("putrid"),
    _("skeezy"),
    _("stupid"),
    _("trashy"),
    _("weak"),
    _("weaksauce"),
]
