from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('get_todos/<int:category_id>', views.get_todos, name="get_todos"),
    path('add_category', views.add_category, name="add_category"),
    path('add_todo/<int:category_id>', views.add_todo, name="add_todo"),
    path('update_category/<int:category_id>', views.update_category, name="update_category"),
    path('update_todo/<int:todo_id>', views.update_todo, name="update_todo"),
    path('delete_category/<int:category_id>', views.delete_category, name="delete_category"),
    path('delete_todo/<int:todo_id>', views.delete_todo, name="delete_todo"),
]