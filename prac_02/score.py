"""
CP1404/CP5632 - Practical
program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    status = determine_score_status(score)
    print(status)
    score = random.randint(0, 100)
    status = determine_score_status(score)
    print(status)


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif 90 > score >= 50:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


main()
