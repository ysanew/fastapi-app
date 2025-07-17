from typing import Annotated

from fastapi import Depends, APIRouter

from repository import TasksRepository
from schemas import NTaskAdd, NTask

router = APIRouter(
    prefix = "/tasks",
    tags = ["tasks"]
)


@router.post("")
async def create_task(task: Annotated[NTaskAdd, Depends()]):
    task_id = await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_task() -> list[NTask]:
    tasks = await TasksRepository.get_all()
    return tasks
