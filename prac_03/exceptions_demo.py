"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("denominator can't be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Answers to the tasks:
1. When will a ValueError occur?
A ValueError will occur when either numerator or denominator is a non-integer (for example a float)

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the denominator is 0. 

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, I could test if the denominator is 0 when it is entered. 
"""