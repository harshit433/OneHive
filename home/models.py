from django.db import models

# Create your models here.

class contact(models.Model):
    email = models.CharField(default = "abc@gmail.com", max_length=50, null=False)
    password = models.CharField( max_length=50 ,default='hjgbv',null=False)