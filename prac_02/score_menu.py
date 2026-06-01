"""
Week 2 - Score menu utilising functions
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def  main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ")
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Your score: {score} is {class_result(score)}")
        elif choice == "S":
            print_symbol("*", score)
            print()
        else:
            print("Invalid Choice.")
        print(MENU)
        choice = input(">>> ")
    print("Goodbye.")

def get_valid_score():
    """Validate if score is between 0 and 100"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid Score.")
        score = int(input("Score: "))
    return score

def class_result(score: float):
    """Class result based on score threshold."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_symbol(symbol: str, length: int):
    """Prints line of symbols equal to specified length."""
    for i in range (length):
        print(symbol, end="")


main()