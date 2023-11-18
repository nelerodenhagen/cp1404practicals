"""
CP1404/CP5632 - Practical
program with menu for score
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    print(MENU)
    choice = input("Please type in your choice: ")
    score = -1
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            if score == -1:
                print("Please enter first a valid score")
            else:
                print_grade(score)
        elif choice == "S":
            if score == -1:
                print("Please enter first a valid score")
            else:
                print("*" * score)
        else:
            print("You entered an invalid choice. Please try again")
        choice = input("Please type in your choice: ")
    print("farewell")


def get_score():
    """
    function gets valid score from user input
    """
    score = int(input("Please enter the score: "))
    while score < 0 or score > 100:
        print("You entered an invalid score. Please try again.")
        score = int(input("Please enter the score: "))
    return score


def print_grade(score):
    """
    first determines and then prints score and grade
    """
    print(f"With the score {score} you reached: ", determine_grade(score))


def determine_grade(score):
    """
    determines the grade for a given score
    """
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASS_THRESHOLD:
        return "Pass"
    else:
        return "Bad"


main()
