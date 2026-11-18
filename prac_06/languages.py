"""
Client code to test the ProgrammingLanguage class.
Estimate: 30 minutes
Actual time: 42 minutes
"""

from prac_06.programming_language  import ProgrammingLanguage


def main():
    """Create ProgrammingLanguage objects and filter dynamically typed ones."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()
