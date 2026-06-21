"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subject_data = load_data(FILENAME)
    for subject, lecturer, number_of_students in subject_data:
        print(f"{subject} is taught by {lecturer} and has {number_of_students} students")


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    all_subject_data = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        subject_data = [parts[0], parts[1], int(parts[2])]
        all_subject_data.append(subject_data)
        print(subject_data)  # See if that worked
        print("----------")
    input_file.close()

    return all_subject_data


main()