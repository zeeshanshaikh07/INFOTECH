from django.db import models

# Create your models here.
class news(models.Model):
    nId = models.AutoField(primary_key=True)
    nHeadline = models.CharField(max_length=100)
    nBody = models.TextField()
    nPic = models.ImageField(upload_to = 'news/')

class blogs(models.Model):
    bId = models.AutoField(primary_key=True)
    bHeadline = models.CharField(max_length=100)
    bBody = models.TextField()
    bPic = models.ImageField(upload_to = 'blogs/')