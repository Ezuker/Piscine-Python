from sys import argv, exit
from string import printable as prt, punctuation
from ft_filter import ft_filter


def main():
    """
    Main function
    """
    arg = "the arguments are bad"
    try:
        assert len(argv) == 3, arg
        text = str(argv[1])
        assert argv[2].isdigit(), arg
        number = int(argv[2])
        assert sum(1 for c in text if c in punctuation) == 0, arg
        assert sum(1 for c in text if c in prt) == len(text), arg
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        exit(1)
    first_list = text.split(" ")
    last_list = ft_filter(lambda word: len(word) > number, first_list)
    print(list(last_list))


if __name__ == "__main__":
    main()
