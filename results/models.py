from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User

# Create your models here.
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.FloatField()
    q_id = models.IntegerField(blank=True,null=True)
    u_id = models.IntegerField(blank=True,null=True)
    

    def __str__(self) :
        return str(self.pk)