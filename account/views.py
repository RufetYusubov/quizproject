from django.shortcuts import render,redirect
from account.models import AccountModel
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import Http404

def check_password(password):
    if len(password)>=8:
        return True
    return False

def check_validation(password):
    has_digit, has_alpha = False, False
    for i in password:
        if i.isalpha():
            has_alpha = True
        elif i.isdigit():
            has_digit = True

    return has_digit and has_alpha


class SignupView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'signup.html')
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            if not check_password(password):
                messages.info(request, "Password must be at least 8 symbols")
                return redirect("signup")
            elif not check_validation(password):
                messages.info(request, "Password must contain both characters and numbers")
                return redirect("signup")
            else:
                User.objects.create_user(
                username=username,
                password=password
               )
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "You logged in")
                return redirect("login")
        else:
            messages.info(request,"Username has been taken")
            return redirect("signup")       
#--------------------------------------------------------------------------
class LoginView(View):
    def get(self,request,*args,**kwargs):

        return render(request,'login.html')
    
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"You logged in")
            return redirect("home")
        else:
            if not User.objects.filter(username=username).exists():
                messages.info(request, "Please enter correct username")
            else:
                messages.info(request,"Please enter correct password")
            return redirect("login")
#--------------------------------------------------------------------------------
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
#--------------------------------------------------------------------------------
class ChangePasswordView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'changepassword.html')
    def post(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            raise Http404
        username = request.POST.get("username")
        newpassword1 = request.POST.get("newpassword1")
        newpassword2 = request.POST.get("newpassword2")

        user = User.objects.get(username=username)
        if newpassword1 == newpassword2:
            user.set_password(newpassword1)
            user.save()
            messages.success(request, "Password changed")

            return redirect("login")





