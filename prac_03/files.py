"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

OUTPUT_FILE = "name.txt"
INPUT_FILE_NUMBERS = "numbers.txt"

input_name = input("Please enter your name: ")
output_file = open(OUTPUT_FILE, 'w')
print(input_name, file=output_file)
output_file.close()

in_file = open(OUTPUT_FILE, 'r')
read_name = in_file.read()
print(f"Your name is {read_name}")
in_file.close()

in_file_numbers = open(INPUT_FILE_NUMBERS, 'r')
a = int(in_file_numbers.readline())
b = int(in_file_numbers.readline())
print(a+b)

in_file_numbers = open(INPUT_FILE_NUMBERS, 'r')
sum_lines = 0
for line in in_file_numbers:
    sum_lines += int(line)
in_file_numbers = open(INPUT_FILE_NUMBERS, 'a')
in_file_numbers.write(str(sum_lines))
