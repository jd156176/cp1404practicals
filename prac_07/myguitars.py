"""Prac 07 More Guitars exercise"""

import csv
from guitar import Guitar

def main():
    guitars = [] #note to self: to print the list directly, need __repr__
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    #file format: Name,Year,Cost

    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), parts[2])
        print(guitar)
        guitars.append(guitar)

    guitars.sort()
    print(guitars)

main()