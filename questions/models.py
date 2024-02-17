from django.db import models
from quizes.models import Quiz
from ckeditor.fields import RichTextField
# Create your models here.
class Question(models.Model):
    sual= RichTextField(blank=True,null=True)
    text = models.TextField(blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    hell = RichTextField(blank=True,null=True)


    def __str__(self):
        return str(self.text)
     
    def get_answers(self):
        return self.answer_set.all()
    


class Answer(models.Model):
    text = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"sual{self.question.text}, cavab: {self.text}, duzgun_cavab {self.correct} "





