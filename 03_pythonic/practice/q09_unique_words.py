"""
Find unique words in a file.
"""

with open("sample.txt", "r") as file:
    words = file.read().split()

unique_words = set(words)

print("Unique words:", unique_words)