from django.db import models

# Create your models here.
class Nationality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=50)
    breed = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True)
    favourited_by = models.CharField(max_length=50)

    def __str__(self):
        return self.name