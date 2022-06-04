from django.shortcuts import render
from django.http import HttpResponse
from .forms import customRegistrationForm
from django.contrib.auth.models import User
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
        return HttpResponse('Successfully registered')
    return render(request, 'auth/register.html',{'form': form})