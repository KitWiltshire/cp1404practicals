import random


def main():
    OUTPUT_FILE = 'minecraft'
    INITIAL_PRICE = 10
    GOOD_ROLL = 0.175  # when a good day occurs it will increase between 0 and 17.5% of the price's value
    BAD_ROLL = -0.05  # when a bad day occurs it will decrease between 0 and 5% of the price's value
    MAXIMUM_PRICE_CAP = 1000
    MINIMUM_PRICE_CAP = 0.01
    MINIMUM_ALLOWED_PRICE = 1
    MAXIMUM_ALLOWED_PRICE = 100
    number_of_days = 0
    current_price = INITIAL_PRICE
    print(f"Starting price: ${INITIAL_PRICE:.2f}")
    out_file = open(OUTPUT_FILE, 'w')
    while MINIMUM_PRICE_CAP < current_price < MAXIMUM_PRICE_CAP:
        number_of_days += 1
        day_luck = random.randint(0, 1)
        if day_luck == 0:
            price_luck = random.uniform(0, GOOD_ROLL)
            money_gained = price_luck * current_price
            if money_gained < MINIMUM_ALLOWED_PRICE:
                money_gained = MINIMUM_ALLOWED_PRICE
            elif money_gained > MAXIMUM_ALLOWED_PRICE:
                money_gained = MAXIMUM_ALLOWED_PRICE
        else:
            price_luck = random.uniform(BAD_ROLL, 0)
            money_gained = price_luck * current_price
            if money_gained > -MINIMUM_ALLOWED_PRICE:
                money_gained = -MINIMUM_ALLOWED_PRICE
            elif money_gained < -MAXIMUM_ALLOWED_PRICE:
                money_gained = -MAXIMUM_ALLOWED_PRICE
        current_price += money_gained
        print(f"On day {number_of_days} price is: ${current_price:.2f}")
        print(f"${current_price:,.2f}", file=out_file)
    out_file.close()


main()
