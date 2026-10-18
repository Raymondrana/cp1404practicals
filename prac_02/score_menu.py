"""
Score Menu Program
"""

menu = "[G]et Score  |  [P]rint Result  |  [S]how Stars  |  [Q]uit"

def main():
    print("Welcome to the Score Manager!")
    score = get_valid_score()

    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result for score {score}: {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice. Please select from the menu.")

        print(menu)
        choice = input(">>> ").upper()

    print("Farewell!")


def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score))


main()
