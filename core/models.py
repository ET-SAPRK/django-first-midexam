from django.db import models


class Student(models.Model):
    studentName = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, default='female')
    grade = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.studentName
