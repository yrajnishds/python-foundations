def is_palindrome(text):
    return text == text[::-1]

text = input("Enter string: ")
print("Palindrome:", is_palindrome(text))