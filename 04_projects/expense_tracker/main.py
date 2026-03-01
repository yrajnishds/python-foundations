from utils import load_expenses, save_expenses


def show_menu():
    print("\n--- EXPENSE TRACKER ---")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Show Total")
    print("4. Exit")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            if not expenses:
                print("No expenses recorded.")
            else:
                for i, (name, amount) in enumerate(expenses, start=1):
                    print(f"{i}. {name} - ₹{amount}")

        elif choice == "2":
            name = input("Expense name: ")
            try:
                amount = float(input("Amount: "))
                expenses.append((name, amount))
                save_expenses(expenses)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid amount.")

        elif choice == "3":
            total = sum(amount for _, amount in expenses)
            print(f"Total Spending: ₹{total}")

        elif choice == "4":
            print("Exiting application.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()