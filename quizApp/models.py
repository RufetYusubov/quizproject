from django.db import models
from django.contrib.auth.models import User

class TopicModel(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='posters/',blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
class QuestionModel(models.Model):
    topic = models.ForeignKey(TopicModel,on_delete=models.CASCADE,related_name="questions")
    question = models.TextField()

    def __str__(self) -> str:
        return self.question

class ChoiceModel(models.Model):
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE,related_name="choices") 
    choice = models.TextField()
    correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.choice

class ResultModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="results")
    choice = models.ForeignKey(ChoiceModel,on_delete=models.CASCADE,related_name="choices")

    def __str__(self) -> str:
        return self.user.username