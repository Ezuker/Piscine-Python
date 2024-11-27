from sys import argv
from string import printable, punctuation
from ft_filter import ft_filter


def main():
	try:
		text = str(argv[1])
		number = int(argv[2])
	except IndexError:
		print("AssertionError: the arguments are bad")
	except ValueError:
		print("AssertionError: the arguments are bad")
	if sum(1 for c in text if c in punctuation) >= 1:
		print("AssertionError: the arguments are bad")
		return
	if sum(1 for c in text if c in printable) != len(text):
		print("AssertionError: the arguments are bad")
		return
	first_list = text.split()
	last_list = ft_filter(lambda word: len(word) > number, first_list)
	print(list(last_list))


if __name__ == "__main__":
	main()
