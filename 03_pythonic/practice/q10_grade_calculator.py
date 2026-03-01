"""
Calculate grade from marks stored in file.
Each line contains a mark.
"""

with open("marks.txt", "r") as file:
    marks = [int(line.strip()) for line in file]

average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("Average:", average)
print("Grade:", grade)