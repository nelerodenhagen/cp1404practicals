"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(f"With the score {score} you reached: ", calculate_grade(score))
    random_score = random.randint(1, 100)
    print(f"With the score {random_score} you reached: ", calculate_grade(random_score))


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
