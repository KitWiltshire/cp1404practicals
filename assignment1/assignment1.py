"""
Name: Kit Wiltshire
Date started: 24/10/2022
GitHub URL:
"""
MOVIE_FILE = "movies.csv"
MENU_STRING = "Menu:\nD - Display movies \nA - Add new movie \nW - Watch a movie \nQ - Quit"

# CONSTANTS FOR MOVIES
WATCHED = "w"
NOT_WATCHED = "u"
TITLE_INDEX = 0
YEAR_INDEX = 1
GENRE_INDEX = 2
WATCHED_INDEX = 3


def main():
    """This function will be in charge of the whole program with other functions inside that do the more complex
    things """
    print("Movies To Watch 1.0 - by Kit Wiltshire")
    movie_list = get_movie_list()  # Read content
    movie_list.sort(key=lambda year: year[YEAR_INDEX])  # Sort the list by year
    menu_input = get_valid_menu_input()
    while menu_input != "Q":
        movies_watched = 0
        movies_unwatched = 0
        for movie in movie_list:
            if movie[3] == WATCHED:  # When the 4th element in the list i.e 'u' or 'w' is watched
                movies_watched += 1
            else:
                movies_unwatched += 1
        if menu_input == "D":
            for index, movie in enumerate(movie_list):
                if movie[WATCHED_INDEX] == NOT_WATCHED:
                    print(f" {index + 1}. * {movie[TITLE_INDEX]} - {movie[YEAR_INDEX]} ({movie[GENRE_INDEX]})")
                else:
                    print(f" {index + 1}.   {movie[TITLE_INDEX]} - {movie[YEAR_INDEX]} ({movie[GENRE_INDEX]})")
            print(f"{movies_watched} movies watched, {movies_unwatched} movies still to watch.")
        elif menu_input == "A":
            new_movie = add_new_movie()
            new_movie = new_movie.split(",")  # Separates the content in the new movie by the comma to make a list
            movie_list.append(new_movie)
            movie_list.sort(key=lambda year: year[YEAR_INDEX])
        else:  # when the user presses "w"
            if movies_watched == len(movie_list):  # When the user has watched all the movies
                print("No more movies to watch!")
            else:
                movie_to_watch = 0
                print("Enter the number of a movie to mark as watched")
                movie_to_watch = watch_movie(movie_list, movie_to_watch)
                try:
                    if movie_list[movie_to_watch - 1][3] == "w":
                        print(f"You have already watched {movie_list[movie_to_watch - 1][TITLE_INDEX]}")
                    else:
                        movie_list[movie_to_watch - 1][3] = "w"
                        print(f"{movie_list[movie_to_watch - 1][TITLE_INDEX]} from "
                              f"{movie_list[movie_to_watch - 1][YEAR_INDEX]} watched")
                except IndexError:
                    print("Invalid movie number")
        menu_input = get_valid_menu_input()
    file = open("movies.csv", 'w')
    for movie in movie_list:
        file.write(f"{movie[0]},{movie[1]},{movie[2]},{movie[3]}\n")  # Converts the items from the lists into just text
    file.close()
    print(f"{len(movie_list)} movies saved to {MOVIE_FILE}")
    print("Have a nice day :)")


def watch_movie(movie_list, movie_to_watch):
    """Will ask the user to watch a movie based on number and only work if the user gives a valid response"""
    valid_movie_to_watch_input = False
    while not valid_movie_to_watch_input:
        try:
            movie_to_watch = int(input(">>> "))
            if movie_to_watch == "":
                print("Input can not be blank")
            elif movie_to_watch > len(movie_list):
                print("Invalid movie number")
            else:
                valid_movie_to_watch_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return movie_to_watch


def get_movie_list():
    """ Open the movie file and copy to a list of lists"""
    file = open(MOVIE_FILE, "r+")
    file_content = file.readlines()
    file.close()
    movie_list = []
    for line in file_content:
        line = line.strip("\n")
        line = line.split(",")
        movie_list.append(line)
    return movie_list


def get_valid_menu_input():
    """Will ask for a valid response in the menu"""
    print(MENU_STRING)
    menu_input = input(">>> ").upper()
    while menu_input != "D" and menu_input != "A" and menu_input != "W" and menu_input != "Q":
        print("Invalid menu choice")
        menu_input = input(">>> ").upper()
    return menu_input


def add_new_movie():
    """Function will go through the process of adding a new movie to the list and prevent invalid responses"""
    CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
    movie_title = input("Title: ")
    while movie_title == "":
        print("Input can not be blank")
        movie_title = input("Title: ")
    valid_year_input = False
    movie_year = 0
    while not valid_year_input:
        try:
            movie_year = int(input("Year: "))
            if movie_year == "":
                print("Input can not be blank")
            elif movie_year < 1:
                print("Number must be >= 1")
            else:
                valid_year_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
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
