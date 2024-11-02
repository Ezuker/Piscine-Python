import sys
import string


def no_arg_management():
	"""
	Reads a line from standard input and returns it.
	Returns:
	str: The line read from standard input.
	"""
	for line in sys.stdin:
		return line


def main():
	"""
	Main function
	"""
	if len(sys.argv) > 2:
		print("AssertionError: provide a single argument")
		sys.exit(1)
	if len(sys.argv) == 2:
		text = sys.argv[1]
	else:
		text = no_arg_management()
	print(f"The text contains {len(text)} characters")
	print(sum(1 for c in text if c.isupper()), "upper letters")
	print(sum(1 for c in text if c.islower()), "lower letters")
	print(sum(1 for c in text if c in string.punctuation), "punctuation marks")
	print(sum(1 for c in text if c.isspace()), "spaces")
	print(sum(1 for c in text if c.isdigit()), "digits")


if __name__ == '__main__':
	main()
