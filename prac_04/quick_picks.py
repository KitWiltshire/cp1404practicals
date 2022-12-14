import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
number_of_quick_picks = int(input("How many quick picks? "))
for number in range(0, number_of_quick_picks):
    quick_picks = []
    for i in range(0, 6):
        quick_pick = f"{random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER):2}"
        while quick_pick in quick_picks:
            quick_pick = f"{random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER):2}"
        quick_picks.append(quick_pick)
        quick_picks.sort()
    quick_picks_string = " ".join(map(str, quick_picks))
    print(f"{quick_picks_string}")
