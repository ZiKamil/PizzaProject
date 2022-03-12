from django.db import models


# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    composition = models.CharField(max_length=500)
    date_cooking = models.DateTimeField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
