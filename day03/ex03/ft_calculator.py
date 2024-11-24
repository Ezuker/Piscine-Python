class calculator:
	def __init__(self, arg):
		self.arg = arg

	def __add__(self, object) -> None:
		self.arg = [x + object for x in self.arg]
		print(self.arg)
		return self.arg

	def __mul__(self, object) -> None:
		self.arg = [x * object for x in self.arg]
		print(self.arg)
		return self.arg

	def __sub__(self, object) -> None:
		self.arg = [x - object for x in self.arg]
		print(self.arg)
		return self.arg

	def __truediv__(self, object) -> None:
		if object == 0:
			return
		self.arg = [x / object for x in self.arg]
		print(self.arg)
		return self.arg
