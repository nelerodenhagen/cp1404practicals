import random


def main():
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        line = []
        for j in range(6):
            new_number = random.randint(1, 46)
            line.append(new_number)
        print(f"{" ".join([str(number) for number in line])}")


main()
