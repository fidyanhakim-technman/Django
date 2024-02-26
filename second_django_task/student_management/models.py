from django.db import models

# Create your models here.

class Standard(models.Model):
    standard_name = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=20)

    def __str__(self):
        return self.standard_name

class Student(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.CharField(max_length=20)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.name
