from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50 , null=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50,  null=True)
    email = models.EmailField (max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)

def __str__(self):
  return f'{self.username} {self.password}'
