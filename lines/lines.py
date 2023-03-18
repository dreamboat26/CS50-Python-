import sys


def main():
    # Check the command-line arguments
    arg_check(sys.argv)

    # Print the number of lines of code
    print(get_lines(sys.argv[1]))


def arg_check(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def get_lines(filename):
    counter = 0
    try:
        with open(filename) as file:
            for line in file:
                if not line.lstrip().startswith("#") and not line.isspace():
                    counter += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return counter


if __name__ == "__main__":
    main()