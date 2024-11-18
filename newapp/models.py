from __future__ import unicode_literals
from django.db import models
class Student1(models.Model):
    first_name = models.CharField(max_length=10)
    last_name  = models.CharField(max_length=10)
    current_designation= models.CharField(max_length=20)
    contact    = models.IntegerField()
    email      = models.EmailField(max_length=20)
    address    = models.CharField(max_length=50)
    age        = models.CharField(max_length=15)
    image      = models.FileField( 
        upload_to="news/",
        max_length=500,
        null=True,
        default= None,
    )

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    class Meta:
        db_table ="student"

 
    