from typing import Optional

from pydantic import BaseModel


class NTaskAdd(BaseModel):
    task_name: str
    task_description: Optional[str] = None


class NTask(NTaskAdd):
    task_id: int