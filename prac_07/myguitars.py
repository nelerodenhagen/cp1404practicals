"""
CP1404 Practical
opens/reads a file, stores in objects of Guitar class
sorts them and possible to add new ones
"""
from guitar import Guitar

guitars = []

in_file = open('guitars.csv', 'r')


for line in in_file:
    parts = line.strip().split(',')
    guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
    guitars.append(guitar)
in_file.close()

print("these are my current guitars:")
for guitar in guitars:
    print(guitar)

guitars.sort()
print("sorted guitars:")
for guitar in guitars:
    print(guitar)

print("now you can enter new guitars:")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(Guitar(name, year, cost))
    name = input("Name: ")

in_file = open('guitars.csv', 'w')
for guitar in guitars:
    in_file.write(f"{guitar.name},{str(guitar.year)},{str(guitar.cost)}\n")

