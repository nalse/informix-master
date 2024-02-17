from django.db import models
from datetime import datetime
# Create your models here.
class Quiz(models.Model):
    name= models.CharField(max_length=120)
    kateqoriya = models.CharField(max_length=120)
    sual_sayi = models.IntegerField()
    time = models.IntegerField(help_text="testin ishlenilme vaxti")
    required_score_to_pass = models.IntegerField(help_text="kecid bali",null=True)
    qiymet = models.IntegerField( blank=True, null=True)
    tarix = models.DateField(default=datetime.now, blank=True)

    
    def __str__(self):
        return f"{self.name}-{self.kateqoriya}"
    
    def get_questions(self):
       return self.question_set.all()[:self.sual_sayi]
    
   


class Meta:
    verbode_name_plural = "Quizes"