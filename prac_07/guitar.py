"""
Cp1404 Week 6 Practical - process guitar data

Estimated Time: 50 Minutes
Actual Time: 36 minutes
"""
import datetime

class Guitar:
    """Represent guitar data as an object"""

    def __init__(self, name="", year=0, cost=0.0):
        """
        Initialize a guitar data set instance

        :param name: string, name of guitar
        :param year: int, year of manufacture
        :param cost: float, cost of manufacture
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Print guitar name, year and cost rounded to two decimal points."""
        return f"{self.name} ({self.year}: ${self.cost:.2f})"

    def __repr__(self):
        """Return string representation of a Guitar object."""
        return str(self)

    def get_age(self):
        """Return integer value of guitar age."""
        return int(datetime.datetime.now().year) - self.year

    def is_vintage(self):
        """Retrun true if age of guitar is 50 or higher."""
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.get_age() < other.get_age()