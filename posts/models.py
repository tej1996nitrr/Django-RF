from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length= 50)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now) 
    category = models.ManyToManyField('Category')
    print(category.name)
    def __str__(self):
        return self.title



