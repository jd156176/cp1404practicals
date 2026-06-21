"""Module 4 Lottery Ticket Generator"""
import random

def main():
    NUMBERS_PER_LINE = 6
    LOWEST_NUMBER = 1
    HIGHEST_NUMBER = 45
    number_of_lines = int(input("How many quick picks? "))

    quick_pick = []
    for number