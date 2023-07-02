from django.urls import path
from quizApp import views

urlpatterns = [
    path('home/',views.HomeView.as_view(),name="home"),
    path('<int:topic_id>/<int:question_id>/',views.QuizView.as_view(),name="quiz")
]