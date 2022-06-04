from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.customUserRegister),
     path('login/',views.login_user),
]