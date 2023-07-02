from django.shortcuts import render,redirect
from quizApp.models import TopicModel,QuestionModel,ResultModel,ChoiceModel
from django.views.generic import View

class HomeView(View):
    def get(self,request,*args,**kwargs):
          topics = TopicModel.objects.order_by("id")

          context = {
              "topics" : topics,
          }
          return render(request,'home.html',context)
    

          
#-------------------------------------------------------
class QuizView(View):
     def get(self,request,topic_id,question_id,*args,**kwargs):
            topic = TopicModel.objects.get(id=topic_id)

            topic_questions = topic.questions.all()
            question = topic_questions[question_id]

            context = {
                "question" : question
            }

            if question_id>0 and question_id < len(topic_questions)-1:
                  next = question_id + 1
                  previous = question_id -1
                  context["next"] = next
                  context["previous"] = previous

            elif question_id == 0:
                  next = question_id + 1
                  context["next"] = next
            elif question_id == len(topic_questions)-1 :
                  previous = question_id -1
                  context["previous"] = previous

            return render(request,"quiz.html",context)


        

        

    

    