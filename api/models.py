from django.db import models


# Create your models here.

class StudentModel(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    phone=models.CharField(max_length=12)
    batch=models.CharField(max_length=100)
    picture=models.ImageField(upload_to="student_pictures")



