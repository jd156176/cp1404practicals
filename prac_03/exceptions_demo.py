"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
except ValueError:
    print("Numerator and denominator must be valid numbers!")
else:
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
print("Finished.")

#1. A ValueError will occur whenever the user inputs anything that isn't a integer value. This includes floating
#point values, letters or symbols.

#2. A ZeroDivisionError will occur if the denominator inputted by the user is equal to zero. This is because
# mathematically, dividing any number by zero is undefined. Zero can be inputted as the numerator, as zero divided
# by any number remains as zero.

#3. To avoid the possibility of a ZeroDivisionError occurring all together, the try/except block could be adjusted so
# that there is an else statement which then uses an if statement to test if the input is equal to zero. The executable
# code then can be placed within this block.