import os

# Base folder
base_folder = "04_projects"

# Project structure dictionary
structure = {
    "todo_cli": [
        "main.py",
        "utils.py",
        "tasks.txt",
        "README.md",
    ],
    "expense_tracker": [
        "main.py",
        "utils.py",
        "expenses.txt",
        "README.md",
    ]
}

# Create base folder
os.makedirs(base_folder, exist_ok=True)

# Create project folders and files
for project, files in structure.items():
    project_path = os.path.join(base_folder, project)
    os.makedirs(project_path, exist_ok=True)

    for file in files:
        file_path = os.path.join(project_path, file)
        open(file_path, "w").close()

print("✅ 04_projects folder structure created successfully!")