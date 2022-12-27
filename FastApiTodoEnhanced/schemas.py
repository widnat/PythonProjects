from pydantic import BaseModel


class TodoBase(BaseModel):
    complete: str

class TodoCreate(TodoBase):
    name: str

class Todo(TodoBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    complete: bool

class CategoryCreate(CategoryBase):
    name: str

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

