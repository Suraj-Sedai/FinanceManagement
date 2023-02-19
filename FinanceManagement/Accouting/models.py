from django.db import models

class Expense(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField()
