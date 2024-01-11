"""
tests Silver Service Taxi
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(my_silver_taxi)
    another_silver_taxi = SilverServiceTaxi("Maike", 300, 2)
    another_silver_taxi.drive(18)
    print(f"the fare is: ${another_silver_taxi.get_fare():.2f}")


main()
