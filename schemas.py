from typing import Optional

from pydantic import BaseModel


class NTaskAdd(BaseModel):
    title: str
    description: Optional[str] = None


class NTask(NTaskAdd):
    id: int


class NTaskId(BaseModel):
    ok: bool = True
    id: int