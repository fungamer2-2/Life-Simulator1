import random
from random import randint

from src.lifesim_lib.lifesim_lib import clamp, Gender

class SocialMedia:
	
	def __init__(self):
		self.followers = 0
		self.likes = 0