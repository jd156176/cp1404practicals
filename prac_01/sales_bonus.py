"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter Sales: $"))

while sales >= 0:
    if sales >= 1000:
        interest = 0.15
    else:
        interest = 0.10
    bonus = sales * interest
    print(f"Expected Bonus is {bonus:.2f}")
    sales = float(input("Enter Sales: $"))
