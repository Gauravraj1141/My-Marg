from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    subscription = models.CharField(max_length=50)

    def __str__(self):
        return self.name
