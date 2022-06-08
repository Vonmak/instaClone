from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import customRegistrationForm, LoginForm, imageAddForm, commentAddForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .emails import send_welcome_email
from django.contrib.auth.decorators import login_required
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from .models import Image, Comment, Profile

# Create your views here.
def customUserRegister(request):
    form = customRegistrationForm
    if request.method == 'POST':
        form = customRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            # recipient = User(username=username, email=email)
            # send_welcome_email(username,email)
            user =  form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
          
            form.save()
        return redirect(login_user)
    return render(request, 'auth/register.html',locals())


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
    
    return render(request,'auth/login.html',locals())

def logout_user(request):
    logout(request)
    return redirect('/login')

# @login_required(login_url='/login')
def index(request):
    images = Image.get_images().order_by('-pub_date')
    profiles= Profile.objects.all()
    # likes = pic.total_likes()
    return render(request,'index.html',locals())


@login_required(login_url='/login')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.owner = current_user
            profile.save()
    else:
        form=ProfileForm()

    return render(request, 'profile/update.html', locals())


def profile(request, id):  
    user=User.objects.filter(id=id).first()
    profile = Profile.objects.get(owner=id)
    images = Image.filter_by_user(id).order_by('-pub_date')
    return render(request,"profile/profile.html",{'user':user, 'images':images, 'profile':profile})

def lookup_profile(request, id):
    profile = Profile.objects.get(id=id)
    images= Image.objects.filter(id=profile.id).order_by('-pub_date').all()
    return render(request,"profile/profile.html",{'images':images, 'profile':profile})

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
  
    return render(request, 'imageAdd.html', locals())  

def like(request, image_id):
    image = Image.objects.get(id=image_id)
    image.likes.add(request.user)
    image.save()
    return HttpResponseRedirect(reverse('imageView', args=[str(image_id)]))

def imageView(request, id):  
    pic = Image.objects.get(id=id)
    likes = pic.total_likes()
    return render(request,"imageView.html",locals())

@login_required(login_url='/login')
def commentAdd(request, image_id):  
    current_user = request.user
    current_image = Image.objects.get(id=image_id)
    if request.method == 'POST':   
        form = commentAddForm(request.POST)
        if form.is_valid(): 
            form = form.save(commit=False) 
            form.user=current_user 
            form.image=current_image
            form.save()  
              
            return redirect(index)  
    else:  
        form = commentAddForm()  
  
    return render(request, 'commentAdd.html', locals())  

def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(results)

        return render(request,'search.html',locals())

    return redirect(index)


def follow(request,user_id):
    users=User.objects.get(id=user_id)
    return redirect('/profile/', locals())
