def square(x: int | float) -> int | float:
	return x * x

def pow(x: int | float) -> int | float:
	return x ** x

def outer(x: int | float, function) -> object:
	count = 0
	def inner() -> float:
		nonlocal x
		x = function(x)
		return x
	return inner