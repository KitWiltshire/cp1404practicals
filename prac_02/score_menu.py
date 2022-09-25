def main():
    score = get_valid_score()
    while score != -1:
        """-1 is the number you type in to quit the program"""
        status = determine_score_status(score)
        print(status)
        create_stars(score)
        print()
        score = get_valid_score()


def get_valid_score():
    score = int(input("Enter score: "))
    while score < -1 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_score_status(score):
    if 90 > score >= 50:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


def create_stars(score):
    """produces as many stars as the number of the score"""
    for i in range(0, score, 1):
        print("*", end='')


main()
