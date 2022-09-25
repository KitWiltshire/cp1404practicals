def main():
    password = get_password()
    create_stars(password)


def get_password():
    password = input("Enter password: ")
    return password


def create_stars(password):
    for i in range(len(password)):
        print("*", end='')


main()
