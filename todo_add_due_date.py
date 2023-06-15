
from todoist_api_python.api import TodoistAPI
from datetime import date

# get inbox project
def get_inbox_project(api : TodoistAPI):
    try:
        projects = api.get_projects()
        for project in projects:
            if project.is_inbox_project:
                return project.id
        return None
    except Exception as error:
        print(error)

# Fetch tasks synchronously
def get_tasks_sync(api : TodoistAPI, inbox_project_id : int):
    try:
        tasks = api.get_tasks(filter = "No due date", project_id = inbox_project_id)
        return tasks
    except Exception as error:
        print(error)

# main
def main():
    api = TodoistAPI("efe5fb6965803037d1fb11a2f18b8e629d9339ce")
    inbox_project_id = get_inbox_project(api)
    tasks = get_tasks_sync(api, inbox_project_id)
    if tasks is None:
        print("No tasks found")
        return

    today = date.today().strftime("%Y-%m-%d")
    for task in tasks:
        print(f'ID: {task.id} - Content: {task.content}')
        try:
            is_success = api.update_task(task_id=task.id, due_date=today, priority=2)
        except Exception as error:
            print(error)

if __name__ == "__main__":
    main()

