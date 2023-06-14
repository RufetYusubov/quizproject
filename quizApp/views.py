from django.shortcuts import render,redirect
from quizApp.models import TopicModel,QuestionModel,ResultModel,ChoiceModel
from django.views.generic import View

class HomeView(View):
    def get(self,request,*args,**kwargs):
          topics = TopicModel.objects.order_by("name")

          context = {
              "topics" : topics,
          }
          return render(request,'home.html',context)
    
    def post(self,request,*args,**kwargs):
        choice_id = request.POST.get("choice_id")
        choice = ChoiceModel.objects.get(id=choice_id)

        ResultModel.objects.create(
             user = request.user,
             choice = choice
        )

        return redirect("home")

          
#-------------------------------------------------------
      

        

    

    