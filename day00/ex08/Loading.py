def ft_tqdm(lst: range) -> None:
	max_len = len(lst)
	for i in lst:
		percent = (i / max_len) * 100
		nb_cases = int((percent / 100) * 63)
		progress_bar = f"{percent:3.0f}%|"
		progress_bar += '█' * nb_cases
		progress_bar += ' ' * (63 - nb_cases)
		progress_bar += f"| {i}/{max_len}\r"
		print(progress_bar, end='')
		yield i
	print(f"100%|{'█' * 63}| {max_len}/{max_len}\r", end='')