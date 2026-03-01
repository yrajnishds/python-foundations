import os

# Base folder
base_folder = "01_basics"

# Files inside 01_basics
main_files = [
    "notes.md",
    "variables.py",
    "data_types.py",
    "operators.py",
    "input_output.py",
    "conditionals.py",
    "loops.py",
]

# Practice files
practice_files = [
    "q01_swap_numbers.py",
    "q02_temperature_convert.py",
    "q03_simple_interest.py",
    "q04_even_or_odd.py",
    "q05_largest_of_three.py",
    "q06_leap_year.py",
    "q07_sum_of_n_numbers.py",
    "q08_factorial.py",
    "q09_multiplication_table.py",
    "q10_reverse_number.py",
    "q11_count_digits.py",
    "q12_palindrome_number.py",
    "q13_armstrong_number.py",
    "q14_prime_check.py",
    "q15_fibonacci_series.py",
    "q16_string_length.py",
    "q17_count_vowels.py",
    "q18_reverse_string.py",
    "q19_palindrome_string.py",
    "q20_remove_spaces.py",
    "q21_list_sum.py",
    "q22_largest_in_list.py",
    "q23_count_occurrences.py",
    "q24_dictionary_basic.py",
    "q25_set_operations.py",
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

print("✅ Folder structure created successfully!")