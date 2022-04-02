
from django.shortcuts import render ,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout ,authenticate ,login  
# Createhere your views .
def home(request):
    return render(request, "base.html")
    
# it is for signup.
def sign_up(request):
  if request.method =="POST":
    fm = SignUpForm(request.POST)
    if fm.is_valid():
        messages.success(request,'accoutn has been created succesful')
        fm.save()
  else:
   fm = SignUpForm()
  return render(request,"sign_up.html",{'form':fm})
def user_login(request):
  if not request.user.is_authenticated:
    if request.method =="POST":
      fm = AuthenticationForm(request=request,data=request.POST)
      if fm.is_valid():
          uname = fm.cleaned_data['username']
          upass = fm.cleaned_data['password']
          user = authenticate(username=uname, password=upass)
          if user is not None:
            login(request,user)
            messages.success(request,'Logged in successfully')
            return HttpResponseRedirect('profile')
    else:
     fm = AuthenticationForm()
    return render(request, "login.html",{'form':fm})
  else:
     return HttpResponseRedirect('profile')
# this profile 
def profile(request):
  if request.user.is_authenticated:
    return render(request,"profile.html" ,{'name':request.user})
  else:
    return HttpResponseRedirect('user_login')
#this is regarding of logout page1
def user_logout(request):
  logout(request)
  return HttpResponseRedirect("user_login")