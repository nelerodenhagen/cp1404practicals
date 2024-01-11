"""
CP1404 Practical
count the occurrence of words in a text
Estimate: 20 Minutes
Actual: 17 Minutes
"""


text = input("Please insert a text: ")
words = text.split()

word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_length = max([len(word) for word in word_to_count.keys()])

for word, count in sorted(word_to_count.items()):
    print(f"{word:{max_length}} : {count:1}")
