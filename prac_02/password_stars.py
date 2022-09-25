def main():
    """Asks for password and turns it into asterisks or stars"""
    password = get_password()
    create_stars(password)


def get_password():
    """this is the code that gets an input from the user for the password"""
    password = input("Enter password: ")
    return password


def create_stars(password):
    """converts a string of characters into just asterisks"""
    for i in range(len(password)):
        print("*", end='')


main()
