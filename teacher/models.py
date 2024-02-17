from django.db import models
from datetime import datetime
# Create your models here.
class Teacher(models.Model):
    ad_soyad             = models.CharField(max_length=50)
    photo                = models.ImageField(upload_to= 'photos/%y/%m/%d')
    haqqinda             = models.TextField()
    email                = models.CharField(max_length=30)
    phone                = models.CharField(max_length=20)
    tarix                = models.DateTimeField(default=datetime.now, blank=True)
    facebook_hesabi_url  = models.CharField(max_length=100,null=True)
    twitter_hesabi_url   = models.CharField(max_length=100,null=True)
    instagram_hesabi_url = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.ad_soyad