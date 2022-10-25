"""
Name: Kit Wiltshire
Date started: 24/10/2022
GitHub URL:
"""


def main():
    """This function will be in charge of the whole program with other functions inside that do the complex
    things """
    print("Movies To Watch 1.0 - by Kit Wiltshire")
    MENU = "D - Display movies \nA - Add new movie \nW - Watch a movie \nQ - Quit"
    print(MENU)
    menu_input = get_valid_menu_input()



def get_valid_menu_input():
    """Will ask for a valid response in the menu"""
    menu_input = input(">>> ").upper()
    while menu_input != "D" and menu_input != "A" and menu_input != "W" and menu_input != "Q":
        print("Invalid menu choice")
        menu_input = input(">>> ").upper()
    return menu_input


if __name__ == '__main__':
    main()
