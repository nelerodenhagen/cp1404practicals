from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013)
print(gibson)

print(f"{gibson.name} get_age() - expected 101. Got {gibson.get_age()}")
print(f"{another.name} get_age() - expected 10. Got {another.get_age()}")

print(f"{gibson.name} is_vintage() - expected True. Got {gibson.is_vintage()}")
print(f"{another.name} is_vintage() - expected False. Got {another.is_vintage()}")
