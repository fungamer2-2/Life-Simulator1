import random
from random import randint
from collections import deque

from src.lifesim_lib.lifesim_lib import clamp, Gender

class SocialMedia:
	
	def __init__(self):
		self.followers = 0
		self.likes = 0
		self.recent_likes = deque()