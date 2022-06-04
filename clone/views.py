from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import customRegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .emails import send_welcome_email

# Create your views here.
def customUserRegister(request):
    form = customRegistrationForm
    if request.method == 'POST':
        form = customRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            recipient = User(first_name=first_name, email=email)
            send_welcome_email(first_name,email)
            form.save()
        return redirect(login_user)
    return render(request, 'auth/register.html',{'form': form})


def login_user(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            usern=form.cleaned_data['email']
            passw=form.cleaned_data['password']
            user=authenticate(request,username=usern,password=passw)
            if user is not None:
                login(request,user)
                return HttpResponse('Login successful')
            else:
                return HttpResponse('Such a user does not exist')
        else:
            return HttpResponse("Form is not Valid")
    
    return render(request,'auth/login.html',{'form':form})

