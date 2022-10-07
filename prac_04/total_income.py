def main():
    monthly_incomes = get_monthly_incomes()
    print_monthly_income_report(monthly_incomes)


def print_monthly_income_report(monthly_incomes):
    print("Income Report")
    print("-------------")
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(0, len(monthly_incomes)):
        income = monthly_incomes[month]
        total += income
        print(f"Month {month + 1:2} - Income: ${income:10.2f}         Total: ${total:10.2f}")


def get_monthly_incomes():
    monthly_incomes = []
    number_of_monthly_incomes = int(input("How many months?: "))
    for month in range(0, number_of_monthly_incomes):
        monthly_income = float(input(f"Enter income for month {month + 1}: "))
        monthly_incomes.append(monthly_income)
    return monthly_incomes


main()
