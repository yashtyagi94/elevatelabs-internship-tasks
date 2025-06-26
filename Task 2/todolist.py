# todo.py

TASK_FILE = 'tasks.txt'


def load_tasks():
    """Load tasks from the file into a list."""
    try:
        with open(TASK_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save the current list of tasks to the file."""
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def show_tasks(tasks):
    """Display all current tasks."""
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print()


def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Task added: {task}")
    else:
        print("❌ Task cannot be empty.")


def remove_task(tasks):
    """Remove a task by its number."""
    show_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"🗑️ Task removed: {removed}")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")


def main():
    print("=== 📋 To-Do List Manager ===")
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1-4.")


if __name__ == '__main__':
    main()