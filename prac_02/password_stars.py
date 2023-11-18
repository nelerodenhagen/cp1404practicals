MINIMUM_PASSWORD_LENGTH = 10


def main():
    password = get_password()
    transform_password_to_asterisks(password)


def transform_password_to_asterisks(password):
    for i in password:
        print("*", end='')


def get_password():
    password = input("Type in your password: ")
    while len(password) < 10:
        print("Your password is too short. Please try again.")
        password = input("Type in your password: ")
    return password


main()
