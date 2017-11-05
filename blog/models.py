from __future__ import unicode_literals

from django.db import models
import time

class Blog(models.Model):
    id = models.IntegerField(auto_created=1,primary_key=True,default=0)
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=10240)
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)
    comments  = models.IntegerField(default=0)
    views = models.IntegerField(default=0)


class Comment(models.Model):
    id = models.IntegerField(auto_created=1,primary_key=True,default=0)
    blog_id = models.ForeignKey(Blog)
    content = models.CharField(max_length=10240)
    username = models.CharField(max_length=32)
    dataTime = models.DateTimeField(default=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)

class Statistics(models.Model):
    id = models.IntegerField(auto_created=1,primary_key=True,default=0)
    blog_id = models.ForeignKey(Blog)
    view = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
# Create your models here.
