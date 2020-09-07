from django.db import models

# Create your models here.'

class Client(models.Model):
        profile=models.ImageField(upload_to='media/img',null=True,blank=True)

