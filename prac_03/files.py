# 1
name = input("Enter name: ")
out_file = open('name.txt', 'w')
print(f"{name}", file=out_file)
out_file.close()


# 2
with open('name.txt', 'r') as out_file:
    name = out_file.read()
print(f"Your name is {name}")
out_file.close()

# 3

total = 0
line_number = 0
out_file = open('numbers.txt', 'r')
for line in out_file:
    if line_number < 2:
        line_number += 1
        total += int(line)
print(total)

# 4

total = 0
line_number = 0
out_file = open('numbers.txt', 'r')
for line in out_file:
    line_number += 1
    total += int(line)
print(total)
