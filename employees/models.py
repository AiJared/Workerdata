from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)