from django.db import models
# Create your models here.
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=32)
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    user_email=models.CharField(max_length=32)    