import os

# Base folder
base_folder = "02_functions"

# Files inside 02_functions
main_files = [
    "notes.md",
    "basic_functions.py",
    "parameters_and_return.py",
    "default_arguments.py",
    "variable_scope.py",
    "lambda_functions.py",
    "docstrings_example.py",
]

# Practice files
practice_files = [
    "q01_factorial_function.py",
    "q02_prime_function.py",
    "q03_palindrome_function.py",
    "q04_fibonacci_function.py",
    "q05_max_of_three.py",
    "q06_sum_list_function.py",
    "q07_count_vowels_function.py",
    "q08_reverse_string_function.py",
    "q09_temperature_converter.py",
    "q10_simple_calculator.py",
    "q11_even_odd_function.py",
    "q12_area_calculator.py",
    "q13_word_counter.py",
    "q14_remove_duplicates.py",
    "q15_password_validator.py",
]

# Create base folder
os.makedirs(base_folder, exist_ok=True)

# Create main files
for file in main_files:
    open(os.path.join(base_folder, file), "w").close()

# Create practice folder
practice_folder = os.path.join(base_folder, "practice")
os.makedirs(practice_folder, exist_ok=True)

# Create practice files
for file in practice_files:
    open(os.path.join(practice_folder, file), "w").close()

print("✅ 02_functions folder structure created successfully!")