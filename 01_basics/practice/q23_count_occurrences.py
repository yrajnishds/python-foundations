"""
Question:
Count occurrences of an element in a list.
"""

numbers = [1, 2, 2, 3, 4, 2, 5]

element = int(input("Enter element to count: "))

count = 0
for num in numbers:
    if num == element:
        count += 1

print("Occurrences:", count)