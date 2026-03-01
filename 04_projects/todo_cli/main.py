from utils import load_tasks, save_tasks


def show_menu():
    print("\n--- TO-DO MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            if not tasks:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully.")

        elif choice == "3":
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter task number to delete: ")) - 1
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Removed task: {removed}")
            except (IndexError, ValueError):
                print("Invalid selection.")

        elif choice == "4":
            print("Exiting application.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()