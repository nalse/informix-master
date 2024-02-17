from django.db import models
from teacher.models import Teacher
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Lecture(models.Model):
     teacher  = models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
     adi = models.CharField(max_length=150)
     kateqoriya = models.CharField(max_length=100)
     body = RichTextField(blank=True,null=True)
     tarix = models.DateField(default=datetime.now, blank=True)
     photo    = models.ImageField(upload_to= 'photos/%y/%m/%d', blank=True, null=True)