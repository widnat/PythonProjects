from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    todos = db.relationship('Todo', backref='category')
    
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))
    name = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


db.create_all()


@app.get("/")
def home():
    categories = db.session.query(Category).all()
    return render_template("todo.html", categories=categories)

@app.get("/get_todos/<int:category_id>")
def get_todos(category_id):
    category = db.session.query(Category).filter(Category.id == category_id).first()
    return render_template("todo.html", todos=category.todos)

@app.post("/add_category")
def add_category():
    name = request.form.get("category_name")
    new_category = Category(name=name, complete=False)
    db.session.add(new_category)
    db.session.commit()
    return redirect(url_for("home"))
    
@app.post("/add_todo/<int:category_id>")
def add_todo(category_id):
    name = request.form.get("todo_name")
    new_todo = Todo(name=name, complete=False, category_id=category_id)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.get("/update_category/<int:category_id>")
def update_category(category_id):
    category = db.session.query(Category).filter(Category.id == category_id).first()
    category.complete = not category.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.get("/update_todo/<int:todo_id>")
def update_todo(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.get("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = db.session.query(Category).filter(Category.id == category_id).first()
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("home"))

@app.get("/delete_todo/<int:todo_id>")
def delete_todo(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))