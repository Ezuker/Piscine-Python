def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	try:
		if (len(height) != len(weight)):
			raise ValueError("bad arguemnts")
		for item in height:
			if not isinstance(item, (int, float)):
				raise ValueError("bad arguments")
		for item in weight:
			if not isinstance(item, (int, float)):
				raise ValueError("bad arguments")
	except ValueError as e:
		print(f"AssertionError: {e}")
		return
	bmi_list = [w / h ** 2 for h, w in zip(height, weight)]
	return bmi_list

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	try:
		for item in bmi:
			if not isinstance(item, (int, float)):
				raise ValueError("bad arguments")
	except ValueError as e:
		print(f"AssertionError: {e}")
		return
	limit_list = [n > limit for n in bmi]
	return limit_list
