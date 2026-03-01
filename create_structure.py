import os

# Base folder
base_folder = "03_pythonic"

# Files inside 03_pythonic
main_files = [
    "notes.md",
    "list_comprehensions.py",
    "dictionary_comprehensions.py",
    "file_reading.py",
    "file_writing.py",
    "file_append.py",
    "exception_handling.py",
    "json_handling.py",
]

# Practice files
practice_files = [
    "q01_word_counter_file.py",
    "q02_line_counter.py",
    "q03_copy_file.py",
    "q04_csv_reader_basic.py",
    "q05_log_parser.py",
    "q06_safe_division.py",
    "q07_json_reader.py",
    "q08_json_writer.py",
    "q09_unique_words.py",
    "q10_grade_calculator.py",
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

print("✅ 03_pythonic folder structure created successfully!")