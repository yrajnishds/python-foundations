"""
Count ERROR lines in a log file.
"""

count = 0

with open("log.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            count += 1

print("Error count:", count)