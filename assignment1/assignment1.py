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
    """This function will be in charge of the whole program with other functions inside that do the complex
    things """
    print("Movies To Watch 1.0 - by Kit Wiltshire")
    # Read Content
    movie_list = get_movie_list()
    movie_list.sort(key=lambda year: year[1])  # Sort the list by movie
    menu_input = get_valid_menu_input()
    while menu_input != "Q":
        # movie_list.sort(key=lambda year: year[1])  # Sort the list by movie
        if menu_input == "D":
            for index, movie in enumerate(movie_list):
                if movie[WATCHED_INDEX] == NOT_WATCHED:
                    print(f"{index + 1}. * {movie[TITLE_INDEX]} - {movie[YEAR_INDEX]} ({movie[GENRE_INDEX]})")
                else:
                    print(f"{index + 1}.   {movie[TITLE_INDEX]} - {movie[YEAR_INDEX]} ({movie[GENRE_INDEX]})")
            # TODO: count the movies watched and movies unwatched and print it out

        elif menu_input == "A":
            new_movie = add_new_movie()
            print(new_movie)
            # new_movie = [new_movie]
            new_movie = new_movie.split(",")
            print(new_movie)
            print(movie_list)
            new_movie[YEAR_INDEX] = int(new_movie[YEAR_INDEX])
            movie_list.append(new_movie)
            movie_list.sort(key=lambda year: year[1])
            print(movie_list)
            # movie_list.seek(0)
            # movies_content = movie_list.read()
        else:  # when the user presses "w"
            print("Enter the number of a movie to mark as watched")
            try:
                movie_to_watch = int(input(">>> "))
                while movie_to_watch != int and movie_to_watch < 1:
                    if movie_to_watch == "":
                        print("Input can not be blank")
                    elif movie_to_watch < 1:
                        print("Number must be >= 1")
            except IndexError:
                print("Invalid movie number")
                movie_to_watch = int(input(">>> "))
            except ValueError:
                print("Invalid input; enter a valid number")
                movie_to_watch = input(">>> ")
            if movie_list[movie_to_watch - 1][3] == "w":
                print(f"{movie_list[movie_to_watch - 1][0]} from {movie_list[movie_to_watch - 1][1]} watched")
            else:
                print("bruh")
                movie_list[movie_to_watch - 1][3] = "w"
                print(movie_list[movie_to_watch - 1])
                print(movie_list)
                # file.seek(0)
                # movies_file.truncate(0)
                # for movie in movie_list:
                #     movies_file.write(f"{movie[0]},{movie[1]},{movie[2]},{movie[3]}\n")

            # TODO: do an if statement for when a movie has already been watched and also turn a movie that hasn't been watched into a watched one
        menu_input = get_valid_menu_input()
    print("Have a nice day :)")
    # movies_file, movie_list = update_movies(movies_content, movies_file)
    # movies_file.close()


def get_movie_list():
    """ Open the movie file and copy to a list of lists"""
    backup_file = open("movies_backup.csv", 'r')
    backup_file_content = backup_file.read()
    file = open(MOVIE_FILE, "r+")
    file_content = file.readlines()
    print(file_content)
    file.close()

    movie_list = []
    for line in file_content:
        line = line.strip("\n")
        # print(line)
        line = line.split(",")
        # print(line)
        line[YEAR_INDEX] = int(line[YEAR_INDEX])
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
    valid_year_input = False
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
    # valid_year_input = False
    # while not valid_year_input:
    #     try:
    #         movie_year = int(input("Year: "))
    #         valid_year_input = True
    #         if movie_year < 1:
    #             print("Number must be >= 1")
    #             valid_year_input = False
    #     except ValueError:
    #         print("Invalid input; enter a valid number")
    #     except None:
    #         print("Input can not be blank")

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

