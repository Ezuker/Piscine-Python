import sys

if __name__ == '__main__':
	if (sys.argv) > 2:
		print("AssertionError: more than one argument is provided")
		sys.exit(1)
	elif len(sys.argv) == 1:
		sys.exit(1)
	number = sys.argv[1]
	try:
		if int(number) % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except:
		print("AssertionError: argument is not an integer")