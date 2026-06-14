def main():
    file_name = input("Enter Filename: ")
    while file_name != "":
        try:
            print(f"{file_name} has {count_lines(file_name)} lines")
        except FileNotFoundError:
            print(f"ERROR: {file_name} does not exist.")

        file_name = input("Enter Filename: ")

def count_lines(file_name):
    number_of_lines = 0
    with open(file_name, "r") as file:
        for line in file:
            number_of_lines += 1
    return number_of_lines

main()