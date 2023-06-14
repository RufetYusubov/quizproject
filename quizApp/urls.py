from django.urls import path
from quizApp import views

urlpatterns = [
    path('home/',views.HomeView.as_view(),name="home")
]