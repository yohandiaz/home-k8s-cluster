from fastapi import FastAPI, HTTPException

from typing import Dict

from .models import Task

import uuid

app = FastAPI()

tasks: Dict[str, Task] = {}

@app.get("/")
async def root():
    return {"message": "To do app, please go to /docs to see the API documentation."}

@app.post("/tasks", response_model=Dict[str, Task])
def create_task(task: Task):
    """
    Create a new task.

    Args:
        task (Task): The task object to be created.

    Returns:
        dict: A dictionary containing the task ID as the key and the task object as the value.
    """
    task_id = str(uuid.uuid4())
    tasks[task_id] = task
    return {task_id: task}

@app.get("/tasks")
def show_all_tasks():
    """
    Retrieves and returns all tasks.

    Returns:
        list: A list of all tasks.
    """
    return tasks

@app.get("/tasks/{task_id}")
def show_task(task_id: str):
    """
    Retrieve a specific task by its ID.

    Parameters:
    - task_id (str): The ID of the task to retrieve.

    Returns:
    - dict: The task object.

    Raises:
    - HTTPException: If the task with the given ID is not found (status code 404).
    """
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    """
    Deletes a task with the given task_id.

    Args:
        task_id (str): The ID of the task to be deleted.

    Returns:
        dict: A dictionary with the detail message "Task deleted".

    Raises:
        HTTPException: If the task with the given task_id does not exist.
    """
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"detail": "Task deleted"}