"""
Word Occurrences
Estimate: 30 Minutes
Actual: 20 minutes 16 seconds
"""

user_string = input("Type in a random string: ")
word_to_count = {}

words = user_string.split()

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
        #populates the dictionary regardless with default value


for word in sorted(word_to_count.keys()):
    print(f"{word:{len(max(word_to_count, key=len))}}: {word_to_count[word]}")