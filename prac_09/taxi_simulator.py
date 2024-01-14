"""
Taxi simulator class
"""


def main():
    from taxi import Taxi
    from silver_service_taxi import SilverServiceTaxi

    MENU = "q)uit, c)hoose taxi, d)rive"

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    current_taxi = None
    choice = get_choice(MENU)
    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            print_taxis(taxis)
            try:
                taxi_index = int(input("Choose taxi: "))
                try:
                    current_taxi = taxis[taxi_index]
                except IndexError:
                    print("Invalid taxi choice")
            except ValueError:
                print("You need to enter a number")

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                print(f"Your {current_taxi.name} cost you {current_taxi.get_fare()}")
                bill_to_date += current_taxi.get_fare()
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date}")
        choice = get_choice(MENU)
    print(f"Total trip costs ${bill_to_date}")
    print("Taxis are now:")
    print_taxis(taxis)


def get_choice(MENU):
    print(MENU)
    choice = input(">>> ").lower()
    return choice


def print_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
