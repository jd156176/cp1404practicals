"""Prac 07 More Guitars exercise"""

import csv
from typing import Any

from guitar import Guitar

def main():
    guitars = read_file()
    get_guitar(guitars)
    guitars.sort()
    print(guitars)
    write_file(guitars)


def get_guitar(guitars: list[Guitar]):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{name} ({year}) : {cost} added.")
        name = input("Name: ")


def read_file() -> list[Guitar]:
    guitars = []  # note to self: to print the list directly, need __repr__
    with open('guitars.csv', 'r', newline="") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for name, year, cost in reader:
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def write_file(guitars: list[Guitar]) -> None:
    with open('guitars.csv', 'w', newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Name", "Year", "Cost"])
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

main()