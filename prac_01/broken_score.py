"""
CP1404/CP5632 - Practical
Broken program to determine score status, Now fixed ;)
"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

