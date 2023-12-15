"""
CP1404/CP5632 - Practical
program to determine score status
"""
import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    score = float(input("Enter score: "))
    print_grade(score)
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print_grade(random_score)


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
