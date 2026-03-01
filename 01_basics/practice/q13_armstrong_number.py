"""
Question:
Check if number is Armstrong number.
Example: 153 = 1³ + 5³ + 3³
"""

num = int(input("Enter number: "))
original = num
result = 0

while num > 0:
    digit = num % 10
    result += digit ** 3
    num //= 10

if original == result:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")