"""Module 4 Lottery Ticket Generator"""
import random

NUMBERS_PER_LINE = 6
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45

def main():
    number_of_lines = int(input("How many quick picks? "))

    for line in range(number_of_lines):
        random_numbers = [random.randint(LOWEST_NUMBER, HIGHEST_NUMBER) for number in range(NUMBERS_PER_LINE)]
        print(" ".join(f"{number:2}" for number in random_numbers))

main()