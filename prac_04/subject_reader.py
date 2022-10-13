"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject_data(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        subject_data.append(parts)
    input_file.close()
    return subject_data

def display_subject_data(data):
    for subject in range(0, len(data)):
        # print(f"{data[subject]:<} is taught by {data[subject + 1]:<12} and has {data[subject + 2]:>3} students")
        print(f"{data[subject][0]} is taught by {data[subject][1]:<12} and has {data[subject][2]:>3} students")

main()