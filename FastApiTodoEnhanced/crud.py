from sqlalchemy.orm import Session

import models, schemas

def get_categories(db: Session):
    return db.query(models.Category).all()
                                      
def get_todos(category_id: int, db: Session):
    category = db.session.query(models.Category).filter(models.Category.id == category_id).first()
    return category.todos

def add_category(category_name: str, db: Session):
    new_category = models.Category(name=category_name)
    db.add(new_category)
    db.commit()
    return new_category

def add_todo(category_id: int, todo_name: str, db: Session):
    new_todo = models.Todo(name=todo_name, category_id=category_id)
    db.add(new_todo)
    db.commit()
    return new_todo

def update_category(category_id: int, db: Session):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    category.complete = not category.complete
    db.commit()
    return category

def update_todo(todo_id: int, db: Session):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()
    return todo

def delete_category(category_id: int, db: Session):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    db.delete(category)
    db.commit()
    return True
    
def delete_todo(todo_id: int, db: Session):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return True