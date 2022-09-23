TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")
cents_per_kwh = int(input("Enter cents per kWh: ")) * 0.01
daily_kwh_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
bill = cents_per_kwh * daily_kwh_use * billing_days
print(f"Estimated bill: ${bill:.2f}")

print("Electricity bill estimator 2.0")
tariff_choice = input("Which tariff? 11 or 31: ")
if tariff_choice == "11":
    tariff = TARIFF_11
else:
    tariff = TARIFF_31
daily_kwh_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
bill = cents_per_kwh * daily_kwh_use * billing_days * tariff
print(f"Estimated bill: ${bill:.2f}")