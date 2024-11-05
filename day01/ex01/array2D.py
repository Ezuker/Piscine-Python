import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
	try:
		np_array = np.array(family)
	except ValueError as e:
		print(f"Assertion error {e}")
		return []
	print(f"My shape is {np_array.shape}")
	np_array = np_array[start:end]
	print(f"My new shape is {np_array.shape}")
	return np_array.tolist()
	