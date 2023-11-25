# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    departent = models.CharField(max_length=10)
    rollnumber = models.IntegerField()
    accountnumber = models.IntegerField()
    amount = models.IntegerField()
    dateofpayment = models.DateField(default='2023-11-27')  # Set a default value here

    def __str__(self):
        return self.name
