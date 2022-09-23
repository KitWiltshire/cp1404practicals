x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Even numbers:")
for i in range(x, y+1, 2):
    if x % 2 == 0:
        print(i, end=' ')
    else:
        print(i+1, end=' ')
