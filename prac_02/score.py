"""
CP1404/CP5632 - Practical
program to determine score status
"""
def main():
    score = float(input("Enter score: "))
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        elif 90 > score >= 50:
            print("Passable")
        elif score >= 90:
            print("Excellent")
        else:
            print("Bad")

main()