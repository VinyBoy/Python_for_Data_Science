import sys


def printError() -> None:
    nameError = "AssertionError:"
    print(f"{nameError} more than one argument is provided")


def checkArg(arg) -> None:
    nameError = "AssertionError:"
    try:
        number = int(arg)
    except ValueError:
        print(f"{nameError} argument is not an integer")
        sys.exit()
    if (number % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    if (len(sys.argv) == 1):
        sys.exit()
    if (len(sys.argv) > 2):
        printError()
        sys.exit()
    checkArg(sys.argv[1])

#Execute main() seulement si ce fichier python est lancer directement depuis le terminal
#Chaque fichier .py possede une variable appeler __name__
if __name__ == "__main__":
    main()
