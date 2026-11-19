"""
CP1404 Practical - Read and sort guitars from a CSV file.
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from file, sort by year, and display them."""
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)


def load_guitars(filename):
    """Read guitar data from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars in a formatted list."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
