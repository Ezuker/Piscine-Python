import sys
import re


def to_morse_code(text, NESTED_MORSE):
	"""
	Translate the text by morse code and print it
	"""
	new_text = ""
	for c in text:
		if c not in NESTED_MORSE:
			print("AssertionError: the arguments are bad")
			return
		new_text += (NESTED_MORSE[c])
	print(new_text)


def main():
	if len(sys.argv) != 2:
		print("AssertionError: the arguments are bad")
		return
	text = sys.argv[1]
	NESTED_MORSE = {
		" ": "/ ",
		"A": ".- ", "a": ".- ",
		"B": "-... ", "b": "-... ",
		"C": "-.-. ", "c": "-.-. ",
		"D": "-.. ", "d": "-.. ",
		"E": ". ", "e": ". ",
		"F": "..-. ", "f": "..-. ",
		"G": "--. ", "g": "--. ",
		"H": ".... ", "h": ".... ",
		"I": ".. ", "i": ".. ",
		"J": ".--- ", "j": ".--- ",
		"K": "-.- ", "k": "-.- ",
		"L": ".-.. ", "l": ".-.. ",
		"M": "-- ", "m": "-- ",
		"N": "-. ", "n": "-. ",
		"O": "--- ", "o": "--- ",
		"P": ".--. ", "p": ".--. ",
		"Q": "--.- ", "q": "--.- ",
		"R": ".-. ", "r": ".-. ",
		"S": "... ", "s": "... ",
		"T": "- ", "t": "- ",
		"U": "..- ", "u": "..- ",
		"V": "...- ", "v": "...- ",
		"W": ".-- ", "w": ".-- ",
		"X": "-..- ", "x": "-..- ",
		"Y": "-.-- ", "y": "-.-- ",
		"Z": "--.. ", "z": "--.. ",
		"1": ".---- ", "2": "..--- ",
		"3": "...-- ", "4": "....- ",
		"5": "..... ", "6": "-.... ",
		"7": "--... ", "8": "---.. ",
		"9": "----. ", "0": "----- "
	}
	to_morse_code(text, NESTED_MORSE)


if __name__ == '__main__':
	main()