from sqlalchemy import select

from database import new_session, TasksTable
from schemas import NTaskAdd, NTask


class TasksRepository:
    @classmethod
    async def add_one(cls, data: NTaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[NTask]:
        async with new_session() as session:
            query = select(TasksTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [NTask.model_validate(task_model) for task_model in task_models]
            return task_schemas