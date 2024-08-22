from django.db import models

# Create your models here.

class UserData(models.Model):
  user_id = models.CharField(max_length=50, unique=True)
  language = models.IntegerField(blank=True, null=True)
  mode = models.IntegerField(blank=True, null=True)
  
class LanguageData(models.Model):
  lang_ja = models.CharField(max_length=20)
  lang_en = models.CharField(max_length=5)
  
class AllWordData(models.Model):
  word = models.CharField(max_length=50)
  read = models.CharField(max_length=100)
  mean = models.CharField(max_length=200)
  language = models.IntegerField()

class OriginalWordData(models.Model):
  user = models.IntegerField()
  word = models.CharField(max_length=50)
  read = models.CharField(max_length=100)
  mean = models.CharField(max_length=200)

class UserWordData(models.Model):
  user = models.IntegerField()
  word = models.IntegerField()
  count = models.IntegerField(default=1)
  quiz = models.IntegerField(default=1)
  correct = models.IntegerField(default=1)
  probability = models.IntegerField(default=1)
  period = models.IntegerField(default=30)
  hide = models.BooleanField(default=False)
  
class ModeData(models.Model):
  name = models.CharField(max_length=50, unique=True)