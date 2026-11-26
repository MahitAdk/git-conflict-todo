import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))


def add_task(tasks, title):
    tasks.append({"title": title, "done": False})


def complete_task(tasks, number):
    tasks[number - 1]["done"] = True


def delete_task(tasks, number):
    tasks.pop(number - 1)


def format_task(number, task):
    return f"{number}. [{'x' if task['done'] else ' '}] {task['title'].capitalize()}"


def ask_number(tasks):
    text = input("Task number: ").strip()
    if text.isdecimal() and 1 <= int(text) <= len(tasks):
        return int(text)
    print("Invalid task number")
    return None


def main():
    tasks = load_tasks()
    while True:
        choice = input("\n[a]dd  [l]ist  [c]omplete  [d]elete  [q]uit: ").strip().lower()
        if choice == "a":
            title = input("Task: ").strip()
            if title:
                add_task(tasks, title)
        elif choice == "l":
            if not tasks:
                print("No tasks yet")
            for number, task in enumerate(tasks, start=1):
                print(format_task(number, task))
        elif choice in ("c", "d"):
            number = ask_number(tasks)
            if number:
                action = complete_task if choice == "c" else delete_task
                action(tasks, number)
        elif choice == "q":
            break
        else:
            print("Unknown option")
        save_tasks(tasks)


if __name__ == "__main__":
    main()
