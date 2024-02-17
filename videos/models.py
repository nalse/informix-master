from django.db import models
from teacher.models import Teacher
from datetime import datetime
# Create your models here.
class Video(models.Model):
    teacher  = models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
    photo    = models.ImageField(upload_to= 'photos/%y/%m/%d', null=True)
    basliq = models.CharField(max_length=300)
    video_haqqinda =models.TextField()
    kateqoriya = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    tarix =models.DateField(default =datetime.now,blank=True)
    