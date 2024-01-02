from django.db import models

# Create your models here.


class Cat(models.Model):
    age = models.IntegerField(null=True, default=-1)
    color = models.TextField(null=True)
    gender = models.BooleanField(default=0) #0:Man 1:Woman

class MyModel(models.Model):
    asdf = models.TextField(null=True)
