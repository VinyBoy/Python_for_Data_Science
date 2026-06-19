import sys


def ft_filter(function, iterable):
    """USe filter with lamda on element of iterable and return the result"""
    result = []
    for element in iterable:
        if function(element):
            result.append(element)
    return result
    

def check_arg(arg2) -> bool:
    """Check if arg2 is int"""
    try:
        n = int(arg2)
    except ValueError:
        return (False)
    return (True)


def print_bad_args():
    """Print error and exit"""
    print("AssertionError: the arguments are bad")
    sys.exit()


def main():
    """Run the programm"""
    if len(sys.argv) != 3:
        print_bad_args()
    if not check_arg(sys.argv[2]):
        print_bad_args()
    words = sys.argv[1].split()
    n = int(sys.argv[2])
    result = ft_filter(lambda word: len(word) > n, words)
    print(result)
    


if __name__ == "__main__":
    main()
