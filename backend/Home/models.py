from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=32,unique=True)
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    user_email=models.CharField(max_length=32)    

class Board(models.Model):
    board_id=models.AutoField(primary_key=True)
    board_name=models.CharField(max_length=32)

class Task(models.Model):
    task_id=models.AutoField(primary_key=True)
    task_name=models.CharField(max_length=32)
    task_desc=models.TextField(max_length=128)
    time_stamp=models.DateTimeField(auto_now_add=True)
    task_status=models.CharField(max_length=16)
    board=models.ForeignKey(Board,on_delete=models.CASCADE,null=True)

class UserBoard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    board=models.ForeignKey(Board,on_delete=models.CASCADE,null=True)
    class Meta:
        # Define a unique constraint for the composite primary key
        constraints = [
            models.UniqueConstraint(fields=['user', 'board'], name='composite_key_constraint')
        ]