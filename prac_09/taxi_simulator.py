from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run a taxi simulator program using Taxi and SilverServiceTaxi classes."""
    total_bill = 0.0
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis, current_taxi)
        elif menu_choice == "d":
            if current_taxi:
                trip_cost = drive_taxi(current_taxi)
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display a numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis, current_taxi):
    """Prompt user to choose a valid taxi from the list."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return current_taxi


def drive_taxi(taxi):
    """Start a new fare, drive the chosen taxi, and return the trip cost."""
    taxi.start_fare()
    distance_to_drive = float(input("Drive how far? "))
    taxi.drive(distance_to_drive)
    return taxi.get_fare()


if __name__ == "__main__":
    main()
