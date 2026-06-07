from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class StudentCreate(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=100)
    course: str = Field(min_length=2, max_length=100)


class StudentUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=100)
    course: str = Field(min_length=2, max_length=100)


class StudentPatch(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    age: Optional[int] = Field(None, gt=0, lt=100)
    course: Optional[str] = Field(None, min_length=2, max_length=100)


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str

    model_config = ConfigDict(from_attributes=True)