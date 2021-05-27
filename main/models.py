from django.db import models

# Create your models here.
class News(models.Model):
    nId = models.AutoField(primary_key=True)
    nHeadline = models.CharField(max_length=100)
    nBody = models.TextField()
    nPic = models.ImageField(upload_to = 'news/')
    def __str__(self):
        return f'{self.nHeadline}'

class Blogs(models.Model):
    bId = models.AutoField(primary_key=True)
    bHeadline = models.CharField(max_length=100)
    bBody = models.TextField()
    bPic = models.ImageField(upload_to = 'blogs/')
    def __str__(self):
        return f'{self.bHeadline}'