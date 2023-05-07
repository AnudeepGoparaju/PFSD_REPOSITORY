from django.db import models
# Create your models here.
class users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    age=models.CharField(max_length=200,null=True)
    balance=models.IntegerField(null=True)


class feed(models.Model):
    feedb=models.CharField(max_length=1024,null=True)




