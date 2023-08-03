from django.db import models

# Create your models here.

class Person(models.Model):
  
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  eye_color = models.CharField(max_length=15)
  