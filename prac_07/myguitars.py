
from guitar import Guitar

guitars = []

in_file = open('guitars.csv', 'r')


for line in in_file:
    parts = line.strip().split(',')
    guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
    guitars.append(guitar)
in_file.close()

for guitar in guitars:
    print(guitar)

guitars.sort()
print("sorted guitars:")
for guitar in guitars:
    print(guitar)


