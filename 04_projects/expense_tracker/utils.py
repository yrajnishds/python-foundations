EXPENSE_FILE = "expenses.txt"


def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            expenses = []
            for line in file:
                name, amount = line.strip().split(",")
                expenses.append((name, float(amount)))
            return expenses
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        for name, amount in expenses:
            file.write(f"{name},{amount}\n")