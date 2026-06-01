"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    print(f"User score {score} is {class_result(score)}")

    if score == 100:
        print("You Get a Prize!")

    random_score = random.randint(0,100)
    print(f"Random: {random_score} is {class_result(random_score)}")

def class_result(score: float):
    """Class result based on score threshold."""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()