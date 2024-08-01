from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    print("Let's drive!")
    print(MENU)
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif user_choice == "d":
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
        user_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """display all taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_taxi):
    current_taxi.start_fare()
    drive_distance = float(input("Drive how far? "))
    current_taxi.drive(drive_distance)
    trip_cost = current_taxi.get_fare()
    return trip_cost

main()
