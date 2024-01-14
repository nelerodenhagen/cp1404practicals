"""
tests unreliable car
"""

from unreliable_car import UnreliableCar


def main():
    my_unreliable_car = UnreliableCar("Hummer", 200, 40)
    print(my_unreliable_car)
    another_unreliable_car = UnreliableCar("Maike", 300, 20)
    another_unreliable_car.drive(18)
    print(f"the fare is: ${another_unreliable_car.get_fare():.2f}")


main()