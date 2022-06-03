from django.shortcuts import render
from django.http import HttpResponse
from .forms import customRegistrationForm

# Create your views here.
def customUserRegister(request):
    form = customRegistrationForm
    if request.method == 'POST':
        form = customRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Successfully registered')
    return render(request, 'auth/register.html',{'form': form})