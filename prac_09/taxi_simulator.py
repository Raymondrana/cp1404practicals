from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run a taxi simulator with distance tracking and input validation."""
    total_bill = 0.0
    total_distance = 0.0
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
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance_driven, trip_cost = drive_taxi(current_taxi)
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f} "
                      f"for {distance_driven:.1f}km")
                total_bill += trip_cost
                total_distance += distance_driven
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f} | Total distance: {total_distance:.1f}km")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f} for {total_distance:.1f}km driven")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display a numbered list of taxis with their costs."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis, current_taxi):
    """Prompt user to choose a valid taxi index with error checking."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return current_taxi


def drive_taxi(taxi):
    """Start a new fare, drive the taxi, and return (actual_distance, trip_cost)."""
    taxi.start_fare()
    distance_to_drive = get_valid_distance()
    actual_distance = taxi.drive(distance_to_drive)
    return actual_distance, taxi.get_fare()


def get_valid_distance():
    """Get a non-negative numeric distance from the user."""
    while True:
        try:
            distance = float(input("Drive how far? "))
            if distance >= 0:
                return distance
            print("Distance must be >= 0")
        except ValueError:
            print("Invalid distance")


if __name__ == "__main__":
    main()
