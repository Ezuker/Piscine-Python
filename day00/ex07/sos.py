from sys import argv, exit


def to_morse_code(text, NESTED_MORSE):
    """
    Translate the text by morse code and print it
    """
    new_text = ""
    for c in text:
        try:
            assert c in NESTED_MORSE, "the arguements are bad"
        except AssertionError as e:
            print(f"AssertionError: {e}")
            exit(1)
        new_text += (NESTED_MORSE[c])
    print(new_text)


def main():
    """
    Main function
    """
    try:
        assert len(argv) == 2, "You need only one argument"
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        exit(1)
    text = argv[1]
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
