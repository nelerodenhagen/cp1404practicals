"""
CP1404/CP5632 - Practical
program that transforms a password to asterisks
"""

MINIMUM_PASSWORD_LENGTH = 10


def main():
    password = get_password()
    transform_password_to_asterisks(password)


def transform_password_to_asterisks(password):
    """
    prints for every letter in password an asterisk
    """
    for i in password:
        print("*", end='')


def get_password():
    """
    gets a valid password
    """
    password = input("Type in your password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Your password is too short. Please try again.")
        password = input("Type in your password: ")
    return password


main()
