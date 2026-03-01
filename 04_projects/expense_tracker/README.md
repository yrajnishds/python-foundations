# 💰 Expense Tracker CLI Application

A command-line expense management tool built using Python.

This project demonstrates:
- File-based data persistence
- Data parsing
- Modular programming
- Input validation


## 🎯 Project Objective

The goal of this project is to build a basic expense tracking system that allows users to:

- Add new expenses
- View recorded expenses
- Calculate total spending
- Persist expense data between sessions


## 📂 Project Structure

expense_tracker/
│
├── main.py        -> Main CLI application
├── utils.py       -> File operations and helper functions
├── expenses.txt   -> Stores expense records (auto-generated)
└── README.md


## ⚙️ How It Works

1. Expenses are stored in:

   expenses.txt

2. Each line follows this format:

   ExpenseName,Amount

Example:

Groceries,1500
Transport,300
Internet,800


3. Program Flow:
   - Load existing expenses
   - Display interactive menu
   - Append new expenses
   - Calculate totals dynamically
   - Save changes automatically


## 🚀 How to Run

Step 1: Navigate to project folder

cd 04_projects/expense_tracker

Step 2: Run the program

python main.py


## 📋 Available Options

1. View Expenses
2. Add Expense
3. Show Total
4. Exit


## 🛠 Example Usage

Add Expense:

Input:
2
Expense name: Books
Amount: 1200

Output:
Expense added successfully.


View Expenses:

1. Books - ₹1200
2. Internet - ₹800


Show Total:

Total Spending: ₹2000


## 🧠 Concepts Demonstrated

- File reading & writing
- String parsing using split()
- Float conversion
- Generator expressions
- Basic financial calculation


## 🔒 Error Handling

Handles:
- Invalid numeric input
- Missing expense file
- Empty expense list


## 📈 Future Improvements

- Categorize expenses
- Monthly summary report
- Export to CSV
- Use JSON storage
- Convert to Object-Oriented Design
- Add graphical interface


## 👨‍💻 Author

Rajnish Yadav
Python Learning Journey – Phase 4