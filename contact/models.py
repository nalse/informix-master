from django.db import models
from datetime  import datetime
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    video = models.CharField(max_length=200)
    video_id = models.IntegerField()
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    istifadeci = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    
    
class ContactLecture(models.Model):
    lecture_id = models.IntegerField()
    message = models.TextField()
    istifadeci = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)