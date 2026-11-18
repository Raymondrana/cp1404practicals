"""
ProgrammingLanguage class definition.
Estimate: 30 minutes
Actual time: 42 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language with its core attributes."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, otherwise False."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a formatted string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
