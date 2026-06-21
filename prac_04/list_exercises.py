"""Week 4 List exercise program"""
from typing import Any


def main():
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)
    print_number_information(numbers)

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Please type username: ")
    check_username(username, usernames)


def print_number_information(numbers: list[Any]):
    """Gathers number information such as first and last numbers, smallest and largest numbers and average.
    Prints for the user."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {(sum(numbers) / len(numbers)):.2f}")


def check_username(username: str, usernames: list[Any]):
    "Checks if inputted username matches from list."
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()