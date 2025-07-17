from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("database tables deleted, creating tables...")
    await create_tables()
    print("app startup")
    yield
    print("app shutdown")

#test
app = FastAPI(lifespan=lifespan)


class NTaskAdd(BaseModel):
    task_name: str
    task_description: Optional[str] = None


class NTask(NTaskAdd):
    task_id: int

tasks = []

@app.post("/tasks")
async def create_task(task: Annotated[NTaskAdd, Depends()]):
    tasks.append(task)
    return {"ok": True}

# @app.get("/tasks")
# def get_task():
#     task = Task(task_name="test task", task_description="test task description")
#     return {"data": task}
