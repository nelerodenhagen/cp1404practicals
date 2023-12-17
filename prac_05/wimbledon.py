FILENAME = "wimbledon.csv"


def main():
    in_file = open(FILENAME)
    lines = in_file.readlines()[1:]

    facts = generate_list(lines)

    winner_countries, winners_to_count = calculate_winners_with_count_and_countries(facts)

    print_winners_and_countries(winner_countries, winners_to_count)


def generate_list(lines):
    facts = []
    for line in lines:
        facts.append((str(line).strip()).split(","))
    return facts


def calculate_winners_with_count_and_countries(facts):
    winners_to_count = {}
    winner_countries = set()
    for fact in facts:
        print(fact[3])
        winner_countries.add(fact[3])
        if fact[2] in winners_to_count:
            winners_to_count[fact[2]] += 1
        else:
            winners_to_count[fact[2]] = 1
    return winner_countries, winners_to_count


def print_winners_and_countries(winner_countries, winners_to_count):
    print("Wimbledon Champions:")
    for winner, count in winners_to_count.items():
        print(f"{winner} {count}")
    print(f"These {len(winner_countries)} countries have won Wimbledon:")
    print(", ".join(winner_countries))


main()
