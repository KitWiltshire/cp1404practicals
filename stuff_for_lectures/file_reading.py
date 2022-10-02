# """File reading"""
#
# total = 0
# line_number = 0
# error_line_numbers = []
# filename = input("Filename: ")
# in_file = open(filename, "r")
# # for line in in_file:
# #     if line[0] == "a":
# #         print(repr(line))
# #         print(line.strip())
# # for line in in_file:
# #     if line.startswith("a"):
# #         print(repr(line))
# #         print(line.strip())
# for line in in_file:
#     line_number += 1
#     try:
#         total += float(line)
#         print(line)
#     except ValueError:
#         print(f"error on line {line_number}")
#         error_line_numbers += 1
#
#
# print(total, line_number, error_line_numbers)
# in_file.close()

# s = "\tPython, Monty  \n"
# print(s[1], ".", sep="")
# print(s.strip(), ".", sep="")
# s.replace(' ', '*')
# print(s.lstrip(), ".", sep="")
# print(s.strip().split(','))
#
# name = input("Name: ")
# out_file = open("minecraft.txt", "w")
# print(name, file=out_file)
# out_file.close()

# file_name = ["Epic", "Bonkers", "Diabolical"]
# # out_file = str(open(file_name, "w"))
# # file_name = input("Name: ")
# # if file_name == "bob":
# with open("bob.txt", "w") as out_file:
#     print(file_name, file=out_file)


strings = ["a", "b", "c"]
for string in strings:
    with open(f"stuff_for_lectures/{string}.txt", "w") as out_file:
        print(string, file=out_file)
    print(":)")



