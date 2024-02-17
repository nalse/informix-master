from django.db import models
from datetime import datetime


# Create your models here.

class Pages(models.Model):
    facebook_hesabi       = models.CharField(max_length=200)
    whatsapp_hesabi       = models.CharField(max_length=200)
    email_hesabi          = models.CharField(max_length=200)
    facebook_hesabi_url   = models.CharField(max_length=200,null=True)
    instagram_hesabi_url  = models.CharField(max_length=200, null=True)
    twitter_hesabi_url    = models.CharField(max_length=200, null=True)
    haqqimizda_photo      = models.ImageField(upload_to='photos/%y/%m/%d',null=True)
    haqqimizda_basliq     = models.TextField(null=True)
    haqqimizda_text       = models.TextField(null=True)

 


   

