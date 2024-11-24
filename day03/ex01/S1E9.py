from abc import ABC, abstractmethod

class Character(ABC):
	"""
	Class Character
	"""
	@abstractmethod
	def __init__(self, first_name, is_alive=True):
		"""
		Init Character object
		"""
		super().__init__()
		self.first_name = first_name
		self.is_alive = is_alive
 
	def die(self):
		"""
		Function that make is_alive to False
		"""
		self.is_alive = False


class Stark(Character):
	"""
	Class Stark
	"""
	def __init__(self, first_name, is_alive=True):
		"""
		Init Stark object
		"""
		super().__init__(first_name, is_alive)
	pass