"""
Question:
Find length of a string without using len().
"""

text = input("Enter string: ")
count = 0

for _ in text:
    count += 1

print("Length:", count)