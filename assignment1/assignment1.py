"""
Name: Kit Wiltshire
Date started: 24/10/2022
GitHub URL:
"""


def main():
    """This function will be in charge of the whole program with other functions inside that do the complex
    things """
    print("Movies To Watch 1.0 - by Kit Wiltshire")
    menu_input = get_valid_menu_input()
    movies_backup_file = open("movies_backup.csv", "r+")
    movies_file = open("movies.csv", "w+")
    movies_content = movies_backup_file.read()
    movies_file.write(movies_content)
    movies_backup_file.close()
    while menu_input != "Q":
        if menu_input == "D":
            movies_file.seek(0)
            movies_list = movies_file.readlines()
            print(movies_list)
            for movie in range(len(movies_list)):
                print(f"{movie+1}. {movies_list[movie]}", end="")
            #TODO: count the movies watched and movies unwatched and print it out
        elif menu_input == "A":
            new_movie = add_new_movie()
            movies_file.write(f"\n{new_movie}")
            movies_file.seek(0)
            movies_content = movies_file.read()
        else: #when the user presses "w"
            print("Enter the number of a movie to mark as watched")
            try:
                movie_to_watch = int(input(">>> "))
                while movie_to_watch != int and movie_to_watch < 1:
                    if movie_to_watch == "":
                        print("Input can not be blank")
                    elif movie_to_watch < 1:
                        print("Number must be >= 1")
                    elif movie_to_watch > len(movies_list):
                        print("Invalid movie number")
                    movie_to_watch = int(input(">>> "))
            except ValueError:
                print("Invalid input; enter a valid number")
                movie_to_watch = input(">>> ")
            #TODO: do an if statement for when a movie has already been watched and also turn a movie that hasn't been watched into a watched one

        menu_input = get_valid_menu_input()

    print("Have a nice day :)")
    movies_file.close()


def get_valid_menu_input():
    """Will ask for a valid response in the menu"""
    print("Menu:\nD - Display movies \nA - Add new movie \nW - Watch a movie \nQ - Quit")
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


def add_new_movie():
    CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
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
