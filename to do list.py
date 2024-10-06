import os

def add_task(tasks, description, final_date):
    tasks.append({"description": description, "final_date": final_date})

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['description']} - final Date: {task['final_date']}")

def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")

def save_tasks_to_file(tasks, file_path):
    with open(file_path, 'w') as f:
        for task in tasks:
            f.write(f"{task['description']}|{task['final_date']}\n")

def load_tasks_from_file(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                description, final_date = line.strip().split('|')
                tasks.append({"description": description, "final_date": final_date})
    return tasks

def main():
    tasks = []
    file_path = "tasks.txt"

    tasks = load_tasks_from_file(file_path)

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            description = input("Enter task description: ")
            final_date = input("Enter final date: ")
            add_task(tasks, description, final_date)
            save_tasks_to_file(tasks, file_path)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
            save_tasks_to_file(tasks, file_path)
        elif choice == '4':
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
