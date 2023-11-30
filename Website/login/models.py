from django.db import models

class data(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    Username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    Address= models.CharField(max_length=60)
# models.py

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

# models.py

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

