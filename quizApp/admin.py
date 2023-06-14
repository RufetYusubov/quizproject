from django.contrib import admin
from quizApp.models import TopicModel,QuestionModel,ChoiceModel

admin.site.register(TopicModel)
admin.site.register(QuestionModel)
admin.site.register(ChoiceModel)
