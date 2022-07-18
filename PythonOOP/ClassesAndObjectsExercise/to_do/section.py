from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = list()

    def add_task(self, new_task: Task):
        for task in self.tasks:
            if task == new_task:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        old_list = self.tasks
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
        tasks_cleared = len(old_list) - len(self.tasks)
        return f"Cleared {tasks_cleared} tasks."

    def view_section(self):
        result = f"Section {self.name}:" + '\n'
        for task in self.tasks:
            result += task.details() + '\n'
        return result.strip()

