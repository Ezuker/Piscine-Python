def slice_me(family: list, start: int, end: int) -> list:
	try:
		model_len = len(family[0])
		for n in family:
			if model_len != len(n):
				raise ValueError("bad arguments")
	except ValueError as e:
		print(f"Assertion error {e}")
		return
	print(f"My shape is ({len(family)}, {model_len})")
	new_list = family[start:end]
	print(f"My new shape is ({len(new_list)}, {len(new_list[0])})")
	return new_list
	