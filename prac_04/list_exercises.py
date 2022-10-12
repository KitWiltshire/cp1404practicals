numbers = []
total = 0
SIZE_OF_LIST = 5
for i in range(0, SIZE_OF_LIST):
    number = int(input("Number: "))
    numbers.append(number)
    total += number
average = total / SIZE_OF_LIST
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average}")
