"""
Cp1404 Week 6 Practical - process programing languages

Estimated Time: 20 Minutes
Actual Time: 16 Minutes 38 Seconds
"""

class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name="", typing="static",reflection=True,year=0):
        """
        Initialize a programming language instance

        :param name: string, name of programming language
        :param typing: string, programming typing mode, either static or dynamic
        :param reflection: boolean
        :param year: int, year of programming language conception
        """
        self.name = name
        self.typing = typing
        self.reflection =  reflection
        self.year = year

    def is_dynamic(self):
        """Return true if program is dynamically typed, false if program is static."""
        return self.typing.upper() == "DYNAMIC"

    def __str__(self):
        """Print the program name, typing method, reflection status and language conception year."""
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"
