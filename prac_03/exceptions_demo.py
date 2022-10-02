"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    while denominator == 0:
        try:
            denominator = int(input("Enter the denominator: "))
            fraction = numerator / denominator
        except ValueError:
            print("Numerator and denominator must be valid numbers!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
    print(fraction)
print("Finished.")

# ValueError occurs when the numerator or denominator are not numbers
# ZeroDivisionError occurs when the numerator is zero
# Make the user input the denominator again until it is a number that isn't zero