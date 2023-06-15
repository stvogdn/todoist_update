from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.api import TodoistAPI
import asyncio

# Fetch tasks asynchronously
async def get_tasks_async():
    api = TodoistAPIAsync("efe5fb6965803037d1fb11a2f18b8e629d9339ce")
    try:
        tasks = await api.get_tasks(filter="No due date")
        for task in tasks:
            print(f'ID: {task.id} - Content: {task.content}')
    except Exception as error:
        print(error)
