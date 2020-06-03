from django.db import models

class User(models.Model):
    name = models.CharField( max_length=50)
    pw   = models.CharField( max_length=50)   

    def __str__(self):
        return self.name

class SavedVideos(models.Model):
    uid = models.IntegerField()

    def __str__(self):
        return self.name

class Recommended(models.Model):
    uid = models.IntegerField()
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class History(models.Model):
    uid = models.IntegerField()
    vid = models.IntegerField()

    def __str__(self):
        return self.name

class SearchHistory(models.Model):
    uid = models.IntegerField()
    qry = models.CharField(max_length=50)

    def __str__(self):
        return self.name