"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {convert_to_fahrenheit(celsius):.2f}")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            print(f"Result: {convert_to_celsius(fahrenheit):.2f}")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_celsius(fahrenheit: float):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_to_fahrenheit(celsius: float):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()