"""
CP1404/CP5632 - Practical
!!
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = input("Please type in your choice: ")
    score = 1
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print_grade(score)
        elif choice == "S":
            print("*"*score)
        else:
            print("You entered an invalid choice. Please try again")
        choice = input("Please type in your choice: ")
    print("farewell")


def get_score():
    score = int(input("Please enter the score: "))
    while score < 0 or score > 100:
        print("You entered an invalid score. Please try again.")
        score = int(input("Please enter the score: "))
    return score


def print_grade(score):
    print(f"With the score {score} you reached: ", calculate_grade(score))


def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
