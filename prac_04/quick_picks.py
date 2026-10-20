import random

# Global Constants
NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate user-specified number of random lottery quick picks."""
    # Ask the user for the number of quick picks
    try:
        num_picks = int(input("How many quick picks? "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Generate each quick pick line
    for i in range(num_picks):
        quick_pick = []

        # Keep adding random numbers until we have the required amount
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)

            # Ensure there are no duplicate numbers in the current line
            if number not in quick_pick:
                quick_pick.append(number)

        # Sort the quick pick in ascending order
        quick_pick.sort()

        # Print the numbers neatly aligned (width of 2 spaces per number)
        # Using string formatting ensures single digits have a leading space
        output_line = " ".join(f"{num:2}" for num in quick_pick)
        print(output_line)


main()
