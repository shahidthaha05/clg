from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
    coursee=models.TextField()