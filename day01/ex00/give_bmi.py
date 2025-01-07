def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""Calculate the Body Mass Index

	Args:
		height (list[int  |  float]): Height of people
		weight (list[int  |  float]): Weight of people

	Returns:
		list[int | float]: A list of body mass index for all people
	"""
	try:
		assert len(height) == len(weight), "bad arguments"
		for item in height:
			assert isinstance(item, (int, float)), "bad arguments"
		for item in weight:
			assert isinstance(item, (int, float)), "bad arguments"
	except AssertionError as e:
		print(f"AssertionError: {e}")
		return []
	bmi_list = [w / h ** 2 for h, w in zip(height, weight)]
	return bmi_list

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""Return list of bool and compare the list to a limit

	Args:
		bmi (list[int  |  float]): Body Mass Index List
		limit (int): The limit of the BMI

	Returns:
		list[bool]: Return a list of bool, false if BMI < limit, else true
	"""
	try:
		for item in bmi:
			assert isinstance(item, (int, float)), "bad arguments"
	except AssertionError as e:
		print(f"AssertionError: {e}")
		return
	limit_list = [n > limit for n in bmi]
	return limit_list
