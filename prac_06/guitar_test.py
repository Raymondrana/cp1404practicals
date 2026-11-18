"""
CP1404 Practical - Guitar Class Tests
Estimate: 15 minutes
Actual:   8 minutes
"""

from guitar import Guitar

CURRENT_YEAR = 2026


def run_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 1512.9)
    fifty_year_guitar = Guitar("50-year old guitar", CURRENT_YEAR - 50, 1000)

    print(f"{guitar.name} get_age() - Expected {104}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {13}. Got {other.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")
    print(
        f"{fifty_year_guitar.name} is_vintage() - Expected {True}. Got {fifty_year_guitar.is_vintage()}"
    )


run_tests()
