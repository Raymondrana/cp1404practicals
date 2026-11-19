"""
CP1404 Practical - Read and sort guitars from a CSV file.
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from file, add new ones, sort, display, and save."""
    guitars = load_guitars(FILENAME)
    print("Loaded guitars:")
    display_guitars(guitars)

    add_new_guitars(guitars)

    guitars.sort()
    print("\nSorted guitars (oldest to newest):")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\n{len(guitars)} guitars saved to {FILENAME}.")


def save_guitars(filename, guitars):
    """Write all Guitar objects to the specified CSV file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def add_new_guitars(guitars):
    """Prompt the user to enter new guitars and append them to the list."""
    print("\nEnter your new guitars (leave name blank to finish):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")


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
