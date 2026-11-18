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

    def __repr__(self):
        """Provide developer-friendly representation of a ProgrammingLanguage."""
        return f"{vars(self)}"

"""Run simple tests/demos on ProgrammingLanguage class."""
# def run_tests():
#     python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
#     ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
#     visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
#
#     print(python)
#     print(repr(python))
#
#     print(ruby)
#     print(repr(ruby))
#
#     print(visual_basic)
#     print(repr(visual_basic))
#
#     # Use assert to ensure correct values are set and method returns correctly
#     assert python.reflection is True
#     assert python.is_dynamic() is True
#     assert python.year == 1991
#     assert ruby.reflection is True
#     assert visual_basic.is_dynamic() is False
#
# run_tests()