"""
CP1404
collect email and name from user
"""

email = input("Email: ")
email_to_name = {}
while email != "":
    name = (email.split("@")[0]).split(".")
    name = (" ".join(name)).title()
    print(f"Is your name {name}?")
    answer = input("(Y/n) ").upper()
    if answer != "Y" or not answer != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
