from django.db import models

class Student(models.Model):
    studentName = models.CharField(max_length=20)
    grade=models.CharField(max_length=20)
    
    objects = models.Manager()

    def __str__(self):
        return self.studentName


