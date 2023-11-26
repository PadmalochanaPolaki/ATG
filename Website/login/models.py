from django.db import models

class data(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    Username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    Address= models.CharField(max_length=60)
