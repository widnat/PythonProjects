from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    complete = Column(Boolean, default=False)
    todos = relationship('Todo', back_populates='category')

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer(), ForeignKey('categories.id'))
    category = relationship('Category', back_populates='todos')
    name = Column(String)
    complete = Column(Boolean, default=False)