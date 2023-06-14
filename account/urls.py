from django.urls import path
from account import views

urlpatterns = [
    path('signup/',views.SignupView.as_view(),name="signup"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('changepassword/',views.ChangePasswordView.as_view(),name="changepassword")
]