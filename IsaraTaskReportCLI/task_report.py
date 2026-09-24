import os
from datetime import datetime

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "/app/data")
REPORT_FILE = os.path.join(OUTPUT_DIR, "task_report.txt")

tasks = [
    {"name": "Complete Docker Task 4", "priority": "High", "status": "Completed"},
    {"name": "Test Docker deployment", "priority": "Medium", "status": "Completed"},
    {"name": "Verify persistent storage", "priority": "High", "status": "In Progress"},
]


def generate_report():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 55)
    print("       ISARA TASK REPORT - DOCKER CLI")
    print("=" * 55)

    completed = 0

    with open(REPORT_FILE, "w") as file:
        file.write("ISARA TASK REPORT\n")
        file.write("=" * 55 + "\n")
        file.write(f"Generated: {datetime.now()}\n\n")

        for number, task in enumerate(tasks, start=1):
            print(
                f"{number}. {task['name']} | "
                f"{task['priority']} | {task['status']}"
            )

            file.write(
                f"{number}. {task['name']} | "
                f"Priority: {task['priority']} | "
                f"Status: {task['status']}\n"
            )

            if task["status"] == "Completed":
                completed += 1

        file.write("\n")
        file.write(f"Total Tasks: {len(tasks)}\n")
        file.write(f"Completed Tasks: {completed}\n")

    print("-" * 55)
    print(f"Total Tasks: {len(tasks)}")
    print(f"Completed Tasks: {completed}")
    print(f"Report saved to: {REPORT_FILE}")
    print("=" * 55)


if __name__ == "__main__":
    generate_report()