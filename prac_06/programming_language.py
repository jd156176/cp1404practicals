"""Cp1404 Week 6 Practical - process programing languages

Estimated Time: 20 Minutes
Actual Time: 16 Minutes 38 Seconds
"""

class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name="", typing="static",reflection=True,year=0):
        self.name = name
        self.typing = typing
        self.reflection =  reflection
        self.year = year

    def is_dynamic(self):
        return self.reflection

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"
