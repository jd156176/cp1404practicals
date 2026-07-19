"""
CP1404 - Week 6 Practical

Testing guitar class
"""

from prac_06.guitar import Guitar

test_guitar = Guitar("Test", 2000, 350.69)
another_guitar = Guitar("Another Guitar", 1975, 40020.746)

print(f"{test_guitar.name} get_age() - expected: 26. Got: {test_guitar.get_age()}")
print(f"{another_guitar.name} get_age() - expected: 51 Got: {another_guitar.get_age()}")

print(f"{test_guitar.name} is_vintage() expected: False. Got:{test_guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() expected: True. Got:{another_guitar.is_vintage()}")
