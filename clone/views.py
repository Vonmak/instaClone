from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .forms import customRegistrationForm, LoginForm, imageAddForm, commentAddForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .emails import send_welcome_email
from django.contrib.auth.decorators import login_required
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from .models import Image, Comment, Profile, Follow

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
            return redirect(index)
    else:
        form=ProfileForm()

    return render(request, 'profile/update.html', locals())


def profile(request, id):  
    user=User.objects.filter(id=id).first()
    profile = Profile.objects.get(owner=id)
    images = request.user.profile.images.all().order_by('-pub_date')
    return render(request,"profile/profile.html",{'user':user, 'images':images, 'profile':profile})

def lookup_profile(request, id):
    profile = Profile.objects.get(id=id)
    user = User.objects.get(id=profile.owner.id)
   
    images = Image.filter_by_user(id)
    user_prof = get_object_or_404(User, id=id)
    if request.user == user_prof:
        return redirect('profile', id=request.user.id)
    user_posts = user_prof.profile.images.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    folo =Follow.objects.all()
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
            
    print(followers)
    print(profile)
    print(images)
    print(user)
    return render(request,"profile/profile.html",{'images':images, 'profile':profile, 'user_prof': user_prof,'user_posts': user_posts,'followers': followers, 'follow_status': follow_status})

@login_required(login_url='/login')
def image_request(request):  
    current_user = request.user
    if request.method == 'POST':   
        form = imageAddForm(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.user=request.user
            post.profile=request.user.profile
            post.save() 
            return redirect(index) 
              
            # return HttpResponseRedirect(request.path_info)  
    else:  
        form = imageAddForm()  
  
    return render(request, 'imageAdd.html', {'form':form})  

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


def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objects.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('profile', user_profile2.owner.id)


def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('profile', user_profile3.owner.id)
