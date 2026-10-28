from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class TaskInput(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def read_root():
    # TODO: Return a message confirming the API is running.
    raise NotImplementedError


@app.post("/tasks", response_model=Task)
def create_task(task_input: TaskInput):
    # TODO: Create a task, assign a unique ID, store it, and return it.
    raise NotImplementedError


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Return all stored tasks.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Return the requested task or raise HTTPException with status 404.
    raise NotImplementedError


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    # TODO: Update the requested task or raise HTTPException with status 404.
    raise NotImplementedError


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete the requested task or raise HTTPException with status 404.
    raise NotImplementedError
