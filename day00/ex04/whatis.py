from sys import exit, argv

if __name__ == '__main__':
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        if len(argv) == 1:
            exit(1)
        assert argv[1].isdigit(), "argument is not an integer"
        if int(argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
