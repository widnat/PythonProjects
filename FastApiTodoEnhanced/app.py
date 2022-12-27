from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    categories = crud.get_categories(db)
    return templates.TemplateResponse("todo.html",
                                      {"request": request, "categories": categories})
                               
@app.get("/get_todos/{category_id}")
def get_todos(request: Request, category_id: int, db: Session = Depends(get_db)):
    todos = crud.get_todos(category_id, db)
    return templates.TemplateResponse("todo.html",
                                      {"request": request, "todos": todos})

@app.post("/add_category", response_model=schemas.Category)
def add_category(request: Request, category_name: str = Form(...), db: Session = Depends(get_db)):
    new_category = crud.add_category(category_name, db)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
    
@app.post("/add_todo/{category_id}", response_model=schemas.Todo)
def add_todo(request: Request, category_id: int, todo_name: str = Form(...), db: Session = Depends(get_db)):
    new_todo = crud.add_todo(category_id, todo_name, db)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/update_category/{category_id}", response_model=schemas.Category)
def update_category(request: Request, category_id: int, db: Session = Depends(get_db)):
    category = crud.update_category(category_id, db)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

@app.get("/update_todo/{todo_id}", response_model=schemas.Todo)
def update_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = crud.update_todo(todo_id, db)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

@app.get("/delete_category/{category_id}")
def delete_category(request: Request, category_id: int, db: Session = Depends(get_db)):
    success = crud.delete_category(category_id, db)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
    
@app.get("/delete_todo/{todo_id}")
def delete_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
    sucess = crud.delete_todo(todo_id, db)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)