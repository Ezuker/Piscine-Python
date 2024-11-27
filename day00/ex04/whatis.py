from sys import exit, argv

if __name__ == '__main__':
	if (argv) > 2:
		print("AssertionError: more than one argument is provided")
		exit(1)
	elif len(argv) == 1:
		exit(1)
	number = argv[1]
	try:
		if int(number) % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except:
		print("AssertionError: argument is not an integer")