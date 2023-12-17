from guitar import Guitar

print("My guitars!")
my_guitars = []
name = input("Name: ")

while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    my_guitars.append(Guitar(name, year, cost))
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(my_guitars, 1):
    vintage_string = "vintage" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:.2f} {vintage_string}")
