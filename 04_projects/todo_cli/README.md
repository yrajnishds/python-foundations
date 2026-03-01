# 📝 To-Do CLI Application

A modular command-line task management system built using Python.

This project demonstrates:
- Modular programming
- File persistence
- CLI interaction
- Clean program structure


## 🎯 Project Objective

The objective of this project is to build a lightweight command-line task manager that allows users to:

- Add new tasks
- View existing tasks
- Delete tasks
- Persist data between sessions using file handling


## 📂 Project Structure

todo_cli/
│
├── main.py       -> Entry point of application
├── utils.py      -> File handling and helper functions
├── tasks.txt     -> Stores task data (auto-generated)
└── README.md


## ⚙️ How It Works

1. Tasks are stored in a file named:

   tasks.txt

2. Each line in the file represents one task.

Example file content:

Buy groceries
Complete Python practice
Read research paper


3. Program Flow:
   - Loads tasks from file
   - Displays interactive menu
   - Updates file whenever changes occur
   - Runs until user exits


## 🚀 How to Run

Step 1: Navigate to project folder

cd 04_projects/todo_cli

Step 2: Run the program

python main.py


## 📋 Available Options

1. View Tasks
2. Add Task
3. Delete Task
4. Exit


## 🛠 Example Usage

Add Task:

Input:
2
Enter new task: Finish assignment

Output:
Task added successfully.


View Tasks:

1. Finish assignment
2. Read Python documentation


Delete Task:

Enter task number to delete: 1
Removed task: Finish assignment


## 🧠 Concepts Demonstrated

- Modular Design (main.py + utils.py)
- Separation of Concerns
- Persistent Storage
- Basic Error Handling
- Loop-based CLI application


## 🔒 Error Handling

Handles:
- Invalid task number
- Non-numeric input
- Empty task list


## 📈 Future Improvements

- Mark tasks as completed
- Add task priority
- Store tasks in JSON instead of text
- Convert to Object-Oriented Design
- Add unit testing


## 👨‍💻 Author

Rajnish Yadav
Python Learning Journey – Phase 4