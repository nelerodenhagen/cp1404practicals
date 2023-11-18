"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit\n F - Convert Fahrenheit to Celsius\n Q - Quit"""
CONVERTER = 32


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_celsius_to_fahreneheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - CONVERTER)
    return celsius


def calculate_celsius_to_fahreneheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + CONVERTER
    return fahrenheit


main()
