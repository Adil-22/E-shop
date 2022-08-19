from django.db import models

class SignUp(models.Model):
    Full_name=models.CharField(max_length=50)
    Phone_no=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=500)
