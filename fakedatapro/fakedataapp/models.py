from django.db import models

class FakeData(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    sal=models.IntegerField()
    loc=models.CharField(max_length=40)
    job=models.CharField(max_length=40)

