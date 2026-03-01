"""
Read CSV file manually (basic).
"""

with open("data.csv", "r") as file:
    for line in file:
        values = line.strip().split(",")
        print(values)