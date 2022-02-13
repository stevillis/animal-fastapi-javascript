from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class SexEnum(str, Enum):
    male = "macho"
    female = "femea"


class AnimalModel(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    age: int
    sex: SexEnum
    color: str


class AnimalUpdateModel(BaseModel):
    name: Optional[str]
    age: Optional[int]
    sex: Optional[SexEnum]
    color: Optional[str]
