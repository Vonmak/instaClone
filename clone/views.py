from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import customRegistrationForm, LoginForm, imageAddForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .emails import send_welcome_email
from django.contrib.auth.decorators import login_required
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from .models import Image


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
                return redirect(index)
            else:
                return HttpResponse('Such a user does not exist')
        else:
            return HttpResponse("Form is not Valid")
    
    return render(request,'auth/login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def index(request):
    images = Image.get_images()
    return render(request,'index.html',{'images': images})

def profile(request, id):  
    user = User.objects.get(id=id)
    return render(request,"profile/profile.html")

@login_required(login_url='/login')
def image_request(request):  
    current_user = request.user
    if request.method == 'POST':   
        form = imageAddForm(request.POST, request.FILES)
        if form.is_valid(): 
            form = form.save(commit=False) 
            form.user=current_user 
            form.save()  
              
            return redirect(index)  
    else:  
        form = imageAddForm()  
  
    return render(request, 'imageAdd.html', {'form': form})  

def like(request, image_id):
    image = Image.objects.get(id=image_id)
    image.likes.add(request.user)
    image.save()
    return HttpResponseRedirect(reverse('imageView', args=[str(image_id)]))

def imageView(request, id):  
    pic = Image.objects.get(id=id)
    likes = pic.total_likes()
    return render(request,"imageView.html",{'pic': pic, 'likes': likes})
