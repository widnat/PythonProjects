from django.db import models
        
class Category(models.Model):
    name = models.CharField(max_length = 350)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Todo(models.Model):
    name = models.CharField(max_length = 350)
    complete = models.BooleanField(default = False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name
