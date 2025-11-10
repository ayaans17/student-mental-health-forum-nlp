from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.
class Forums(models.Model):

    name = models.CharField(max_length=100)
    desc = models.TextField()
    topics = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)

class iForum(models.Model):
    username=models.CharField(max_length=100)
    posts=models.TextField()
    pc=models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
