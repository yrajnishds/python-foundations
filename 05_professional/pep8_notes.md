# 📏 PEP8 Style Guide (Important Rules)

1. Use 4 spaces for indentation
2. Function names → lowercase_with_underscores
3. Class names → CapitalizedWords
4. Line length ≤ 79 characters
5. Two blank lines before top-level functions
6. One blank line between methods

Bad Example:

def Add(a,b):return a+b

Good Example:

def add(a, b):
    return a + b

Use formatter:

pip install black
black filename.py