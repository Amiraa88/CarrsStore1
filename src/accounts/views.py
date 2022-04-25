from django.shortcuts import render ,redirect
#from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
#from django.contrib.auth.models import  User,auth
#from .models import Profile
from .forms import   SignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate ,login

# Create your views here.
#def login(request):
   
  #  return render(request,'registration/login.html')
def signup(request):
    
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=username,password=password)
            login(request, user)
            return redirect('/product')
    else:
       form=SignupForm()
    return render(request,'registration/signup.html',{'form':form})     
   