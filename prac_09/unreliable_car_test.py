from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar with high and low reliability."""
    # Create cars with different reliabilities (plenty of fuel so it doesn't run out during 100 tests)
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # Attempt to drive both cars 100 times for 1 km each
    for i in range(1, 101):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    # Print final states of the cars to verify overall distances
    print("\nFinal states:")
    print(good_car)
    print(bad_car)


main()
