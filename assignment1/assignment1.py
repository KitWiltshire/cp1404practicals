"""
Name: Kit Wiltshire
Date started: 24/10/2022
GitHub URL:
"""


def main():
    """This function will be in charge of the whole program with other functions inside that do the complex
    things """
    CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
    print("Movies To Watch 1.0 - by Kit Wiltshire")
    MENU = "D - Display movies \nA - Add new movie \nW - Watch a movie \nQ - Quit"
    print(MENU)
    menu_input = get_valid_menu_input()
    movies_backup_file = open("movies_backup.csv", "r")
    movies_file = open("movies.csv", "w")
    initial_movies_content = movies_backup_file.read()
    movies_file.write(initial_movies_content)
    print(initial_movies_content)
    if menu_input == "D":
        print(initial_movies_content)
    elif menu_input == "A":
        new_movie = add_new_movie(CATEGORIES)
        print(new_movie)



def get_valid_menu_input():
    """Will ask for a valid response in the menu"""
    menu_input = input(">>> ").upper()
    while menu_input != "D" and menu_input != "A" and menu_input != "W" and menu_input != "Q":
        print("Invalid menu choice")
        menu_input = input(">>> ").upper()
    return menu_input

# name = input("Name: ")
# out_file = open("minecraft.txt", "w")
# print(name, file=out_file)
# print(out_file)
# out_file.close()


def add_new_movie(CATEGORIES):
    movie_title = input("Title: ")
    while movie_title == "":
        print("Input can not be blank")
        movie_title = input("Title: ")
    try:
        movie_year = int(input("Year: "))
        while movie_year != int and movie_year < 1:
            if movie_year == "":
                print("Input can not be blank")
            elif movie_year < 1:
                print("Number must be >= 1")
            movie_year = int(input("Year: "))
    except ValueError:
        print("Invalid input; enter a valid number")
        movie_year = input("Year: ")
    # TODO: Fix the code so it will continue to ask for a year if the input is not a number
    print(f"Categories available: {CATEGORIES}")
    movie_category = input("Category: ").capitalize()
    if movie_category not in CATEGORIES:
        print("Invalid category; using Other")
        movie_category = "Other"
    print(f"{movie_title} ({movie_category} from {movie_year}) added to movie list")
    new_movie = f"{movie_title},{movie_year},{movie_category},u"
    return new_movie


if __name__ == '__main__':
    main()
