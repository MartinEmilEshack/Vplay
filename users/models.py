from django.db import models
from videos.models import Video

class User(models.Model):
    name = models.CharField( max_length=50)
    pw   = models.CharField( max_length=50)   

    def __str__(self):
        return self.name

class SavedVideos(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    vid = models.ForeignKey(Video,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name

class Recommended(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class History(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    vid = models.ForeignKey(Video,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name

class SearchHistory(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    qry = models.CharField(max_length=100)

    def __str__(self):
        return self.name