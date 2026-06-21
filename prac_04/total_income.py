"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
from typing import Any


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    print_report(incomes, number_of_months)


def print_report(incomes):
    """Print report based on incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {str(month)} - Income: {income:8.2f} Total: {total:8.2f}")


main()