MINIMUM_PASSWORD_LENGTH = 10

password = input("Type in your password: ")
while len(password) < 10:
    print("Your password is too short. Please try again.")
    password = input("Type in your password: ")
for i in password:
    print("*", end='')
