from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=100, decimal_places=2)
    qrade = models.IntegerField()