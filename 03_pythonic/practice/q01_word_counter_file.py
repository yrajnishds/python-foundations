"""
Count number of words in a file.
"""

with open("sample.txt", "r") as file:
    text = file.read()
    words = text.split()

print("Word count:", len(words))