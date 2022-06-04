from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class customRegistrationForm( UserCreationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')
        
class LoginForm(forms.Form):
    email=forms.CharField(max_length=50)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)
  