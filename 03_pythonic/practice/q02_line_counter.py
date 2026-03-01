"""
Count lines in a file.
"""

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Line count:", len(lines))